create table if not exists projects(
    id integer primary key autoincrement,
    title text not null,
    status text check(status in ('ongoing', 'completed', 'inactive')) default 'ongoing'
);

create table if not exists tasks(
    id integer primary key autoincrement,
    project_id int,
    title text not null,
    status text check(status in ('pending', 'done')) default 'pending',
    foreign key(project_id) references projects(id) on delete cascade
);

create table if not exists app_state(
    state_key text primary key,
    state_value text
);