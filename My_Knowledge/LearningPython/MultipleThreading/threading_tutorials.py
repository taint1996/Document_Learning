import threading
import time

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 second \
           \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))

start = time.time()
for i in range(5):
    print('interation {} has started'.format(i))
    sleeper(1, i)

end = time.time()

print('Time taken: {}'.format(end - start))
