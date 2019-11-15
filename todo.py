
pending_list = []
completed_list = []

def print_todos(pending_list, completed_list):
    pending_menu_top = """
====== Pending ======
    """
    print(pending_menu_top)
    if len(pending_list) == 0:
        print("You have nothing to do.")
    else:
        i = 0
        for todo in pending_list:
            print(f"{i}: {todo}")
            i += 1
    pending_menu_bottom = """
=====================    
    """
    print(pending_menu_bottom)
    
    completed_menu_top = """
====== Completed ======
    """
    print(completed_menu_top)

    i = 0
    for todos in completed_list:
        print(f"{i}: {todo}")
        i += 1

    completed_menu_bottom = """
=======================    
    """
    print(completed_menu_bottom)

def add_todo(lst, item):
    new_dict = {}
    new_dict[item] = 'do the thing'
    new_dict['completed'] = False
    
    lst.append(new_dict)
    

def complete_todo(todos, index):
    todos[index]['completed'] = True
    completed_todo = todos[index]
    # print(f"{completed_todo} is completed.")
    completed_list.append(completed_todo)
    
    del todos[index]

    
    # completed_list.append(completed_todo)
    
    # try:
    #     del todos[index]
    # except IndexError:
    #     print("That todo does not exist.")

def print_menu():
    message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
"""
    print(message)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number.")
    return choice
    
def main():
    # todo_list = []
    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("K. Byeeee!")
            is_running = False
        elif choice == 1:
            print_todos(pending_list, completed_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            add_todo(pending_list, new_todo)
            # print(pending_list)
        elif choice == 3:            
            index_to_delete = get_choice("Enter the index to complete: ")
            complete_todo(pending_list, index_to_delete)
            # print(completed_list)
    
        
main()
