class Task:
    def __init__(self, description, name):
        self.description = description
        self.name = name
        self.completed = False

    def is_completed(self):
        return self.completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        completed = "completada" if self.completed else "incompleta"
        return f"{self.name}: {self.description} ({completed})"
    
    def __eq__(self, other):
        return self.name == other.name and self.description == other.description


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        
    def get_task(self, name):
        tasks_by_name = [task for task in self.tasks if task.name == name]
        if tasks_by_name:
            return tasks_by_name[0]
        else:
            return None

    def remove_task(self, task_name):
        task = self.get_task(task_name)
        self.tasks.remove(task)

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.is_completed()]
    
    def remove_all_tasks(self):
        self.tasks = []

    def mark_task_completed(self, task):
        task.mark_completed()

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.is_completed()]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_completed()]

    def get_all_tasks(self):
        return self.tasks

    def __str__(self):
        return "\n".join(["* " + str(task) for task in self.tasks])
