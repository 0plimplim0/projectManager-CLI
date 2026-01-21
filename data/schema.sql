create table if not exists projects(
    id int primary key autoincrement,
    title text not null,
    status text check(status in ('ongoing', 'completed', 'inactive'))
);

create table if not exists tasks(
    id int primary key autoincrement,
    project_id int,
    title text not null,
    status text check(status in ('pending', 'done')) default 'pending',
    foreign key(project_id) references projects(id)
);

create table if not exists app_state(
    state_key text primary key,
    state_value text
);