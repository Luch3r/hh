from datetime import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
    def add_task(self, name, deadline):
        self.tasks[name] = {'deadline': datetime.strptime(deadline, '%Y-%m-%d').date(), 'done': False}
    def complete_task(self, name):
        if name in self.tasks:
            self.tasks[name]['done'] = True
    def overdue_tasks(self):
        today = datetime.now().date()
        return [name for name, info in self.tasks.items() if not info['done'] and info['deadline'] < today]
    def today_tasks(self):
        today = datetime.now().date()
        return [name for name, info in self.tasks.items() if info['deadline'] == today and not info['done']]

scheduler = TaskScheduler()
scheduler.add_task("Купить молоко", "2026-02-14")
scheduler.add_task("Сдать проект", "2026-02-13")
scheduler.complete_task("Сдать проект")
print(scheduler.today_tasks())
print(scheduler.overdue_tasks())
