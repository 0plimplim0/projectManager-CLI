from typing import Annotated, Any
from controllers import project, task
from utils import utils
import typer

app = typer.Typer()

@app.command()
def main(object: str, action: Annotated[str, typer.Argument()] = 'list', data=typer.Argument(default=None)):
    objects = ['proj', 'task']
    actions = ['create', 'add', 'list', 'select', 'done']
    if action not in actions:
        action = 'list'
    if object not in objects:
        print(f'Objeto inválido: {object}')
        raise typer.Abort()
    match object:
        case 'proj':
            project.getData(action, data)
        case 'task':
            print(f'Objeto válido: {object}')

if __name__ == '__main__':
    # ToDo: Agregar mensaje en info.log con el status de la iniciacion
    utils.initDb()
    app()