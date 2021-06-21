import click
from commands import base64_handler
from commands import add_secrets
from commands import remove_secrets

@click.group()
def group():
    pass

add_secrets.register_commands(group)
remove_secrets.register_commands(group)


if __name__ == '__main__':
    group()

