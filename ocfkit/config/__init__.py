import click


@click.group()
def config(**kwargs):
    """configure your machine with OCF services"""
    pass


@config.command()
def apt(**kwargs):
    """toggle using ocf mirrors on your machine"""
    raise NotImplementedError()


@config.command()
def ssh(**kwargs):
    """add OCF hosts to your ~/.ssh/config"""
    raise NotImplementedError()


@config.command()
def kubectl(**kwargs):
    """configure your local kubectl for the OCF cluster"""
    raise NotImplementedError()


@config.command()
def wireguard(**kwargs):
    """configure all wireguard tunnels you have permission to use"""
    raise NotImplementedError()
