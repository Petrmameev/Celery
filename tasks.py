import celery
import time


app = celery.Celery(
    broker='redis://127.0.0.1:6379/1',
    backend='redis://127.0.0.1:6379/2'
)


@app.task
def cpu_bound(a, b):
    time.sleep(1)
    return a + b