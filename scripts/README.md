# Scripts

The public repository contains analysis logic, not benchmark content.

## Included

- `check_sleight_repo.py` — verifies a local SLEIGHT-Bench checkout against the frozen manifest and the four frozen monitor prompts; emits `repo_audit.json` with SHA-256 hashes. It reads prompt/manifest files for hashing only and does not read or emit benchmark transcript content.
- `summarize_run.py` — reads a completed run directory (`run_meta.json`, `raw_results.jsonl`) and produces a minimal summary plus an upload manifest. It consumes result metadata, not benchmark transcripts.

## Safety checks applied before inclusion

- no benchmark-data leakage (scripts reference file names and hashes, not transcript text)
- no hard-coded local paths
- no credentials
- no provider-specific secrets
- no accidental inclusion of decrypted transcript content

Scripts that read or decrypt benchmark transcripts are intentionally **not** published here.
