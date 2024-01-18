import click


@click.group(short_help="scheme_sddi CLI.")
def scheme_sddi():
    """scheme_sddi CLI.
    """
    pass


@scheme_sddi.command()
@click.argument("name", default="scheme_sddi")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [scheme_sddi]
