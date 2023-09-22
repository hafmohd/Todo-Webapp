FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_write, filepath=FILEPATH):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_write)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
