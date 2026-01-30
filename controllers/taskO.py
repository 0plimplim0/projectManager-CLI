from utils import utils

def getData(data):
    match data['action']:
        case 'add':
            if not data['name']:
                print('Invalid name.')
                return
            addTask(data['active_proj_id'] ,data['name'])
        case 'list':
            listTasks(data['active_proj_id'])
        case 'done':
            doneTask(data['id'])

def addTask(proj_id, name):
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('insert into tasks(project_id, title) values(?, ?)', (proj_id, name))
    conn.commit()
    print(f'Task added: {name}')

def listTasks(proj_id):
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('select * from tasks where project_id = ? order by status desc', (proj_id,))
    tasks = cursor.fetchall()
    if not tasks:
        print('This project has no tasks.')
        return
    index = 1
    for task in tasks:
        print(f'{index} id({task[0]}) - {task[2]} ({task[3]})')
        index += 1

def doneTask(id):
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('select * from tasks where id = ?', (id,))
    task = cursor.fetchone()
    if not task:
        print('There is no task with that ID.')
        return
    cursor.execute('update tasks set status = ? where id = ?', ('done', id))
    conn.commit()
    print('Task marked as done.')