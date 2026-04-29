# PythonRepoTemplate

A template repository for creating new Python packages quickly — batteries included.

---

## What's included

| Tool | Purpose |
|------|---------|
| **setuptools + setuptools-scm** | Build system; version derived automatically from git tags — no manual version bumps |
| **src layout** | Source lives under `src/<package>/` to prevent accidental imports of the uninstalled package |
| **ruff** | Fast linting (`ruff check`) and formatting (`ruff format`) in one tool, replacing flake8 + black + isort |
| **pre-commit** | Git hook runner — enforces lint, format, and file hygiene checks before every commit |
| **pytest + pytest-cov** | Test runner with code coverage reporting; configured in `pyproject.toml` |
| **GitHub Actions CI** | Runs pre-commit and pytest on every push and PR across Python 3.12 & 3.13 on Ubuntu and Windows |
| **Dependabot** | Weekly PRs to keep GitHub Actions and pip dependencies up to date automatically |
| **Copilot prompt** | `/new-project` slash command to rename and wire up a new project in seconds |
| **copilot-instructions.md** | Always-on Copilot context with repo conventions so you don't re-explain them in every chat |

---

## Creating a new project from this template

### Option 1 — VS Code + Copilot (local, recommended)

1. **Clone or duplicate this template** — use GitHub's **"Use this template"** button, or clone directly.
2. **Open the new folder in VS Code.**
3. **Activate the virtual environment** (see [Setup](#setup) below) and make sure GitHub Copilot is installed.
4. **Open Copilot Chat in Agent mode** (`Ctrl+Alt+I`).
5. **Type `/` and select `new-project`** from the prompt list.
6. **Run it with your names:**
   ```
   /new-project <project-name> <package-name>
   ```
   For example:
   ```
   /new-project my-awesome-lib my_awesome_lib
   ```
   - `project-name` — distribution/PyPI name, typically hyphen-separated (used in `pyproject.toml`)
   - `package-name` — importable Python name, typically underscore-separated (used for the `src/` folder)

   If you only provide one name, the other is derived automatically.

7. Copilot will:
   - Update `pyproject.toml` with your names
   - Rename `src/pkg/` → `src/<package-name>/`
   - Update the placeholder test import
   - Clean up the stale egg-info
   - Reinstall with `pip install -e ".[dev]"`

8. **Review the changes**, run `pytest` to verify, then commit to git.

---

### Option 2 — GitHub Copilot cloud agent (PR-based workflow)

1. **Push this template to GitHub** and enable Copilot in the repository settings (Settings → Copilot).
2. **Create a new Issue** describing the setup, for example:
   > Set up this repo as a new project called `my-awesome-lib` with package name `my_awesome_lib`.
3. **Assign the issue to @copilot** — click *Assignees* → select *Copilot*.
4. Copilot reads the repo, makes the changes, and **opens a Pull Request** for you to review and merge.

This approach is better when you want a review trail or are working with a team.

---

## Setup

### Create and activate the virtual environment
```console
cd <your project root directory>
python -m venv .venv
.\.venv\Scripts\activate        # Windows
source .venv/bin/activate       # macOS / Linux
```

### Install with dev dependencies (recommended)
```console
pip install -e ".[dev]"
```
This installs the package in editable mode plus `pytest` and `pytest-cov`.

### Install runtime only
```console
pip install -e .
```

---

## Running tests
```console
pytest
```
Coverage is reported automatically (`--cov=src --cov-report=term-missing` is set in `pyproject.toml`).

---

## Pre-commit hooks

Install hooks to run automatically before every commit:
```console
pre-commit install
```

Run manually against all files:
```console
pre-commit run --all-files
```

Hooks configured:

| Hook | What it does |
|------|-------------|
| `ruff-check --fix` | Lint and auto-fix |
| `ruff-format` | Format code |
| `check-yaml` | Validate YAML syntax |
| `check-toml` | Validate TOML syntax |
| `end-of-file-fixer` | Ensure files end with a newline |
| `trailing-whitespace` | Remove trailing whitespace |
| `check-merge-conflict` | Catch forgotten conflict markers |
| `requirements-txt-fixer` | Keep `requirements.txt` sorted |
| `pretty-format-json` | Auto-format JSON files |
| `check-illegal-windows-names` | Prevent Windows-incompatible filenames |

---

## CI

GitHub Actions runs on every push and pull request:

- **Matrix**: Python 3.12 × Python 3.13 × ubuntu-latest × windows-latest (4 jobs)
- **Steps**: checkout → set up Python → install deps → run pre-commit → run pytest

See [`.github/workflows/template.yaml`](./workflows/template.yaml).

---

## Versioning

Versions are derived automatically from git tags by `setuptools-scm` — no manual version file editing needed.

To release a new version:
```console
git tag v1.0.0
git push origin v1.0.0
```

