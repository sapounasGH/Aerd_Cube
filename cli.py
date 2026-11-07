from stac_loader import StacLoader
import consts
import typer


class AerdCubeCLI:
    """Typer-based CLI wrapper around the loader workflow."""
    app = typer.Typer(help="Aerd Cube")

    def __init__(self):
        return


    @app.callback()
    def _cli():
        print("Welcome to  Äerd Cube")

    @app.command()
    def analyze():
        loader = StacLoader()

        query = loader.search(
            collections=[consts.DEFAULT_COLLECTION],
            bbox=consts.DEFAULT_BBOX,
            datetime=consts.DEFAULT_DATETIME
        )

        xx = loader.load(
            query=query,
            bands=consts.DEFAULT_BANDS
        )

        print(xx)

    def run(self):
        self.app()


if __name__ == "__main__":
    AerdCubeCLI().run()
