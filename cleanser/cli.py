import click


@click.group()
def cli():
    """Example script."""
    pass


@cli.command()
@click.argument('args', nargs=-1)
def manage(args):
    import sys
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cleanser.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', *args])