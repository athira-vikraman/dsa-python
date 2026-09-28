"""
Test helper: import the lesson modules by file path.

The lesson files are named `01_constant_time.py`, `02_...` and so on,
because the numbers keep them in reading order. Python cannot `import`
a module whose name starts with a digit, so we load them from their path
instead. This helper hides that detail from the tests.
"""

import importlib.util
import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
CODE_DIR = PROJECT_ROOT / "code"
EXERCISES_DIR = PROJECT_ROOT / "exercises"


def load_module(path, name=None):
    """Load a .py file as a module object, whatever it is called."""
    path = pathlib.Path(path)
    name = name or ("lesson_" + path.stem.replace("-", "_"))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_code(filename):
    """Load a file from the code/ folder, e.g. load_code('01_constant_time.py')."""
    return load_module(CODE_DIR / filename)


def load_exercise(filename):
    """Load a file from the exercises/ folder."""
    return load_module(EXERCISES_DIR / filename)


def is_implemented(func, *args, **kwargs):
    """True if a practice function does something other than `pass`.

    An unimplemented stub returns None. That lets test_practice.py SKIP
    the exercises you have not reached yet, instead of drowning you in
    failures on day one.
    """
    if func is None:
        return False
    try:
        return func(*args, **kwargs) is not None
    except Exception:
        return False
