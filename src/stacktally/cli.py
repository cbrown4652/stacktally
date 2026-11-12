import typer

from stacktally import __version__

app = typer.Typer(help="Service catalog and drift detection for Docker Compose")


@app.callback()
def main() -> None:
    """Service catalog and drift detection for Docker Compose"""


@app.command()
def version() -> None:
    """Print the stacktally version."""
    print(__version__)


@app.command()
def hello(name: str, shout: bool = False) -> None:
    """Print a greeting to a user."""
    response = f"Hello, {name}!"
    if shout:
        response = response.upper()
    print(response)
