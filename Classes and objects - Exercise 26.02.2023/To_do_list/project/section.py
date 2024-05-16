from typing import List
from project_TO_DO_LIST.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            a_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"
        a_task.completed = True
        return f"Completed task {a_task}"

    def clean_section(self):
        tasks_left = list(filter(lambda t: not t.completed, self.tasks))
        finished = len(self.tasks) - len(tasks_left)
        self.tasks = tasks_left
        return f"Cleared {finished} tasks."

    def view_section(self):
        all_tasks = '\n'.join(tsk.details() for tsk in self.tasks)
        return f"Section {self.name}:\n{all_tasks}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())