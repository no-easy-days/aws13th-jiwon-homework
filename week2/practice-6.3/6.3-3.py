class TodoList:
    def __init__(self):
        self.todo = list()

    def add_task(self, task):
        self.todo.append(task)

    def complete_task(self, task):
        self.todo.remove(task)

    def show_tasks(self):
        print(self.todo)



my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")
my_todo.show_tasks()
# 출력:
# 1. Python 공부
# 2. Git 연습

my_todo.complete_task("Python 공부")
my_todo.show_tasks()
# 출력:
# 1. Git 연습