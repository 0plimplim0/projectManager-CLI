from typing import Annotated
import typer

app = typer.Typer()

@app.command()
def main(object: str, action: Annotated[str, typer.Argument()] = 'list'):
    objects = ['proj', 'task']
    if object not in objects:
        print(f'Objeto inválido: {object}')
    match object:
        case 'proj':
            print(f'Objeto válido: {object}')
        case 'task':
            print(f'Objeto válido: {object}')

if __name__ == '__main__':
    app()