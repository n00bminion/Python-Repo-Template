---
description: "Set up a new Python project from this template. Renames the package, updates pyproject.toml, fixes tests, and cleans up generated files. Run with no arguments — project name is auto-detected from git, package name is derived automatically. Usage: /new-project [optional-package-name]"
agent: "agent"
argument-hint: "[optional-package-name]  e.g. my_awesome_lib — leave blank to auto-derive from git remote"
---

You are setting up a new Python project from the PythonRepoTemplate.

## Determine project and package names

### Auto-detect from git (preferred)
Run the following in the terminal to get the repository name from the git remote:
```
git remote get-url origin
```
Parse the final path segment of the URL and strip any `.git` suffix to get the **project-name**.
For example:
- `https://github.com/user/my-awesome-lib.git` → `my-awesome-lib`
- `git@github.com:user/my-awesome-lib.git` → `my-awesome-lib`

### Derive package-name
- **package-name** = project-name lowercased, with hyphens replaced by underscores
- e.g. `My-Awesome-Lib` → `my_awesome_lib`

### Override package-name (optional)
If the user provided a package name in their message, use that instead of the derived value.

Validate the provided package name before proceeding:
- Must contain only lowercase letters, digits, and underscores
- Must not contain hyphens, spaces, or uppercase letters
- If invalid, tell the user what is wrong and what the correct format should be, then stop and wait for them to provide a valid name. Do not proceed until a valid name is given.

Tell the user the detected project-name and the final package-name and confirm before proceeding.

## Steps to perform

### 1. Update `pyproject.toml`
- Change `name = "pkg-name"` to `name = "<project-name>"`
- Change `version_file = "src/pkg/_version.py"` to `version_file = "src/<package-name>/_version.py"`

### 2. Rename the source package directory
Run in terminal:
```
Move-Item src\pkg src\<package-name>
```

### 3. Update the placeholder test import
In `tests/test_pkg.py`, replace:
```python
import pkg
```
with:
```python
import <package-name>
```
And replace:
```python
assert pkg is not None
```
with:
```python
assert <package-name> is not None
```

### 4. Remove stale egg-info directory
Run in terminal:
```
if (Test-Path src\pkg_name.egg-info) { Remove-Item -Recurse -Force src\pkg_name.egg-info }
```

### 5. Create a virtual environment and install the package
Run in terminal:
```
python -m venv .venv
.venv\Scripts\pip install -e ".[dev]"
```
This creates a `.venv` environment, then installs the package in editable mode along with dev dependencies (pytest, pytest-cov).

### 6. Install pre-commit hooks
Run in terminal:
```
.venv\Scripts\pre-commit install
```

### 7. Remove template-only files
Now that setup is complete, delete the template README and this prompt folder so they cannot be used again:
```
Remove-Item -Force README.md
Remove-Item -Recurse -Force .github\prompts
```

### 8. Confirm
Report back what was changed and remind the user to:
- Commit the changes to git
- Add their actual source code under `src/<package-name>/`
- Run `pytest` to verify the placeholder test passes
