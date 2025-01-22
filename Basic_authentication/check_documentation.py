#!/usr/bin/env python3
import importlib
import inspect
import sys

def check_documentation(module_name):
    """Check if the routes in the given module are properly documented."""
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Inspect all functions in the module
    functions = inspect.getmembers(module, inspect.isfunction)

    for func_name, func in functions:
        # Check if function has docstring
        if not func.__doc__:
            print(f"Warning: Function '{func_name}' is missing documentation.")
        else:
            print(f"Function '{func_name}' is documented.")

    # Check if routes are correctly set up in the app (optional)
    if hasattr(module, 'app_views'):
        blueprint = module.app_views
        routes = [rule for rule in blueprint.url_map.iter_rules()]
        print(f"Found {len(routes)} routes in the blueprint.")
        for rule in routes:
            print(f"Route: {rule}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./check_documentation.py <module_name>")
        sys.exit(1)

    module_name = sys.argv[1]
    check_documentation(module_name)
