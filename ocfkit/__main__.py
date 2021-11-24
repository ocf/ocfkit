import click
import ocfkit.auth
import ocfkit.config
import ocfkit.net


@click.group()
def cli():
    pass


cli.add_command(ocfkit.auth.auth, "auth")
cli.add_command(ocfkit.config.config, "config")
cli.add_command(ocfkit.net.net, "net")

if __name__ == "__main__":
    cli()
