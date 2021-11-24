import click


@click.group()
def net(**kwargs):
    """networking related utilities"""
    pass


@net.command()
def tunnel(**kwargs):
    """bring up an SSH tunnel to an OCF machine"""
    raise NotImplementedError()


@net.command()
def ping(**kwargs):
    """ping an OCF host over v4 and v6"""
    raise NotImplementedError()


@net.command()
def reachable(**kwargs):
    """check if host A is reachable from host B over v4 and v6"""
    raise NotImplementedError()
