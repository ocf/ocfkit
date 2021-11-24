import click


@click.group()
def auth(**kwargs):
    """authenticate with your OCF account"""
    pass


@auth.command()
def login(**kwargs):
    """auth to your OCF account or principal"""
    raise NotImplementedError()


@auth.command()
def logout(**kwargs):
    """delete all authentication information"""
    raise NotImplementedError()


@auth.command()
def kinit(**kwargs):
    """configure your local kinit and get a kerb ticket"""
    raise NotImplementedError()
