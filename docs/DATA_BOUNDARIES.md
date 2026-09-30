# Data and Provider Boundaries

## Benchmark data

This public repository must not contain decrypted SLEIGHT benchmark transcripts.

Do not commit:

- decrypted `transcript.jsonl`;
- decrypted `benign.jsonl`;
- `transcript_non_triggering.jsonl`;
- benchmark caches containing transcript text;
- copied benchmark content;
- API request logs containing full benchmark transcripts.

## Secrets

Never commit:

- API keys;
- `.env` files containing credentials;
- terminal history containing credentials;
- provider account tokens.

## Provider gate

Engineering smoke tests may use synthetic data.

Real benchmark data should only be transmitted to an external provider when the project's data-governance requirements are satisfied and the decision is documented.

## Empirical labeling

Synthetic smoke results are engineering validation only.

They must not be presented as evidence about monitor performance on SLEIGHT.
