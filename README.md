# PythonRepoTemplate

A GitHub template for Python packages using `setuptools-scm` for versioning, `ruff` for linting/formatting, `pytest` for testing, and `pre-commit` for code quality hooks.

## Getting started

### 1. Create your new repo from this template

On GitHub, click **Use this template → Create a new repository** and give your repo a name (e.g. `My-Awesome-Lib`).

### 2. Clone your new repo locally

```bash
git clone https://github.com/<your-username>/My-Awesome-Lib.git
cd My-Awesome-Lib
```

### 3. Run the setup prompt in VS Code

Open the repo in VS Code, then in the Copilot Chat panel type:

```
/new-project
```

Copilot will automatically detect your project name from the git remote and then:

- Rename `src/pkg/` → `src/<package-name>/`
- Update `pyproject.toml` with your project and package names
- Update the placeholder test to import your package
- Remove the stale `pkg_name.egg-info/` directory
- Create a `.venv` virtual environment and install the package in editable mode (`pip install -e ".[dev]"`)
- Install pre-commit hooks into `.venv`
- Delete this README and the `.github/prompts/` folder

> The project name is taken from your GitHub repo name (e.g. `My-Awesome-Lib`).
> The importable package name is derived automatically by lowercasing and replacing hyphens with underscores (e.g. `my_awesome_lib`).
> You will be shown the detected names and asked to confirm before any changes are made.
> To override the package name: `/new-project my_custom_name` (must be lowercase with underscores)
> The prompt and `.github/prompts/` folder are deleted after setup so it can't be run again.

### 4. Finish setup

Run the tests to verify everything is working:

```bash
.venv\Scripts\pytest
```

Then add your source code under `src/<package-name>/` and start building.

## What's included

| Tool | Purpose |
|---|---|
| `setuptools-scm` | Derives the package version from git tags — no manual version bumps |
| `ruff` | Fast Python linter and formatter |
| `pytest` + `pytest-cov` | Test runner with coverage reporting |
| `pre-commit` | Runs ruff and common file checks before each commit |
| GitHub Actions | CI matrix across Ubuntu and Windows on push/PR |
| Dependabot | Keeps GitHub Actions, pip dependencies, and pre-commit hooks up to date |

## Versioning

Versions are derived from git tags via `setuptools-scm`. To release a version:

```bash
git tag v1.0.0
git push origin v1.0.0
```
