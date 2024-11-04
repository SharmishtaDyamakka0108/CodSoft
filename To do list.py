#Program for to do list
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\nTasks:")
    for i, task in range(tasks, start=1):
        print(f"{i}. {task}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to be marked as done")
        return


    view_tasks(tasks)
    index = int(input("Enter the task index to be marked as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()


    while True:
        display_menu()


        choice = input("Enter your choice: ")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()        






#Program for Contact Book
names = []
phone_numbers = []
num = 3


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\t,Phone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_item = input("\nEnter search item: ")

print("Search result:")

if search_item in names:
    index = names.index(search_item)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_item, phone_number))

else:
    print("Name Not Found")
