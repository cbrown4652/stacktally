from typer.testing import CliRunner

from stacktally import __version__
from stacktally.cli import app

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert result.output == f"{__version__}\n"


def test_hello() -> None:
    result = runner.invoke(app, ["hello", "Chris"])
    assert result.exit_code == 0
    assert result.output == "Hello, Chris!\n"


def test_hello_shout() -> None:
    result = runner.invoke(app, ["hello", "Chris", "--shout"])
    assert result.exit_code == 0
    assert result.output == "HELLO, CHRIS!\n"
