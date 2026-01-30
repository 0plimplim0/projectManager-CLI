from utils import utils

def getData(data):
    match data['action']:
        case 'add':
            addTask(data['active_proj_id'] ,data['name'])
        case 'list':
            pass
        case 'done':
            pass

def addTask(proj_id, name):
    pass