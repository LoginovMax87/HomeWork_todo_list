import json
import os

from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f'Задача "{title}" добавлена')

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная')
                return
        print(f'Задача "{title}" не найдена')

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return

        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([vars(task) for task in self.tasks], f, ensure_ascii=False, indent=4)
        print("Данные сохранены")

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task(item['title'], item['is_done']) for item in data]