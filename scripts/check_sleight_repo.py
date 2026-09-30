#!/usr/bin/env python3
import argparse, csv, json, hashlib
from pathlib import Path

PROMPTS = [
    "control_arena",
    "state_tracking",
    "control_arena_doc_planting_aware",
    "control_arena_env_awareness",
]

def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--manifest", default=str(Path(__file__).resolve().parents[1] / "prereg" / "split_manifest.csv"))
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "repo_audit.json"))
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    manifest_path = Path(args.manifest).resolve()
    errors = []
    prompt_hashes = {}

    for name in PROMPTS:
        p = repo / "prompts" / f"{name}.md"
        if not p.exists():
            errors.append(f"missing prompt: {p}")
        else:
            prompt_hashes[name] = sha256(p)

    exp = repo / "experiment_paper.yaml"
    if not exp.exists():
        errors.append(f"missing: {exp}")

    rows = list(csv.DictReader(manifest_path.open(encoding="utf-8")))
    missing_dirs = []
    missing_decrypted = []
    transcript_count = 0

    for row in rows:
        for rel in row["source_dirs"].split(";"):
            d = repo / rel
            if not d.exists():
                missing_dirs.append(rel)
                continue
            t = d / "transcript.jsonl"
            b = d / "benign.jsonl"
            if not t.exists() or not b.exists():
                missing_decrypted.append(rel)
            else:
                transcript_count += 1

    audit = {
        "repo": str(repo),
        "manifest": str(manifest_path),
        "attack_units_manifest": len(rows),
        "source_transcript_directories_present_and_decrypted": transcript_count,
        "dev_units": sum(r["split"] == "DEV" for r in rows),
        "test_units": sum(r["split"] == "TEST" for r in rows),
        "prompt_sha256": prompt_hashes,
        "experiment_paper_sha256": sha256(exp) if exp.exists() else None,
        "missing_dirs": missing_dirs,
        "missing_decrypted_dirs": missing_decrypted,
        "errors": errors,
    }
    Path(args.out).write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(audit, ensure_ascii=False, indent=2))
    if errors or missing_dirs or missing_decrypted:
        raise SystemExit(2)
    print("\nOK: repository, frozen prompts, manifest mapping, and decrypted transcript pairs are present.")

if __name__ == "__main__":
    main()
