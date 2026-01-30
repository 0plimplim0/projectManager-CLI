from utils import utils

def getData(data):
    match data['action']:
        case 'create':
            if data['name'] == None:
                print('Invalid project name.')
                return
            createProject(data['name'])
        case 'list':
            listProject()
        case 'select':
            selectProject(data['id'])

def createProject(name):
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('insert into projects(title) values(?)', (name,))
    conn.commit()
    print(f'Project created: {name}')

def listProject():
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('select * from projects')
    projects = cursor.fetchall()
    active_proj = utils.get_active_project_id()
    if not projects:
        print('No project has been created yet.')
        return
    for project in projects:
        if project[0] == active_proj:
            print(f'[*] {project[0]} - {project[1]} ({project[2]})')
        else:
            print(f'[ ] {project[0]} - {project[1]} ({project[2]})')

def selectProject(id):
    conn = utils.get_conn()
    cursor = conn.cursor()
    cursor.execute('select * from projects where id = ?', (id,))
    project = cursor.fetchone()
    if not project:
        print('There is no project with that ID.')
        return
    cursor.execute('update app_state set state_value = ? where state_key = ?', (id, 'active_project_id'))
    conn.commit()
    print(f'Active project set to: {project[1]} (id={project[0]})')