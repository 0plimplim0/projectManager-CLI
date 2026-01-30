import sqlite3


def initDb():
    connection = sqlite3.connect('./data/database.sqlite')
    with open('./data/schema.sql', 'r') as schema:
        connection.executescript(schema.read())
    cursor = connection.cursor()
    cursor.execute('select * from app_state where state_key = ?', ('active_project_id',))
    current_exist = cursor.fetchone()
    if not current_exist:
        with open('./data/data.sql', 'r') as data:
            connection.executescript(data.read())
    connection.commit()
    connection.close()

def get_active_project_id():
    with sqlite3.connect('./data/database.sqlite') as conn:
        active_id = conn.execute('select state_value from app_state where state_key = ?', ('active_project_id',)).fetchone()
        active_id = int(active_id[0])
        return active_id
    
def get_conn():
    connection = sqlite3.connect('./data/database.sqlite')
    return connection