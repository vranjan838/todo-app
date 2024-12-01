
FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_args,filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)

# while True:
#     user_enter = input("Type add, show, edit, complete, or exit: ")
#     user_enter = user_enter.strip()
#
#     if user_enter.startswith("add"):
#         todo = user_enter[4:]
#         todos = get_todos(FILEPATH)
#         todos.append(todo + '\n')
#
#         write_todos(todos)
#
#     elif user_enter.startswith("show"):
#         todos= get_todos(FILEPATH)
#
#         for index, item in enumerate(todos):
#             item =item.strip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#
#     elif user_enter.startswith("edit"):
#         number = int(user_enter[5:])
#         number = number-1
#
#         todos = get_todos(FILEPATH)
#
#         new_todo = input("Enter new todo: ")
#
#         todos[number] = new_todo
#
#         write_todos(todos)
#
#     elif user_enter.startswith("complete"):
#         number = int(user_enter[9:])
#
#         todos = get_todos(FILEPATH)
#
#         index = number - 1
#
#         todo_to_remove = todos[index].strip('\n')
#         todos.pop(index)
#
#         write_todos(todos)
#         message = f"{todo_to_remove} was removed from the todos!"
#         print(message)
#
#     elif user_enter.startswith("exit"):
#         break
#
#     else:
#         print("You have entered the wrong command!")
