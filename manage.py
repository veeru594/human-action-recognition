#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # 👇 Add the actual folder where 'HumanAction' module is located
    sys.path.append(os.path.join(os.path.dirname(__file__), 'Code', 'HumanAction'))

    # 👇 Match the location of settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HumanAction.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
