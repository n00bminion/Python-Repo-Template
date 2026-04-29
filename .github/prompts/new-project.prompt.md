---
description: "Set up a new Python project from this template. Renames the package, updates pyproject.toml, fixes tests, and cleans up generated files. Usage: /new-project <project-name> <package-name>"
agent: "agent"
argument-hint: "<project-name> <package-name>  e.g. my-awesome-lib my_awesome_lib"
tools: ["read_file", "replace_string_in_file", "create_file", "run_in_terminal", "file_search"]
---

You are setting up a new Python project from the PythonRepoTemplate.

The user has provided two names in their message:
- **project-name**: the distribution/PyPI name used in `pyproject.toml` (e.g. `my-awesome-lib`, typically hyphen-separated)
- **package-name**: the importable Python package name used for the `src/` folder (e.g. `my_awesome_lib`, typically underscore-separated)

If the user only provided one name, derive the other automatically:
- package-name = project-name with hyphens replaced by underscores
- project-name = package-name with underscores replaced by hyphens

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

### 5. Reinstall the package in editable mode
Run in terminal:
```
pip install -e ".[dev]"
```
This regenerates the egg-info under the correct package name and installs dev dependencies (pytest, pytest-cov).

### 6. Confirm
Report back what was changed and remind the user to:
- Commit the changes to git
- Add their actual source code under `src/<package-name>/`
- Run `pre-commit install` if they haven't yet
- Run `pytest` to verify the placeholder test passes

