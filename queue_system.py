import queue
import uuid

class TaskQueue:
    def __init__(self):
        self.q = queue.Queue()

    def add_task(self, x, y):
        task_id = str(uuid.uuid4())
        self.q.put((task_id, x, y))
        return task_id

    def get_task(self):
        return self.q.get()

task_queue = TaskQueue()
