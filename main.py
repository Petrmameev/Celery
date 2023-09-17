import datetime
from tasks import cpu_bound

def main():
    a_task = cpu_bound.delay(1, 2)
    b_task = cpu_bound.delay(4, 8)
    c_task = cpu_bound.delay(8, 1)
    d_task = cpu_bound.delay(10, 5)
    print(a_task, b_task, c_task, d_task)
    a = a_task.get()
    b = b_task.get()
    c = c_task.get()
    d = d_task.get()
    print(a, b, c, d)

start = datetime.datetime.now()
main()
print(datetime.datetime.now() - start)