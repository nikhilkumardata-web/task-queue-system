from queue_system import task_queue
import time

def worker():
    while True:
        task_id, x, y = task_queue.get_task()
        result = x + y
        print(f"Processed Task {task_id}: {x} + {y} = {result}")
        time.sleep(1)

if __name__ == "__main__":
    worker()
