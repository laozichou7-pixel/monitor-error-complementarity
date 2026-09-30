# Publish this repository to GitHub

Recommended repository name:

`monitor-error-complementarity`

Recommended description:

> Preregistered study of rule-induced AI monitor diversity, correlated misses, and ensemble complementarity.

## GitHub website + Git

1. Create a new **public** repository named `monitor-error-complementarity`.
2. Do **not** initialize it with README, license, or `.gitignore`.
3. Open a terminal in this folder.
4. Run:

```bash
git init
git branch -M main
git add .
git status
git commit -m "Initial public research package"
git remote add origin https://github.com/YOUR_USERNAME/monitor-error-complementarity.git
git push -u origin main
```

## Or GitHub CLI

After `gh auth login`:

```bash
git init
git add .
git status
git commit -m "Initial public research package"
gh repo create monitor-error-complementarity --public --source=. --remote=origin --push
```

## Before pushing

Inspect `git status` carefully.

Verify that no benchmark transcript, API key, `.env`, or raw provider request has been staged.

## License

Do not add a license until you decide how you want others to reuse the code and documents.
