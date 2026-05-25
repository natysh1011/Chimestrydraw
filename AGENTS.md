# Repository Guidelines

## Project Structure & Module Organization

ChemCanvas is a Python 3/PyQt5 desktop application. Core code lives in `chemcanvas/`; `main.py` starts the GUI, drawing behavior is split across `paper.py`, `tools.py`, `atom.py`, and `bond.py`, and format handlers follow `fileformat_*.py`. Static chemistry data and templates live in `chemcanvas/periodic_table.csv` and `chemcanvas/templates/`.

Tests are in `tests/` and use standard-library `unittest`. Qt assets are in `data/`, including `mainwindow.ui` and `resources.qrc`. Platform packaging lives in `Windows/`, `AppImage/`, `debian/`, `snapcraft.yaml`, and `io.github.ksharindam.chemcanvas.yaml`.

## Build, Test, and Development Commands

- `pyrcc5 -o chemcanvas/resources_rc.py data/resources.qrc`: regenerate Qt resource bindings after editing `data/resources.qrc` or referenced assets.
- `pyuic5 -o chemcanvas/ui_mainwindow.py data/mainwindow.ui`: regenerate the main window Python UI after editing Qt Designer files.
- `python3 -m chemcanvas.main`: run the application from the source tree.
- `python3 -m pip install --no-build-isolation .`: install locally; PyQt5 and pyqt5-dev-tools must already be available.
- `python3 -m unittest discover -s tests`: run the current automated test suite.
- `python3 -m compileall chemcanvas`: run a quick syntax sanity check over application modules.

## Coding Style & Naming Conventions

Use standard Python style with 4-space indentation. Keep module names lowercase with underscores, matching `fileformat_smiles.py` and `template_manager.py`. Prefer explicit class and method names that reflect chemistry and drawing concepts. No formatter or linter is configured, so match nearby style.

Do not hand-edit generated files. Regenerate `chemcanvas/resources_rc.py` from `data/resources.qrc` and `chemcanvas/ui_mainwindow.py` from `data/mainwindow.ui`.

## Testing Guidelines

Add focused `unittest` cases under `tests/` using `test_*.py` filenames and descriptive method names such as `test_preserves_existing_pythonpath`. GUI-adjacent tests should set `QT_QPA_PLATFORM=offscreen` where needed.

For pure logic changes, run `python3 -m unittest discover -s tests` and `python3 -m compileall chemcanvas`. For GUI, drawing, file-format, or packaging changes, also smoke test startup and affected workflows, such as opening/saving SMILES, Molfile, SVG, or CDXML files.

## Commit & Pull Request Guidelines

Recent history uses short, imperative subjects, often scoped by feature or fix, for example `add p-orbital in shapetool` and `fix #12 : bond touched atom text on top side`. Keep commits narrow and mention issue numbers when applicable.

Pull requests should describe the user-visible change, list automated and manual checks performed, note affected platforms, and include screenshots for visible UI or drawing behavior changes.

## Security & Configuration Tips

Do not commit IDE files, caches, build outputs, virtual environments, or platform-specific temporary artifacts. Avoid startup network calls unless optional and clearly surfaced to users.
