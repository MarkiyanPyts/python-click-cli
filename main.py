import click

@click.group
def mycommands():
    pass

@click.command()
@click.option('--name', prompt="Enter your name", help="the name of the user")
def hello(name):
    click.echo('Hello %s!' % name)

PRIORITIES = {
    'o': 'OPTIONAL',
    'l': 'LOW',
    'm': 'MEDIUM',
    'h': 'HIGH',
    'c': 'CRITICAL'
}

@click.command()
@click.argument('priority', type=click.Choice(PRIORITIES.keys()), default='m')
@click.argument('todofile', type=click.Path(exists=False), required=0 )
@click.option('-n', '--name', prompt="Enter the todo name", help="The name of the todo item")
@click.option('-d', '--description', prompt="Enter the todo description", help="The description of the todo item")
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else 'mytodo.txt'
    with open(filename, 'a+') as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]\n")

@click.command()
@click.argument('idx', type=int, required=1 )
def delete_todo(idx):
    with open('mytodo.txt', "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open('mytodo.txt', "w") as f:
        f.write('\n'.join(todo_list))
        f.write('\n')

@click.command()
@click.option('-p', '--priority', type=click.Choice(PRIORITIES.keys()), default='m')
@click.argument('todofile', type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else 'mytodo.txt'
    with open(filename, 'r') as f:
        todo_list = f.read().splitlines()
        
        if priority is None:
            for idx, todo in enumerate(todo_list):
                print(f"{idx}: {todo}")
        else:
            for idx, todo in enumerate(todo_list):
                if f"[Priority: {PRIORITIES[priority]}]" in todo:
                    print(f"{idx}: {todo}")

mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)


if __name__ == '__main__':
    mycommands()