import os

task_list = []
task_index_list = [task_list.index(x) + 1 for x in task_list]


def read_file():
  global task_list
  global task_index_list
  with open("data.txt", mode="r") as file:
    x = file.readlines()
    x = [_.strip() for _ in x]
    task_list = x
    task_index_list = [task_list.index(x) + 1 for x in task_list]


def write_file():
  with open("data.txt", mode="w") as file:
    for task in task_list:
      file.write(f"{task}\n")


def view():
  read_file()
  if len(task_list) == 0:
    print("No Task")
  else:
    list = ""
    for x in task_list:
      list += f"{task_list.index(x)+1}. {x}\n"
    print(f"\n  Tasks\n{list} ")


def add(x):
  global task_list
  task_list.append(x)
  write_file()


def update(x):
  global task_list
  task_list[int(x)] = input("Enter the updated task : ")
  write_file()


def delete(x):
  global task_list
  task_list.pop(x)
  write_file()


def quit():
  global repeat
  repeat = False
  print()
  return


def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("""
    ___To Do List___

        Menu
        1. View
        2. Add 
        3. Update
        4. Delete
        5. Quit
        """)

  option = input("Enter the operation : ").lower()

  if option == "1" or option == "view":
    view()

  elif option == "2" or option == "add":
    task = input("Enter the task to be added : ")
    add(task)

  elif option == "3" or option == "update":
    view()
    task_number = int(input("Enter the task number to be updated : ")) - 1
    update(task_number)

  elif option == "4" or option == "delete":
    view()
    task_number = int(input("Enter the task number to be deleted : ")) - 1
    delete(task_number)
  elif option == "5" or option == "quit":
    quit()


repeat = True
main()

while repeat:
  ask = input("\nAgain? Y or N ").lower()
  if ask == "y" or ask == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
  elif ask == "n" or ask == "no":
    repeat = False
    print()
