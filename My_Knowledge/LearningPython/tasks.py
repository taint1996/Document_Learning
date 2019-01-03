from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost', backend='rpc://')

@app.task
def reverse(string):
  return string[::-1]
