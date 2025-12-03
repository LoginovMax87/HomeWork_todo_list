class Task:
    def __init__(self, title, is_done=False):
        self.title = title
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"{self.title} - {status}"