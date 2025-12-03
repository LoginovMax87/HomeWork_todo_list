from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        choice = input("Введите команду (add, done, show, exit): ")

        if choice == "add":
            title = input("Введите название задачи: ")
            if title:
                manager.add_task(title)
        elif choice == "done":
            title = input("Введите название задачи: ")
            if title:
                manager.mark_task_done(title)
        elif choice == "show":
            manager.show_tasks()
        elif choice == "exit":
            manager.save_to_file()
            print("Вы вышли из программы")
            break
        else:
            print("Введите только add, done, show или exit")

if __name__ == "__main__":
    main()