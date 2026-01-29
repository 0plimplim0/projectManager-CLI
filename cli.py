from typing import Annotated
from controllers import project, task
import typer

app = typer.Typer()

@app.command()
def proj(action: str,
         proj_name: Annotated[str, typer.Option(help='Nombre del proyecto')],
         proj_id: Annotated[int, typer.Option(help='ID del proyecto')]
):
    '''
    Ejecuta una accion con el objeto "Proyecto".
    '''
    actions = ['create', 'list', 'select']
    if action not in actions:
        print('Accion inválida.')
        raise typer.Exit()
    data = {
        'action': action,
        'name': proj_name,
        'id': proj_id
    }
    project.getData(data)

@app.command()
def task(action: str,
         task_name: Annotated[str, typer.Option(help='Nombre de la tarea.')]
):
    '''
    Realiza una accion con el objeto "Tarea".
    '''
    actions = ['add', 'list']
    if action not in actions:
        print('Accion inválida.')
        raise typer.Exit()
    data = {
        'action': action,
        'name': task_name
    }
    task.getData(data)

if __name__ == '__main__':
    app()