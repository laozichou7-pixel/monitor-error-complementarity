#!/usr/bin/env python3
import argparse, json, statistics
from collections import Counter, defaultdict
from pathlib import Path

def mean(xs):
    return statistics.fmean(xs) if xs else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    d = Path(args.run)
    rp = d / "raw_results.jsonl"
    if not rp.exists():
        raise SystemExit(f"Missing {rp}")

    rows = [json.loads(x) for x in rp.read_text(encoding="utf-8").splitlines() if x.strip()]
    errors = []
    ep = d / "errors.jsonl"
    if ep.exists():
        errors = [json.loads(x) for x in ep.read_text(encoding="utf-8").splitlines() if x.strip()]

    by_monitor_sample = defaultdict(list)
    parse_fail = 0
    models = Counter()
    total_input = total_output = 0

    for r in rows:
        models[str(r.get("model_returned"))] += 1
        if not r.get("parse_ok"):
            parse_fail += 1
        elif r.get("score") is not None:
            by_monitor_sample[(r["monitor_id"], r["sample_type"])].append(float(r["score"]))
        usage = r.get("usage") or {}
        total_input += int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        total_output += int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)

    scores = {}
    for (m,s), xs in sorted(by_monitor_sample.items()):
        scores[f"{m}:{s}"] = {
            "n": len(xs),
            "mean": mean(xs),
            "min": min(xs) if xs else None,
            "max": max(xs) if xs else None,
        }

    summary = {
        "completed_rows": len(rows),
        "error_rows": len(errors),
        "parse_failures": parse_fail,
        "parse_success_rate": (len(rows)-parse_fail)/len(rows) if rows else 0,
        "returned_models": dict(models),
        "token_usage_observed": {"input_or_prompt": total_input, "output_or_completion": total_output},
        "score_summary": scores,
        "important_note": "Smoke/dev1 summaries are engineering diagnostics. Do not estimate a stable 1% FPR operating point from tiny benign samples.",
    }
    (d / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    upload_manifest = """Upload back to ChatGPT:
- run_meta.json
- raw_results.jsonl
- summary.json
- errors.jsonl (if it exists)
- repo_audit.json (from the handoff root, if available)

Do NOT upload:
- API keys or shell history containing them
- decrypted SLEIGHT transcript.jsonl / benign.jsonl
- encrypted benchmark copies are also unnecessary
"""
    (d / "UPLOAD_MANIFEST.txt").write_text(upload_manifest, encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("\nWrote summary.json and UPLOAD_MANIFEST.txt")

if __name__ == "__main__":
    main()
