from typing import Annotated
from controllers import project, task
from utils import utils
import typer

app = typer.Typer()

@app.command()
def proj(action: str,
         proj_name: Annotated[str, typer.Option('--name',help='Project name.')] = None,
         proj_id: Annotated[int, typer.Option('--id',help='Project ID.')] = None
):
    actions = ['create', 'list', 'select']
    if action not in actions:
        print('Invalid action.')
        raise typer.Exit()
    data = {
        'action': action,
        'name': proj_name,
        'id': proj_id
    }
    project.getData(data)

@app.command()
def task(action: str,
         task_name: Annotated[str, typer.Option('--name',help='Task name.')] = None,
         task_id: Annotated[str, typer.Option('--id', help='Task ID.')] = None
):
    active_proj_id = utils.get_active_project_id()
    if not active_proj_id or active_proj_id < 1:
        print('No active project selected.\nUse: proj list\nThen: proj select <id>')
        raise typer.Exit()
    actions = ['add', 'list', 'done']
    if action not in actions:
        print('Invalid action.')
        raise typer.Exit()
    data = {
        'active_proj_id': active_proj_id,
        'action': action,
        'name': task_name,
        'id': task_id
    }
    task.getData(data)

if __name__ == '__main__':
    utils.initDb()
    app()