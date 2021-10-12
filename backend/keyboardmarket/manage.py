#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keyboardmarket.settings')
    os.environ['PAYPAL_CLIENT_ID'] = 'ARAxND323L6wsWMUmG_xneuznOfmjlfYsjhDPccPVggbA5RAzKjmsdx14S-62mdIK84NwINvJgiTY0mI'
    os.environ['PAYPAL_CLIENT_SECRET'] = 'ECQltltKV0Y3eGhaAgD3dDt8xbwsBTuAdslA8TCXqNxSTjc856_pZ4GXNY_TiX7tuZd4z_8q0R627uvd'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
