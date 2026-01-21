import typer

app = typer.Typer()

def object(obj: str = typer.Argument()):
    '''
    Ejecuta una accion con el objeto seleccionado.
    
    Objetos válidos: proj | task
    '''
    objList = ['proj', 'task']
    if obj in objList:
        print('Objeto: Válido')
    else:
        print('Objeto: Inválido')

def action(action: str):
    '''
    Ejecuta la accion seleccionada.

    Acciones permitidas: create | select | list | add | done
    '''
    actionList = ['create', 'list', 'add', 'done', 'select']
    if action in actionList:
        print('Accion: Válida')
    else:
        print('Accion: Inválida')

@app.command()
def main(obj: str, act: str, data: str = None):
    object(obj)
    action(act)

if __name__ == '__main__':
    app()