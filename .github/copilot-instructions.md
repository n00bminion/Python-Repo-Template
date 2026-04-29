# Copilot instructions for this repository
# These are always included in Copilot context for this workspace.

## Project layout
- Source code lives under `src/<package-name>/` (src layout)
- Tests live under `tests/`
- A placeholder `tests/test_pkg.py` exists — add real tests alongside it

## Build & packaging
- Uses `setuptools` with `setuptools-scm` for automatic version from git tags
- Version is written to `src/<package-name>/_version.py` — do not edit it manually
- Runtime dependencies go in `requirements.txt`
- Dev-only dependencies (pytest, pytest-cov) go in `[project.optional-dependencies] dev` in `pyproject.toml`
- Install for development: `pip install -e ".[dev]"`

## Code style
- Linting and formatting: **ruff** (`ruff check`, `ruff format`)
- Rules in `[tool.ruff.lint]` in `pyproject.toml`: E (pycodestyle errors), F (pyflakes), I (isort)
- Quote style: double quotes

## Testing
- Test runner: **pytest**
- Config in `[tool.pytest.ini_options]` in `pyproject.toml`
- Coverage: `pytest-cov`, reports to terminal with `--cov=src --cov-report=term-missing`
- Run tests: `pytest`

## Pre-commit hooks (run automatically before every commit)
- `ruff-check --fix` — lint and auto-fix
- `ruff-format` — format
- `check-yaml`, `check-toml` — config file syntax
- `end-of-file-fixer`, `trailing-whitespace` — file hygiene
- `check-merge-conflict` — no forgotten conflict markers
- `requirements-txt-fixer` — keeps requirements.txt sorted
- Install hooks: `pre-commit install`

## CI (GitHub Actions — `.github/workflows/template.yaml`)
- Runs on every push and pull request
- Matrix: Python 3.12 and 3.13 × ubuntu-latest and windows-latest
- Steps: install → pre-commit → pytest

## Python version
- Minimum supported: Python 3.12
