import threading
import time
#Basic Thread commands
t=threading.current_thread()
print("Current Thread:", t)

print("Current Thread name:", t.name)

print("Thread identifier:", t.ident)

print("is thread alive? - ", t.is_alive())

print("is thread daemon? - ", t.daemon)

t.name = "MyBest Thread"

print("Current Thread name:", t.name)


#Launching Threads
"""There are two ways to launch a new thread,
1. By passing the name if the function that should run as a separate thread, to the constructor of the thread class


th1 = threading.Thread(name='My first thread', target=func1)
th2 = threading.Thread(target=func2)
th1.start()
th2.start()


2. By Overriding the __init__() and run() methods in a subclass of Thread class
long process, ignore"""

def fun1():
    t = threading.current_thread()
    print('Starting',t.name)
    time.sleep(1)
    print('Exiting',t.name)

def fun2():
    t = threading.current_thread()
    print('Starting',t.name)
    time.sleep(1)
    print('Exiting',t.name)

def fun3():
    t = threading.current_thread()
    print('Starting',t.name)
    time.sleep(1)
    print('Exiting',t.name)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(name='My second thread', target=fun2)
t3 = threading.Thread(name='My third thread', target=fun3)

t1.start()
t2.start()
t3.start()


def squares(n):
    return n**n

def double(n):
    print(f"The double of {n} is ", 2*n)


startTime = time.time()
for i in range(1,11):
    th = threading.Thread(target=squares, args=(i,))
    th2 = threading.Thread(target=double, args=(i,))
    th.start()
    th2.start()

    th.join()
    th2.join()
endTime = time.time()

print("Time taken =", endTime-startTime)


#The above method doesn't work if we need any return value from a thread.
#It can work by overloading run method of threading class.
#Better implementation is below, by using thread pool executor.


from concurrent.futures import ThreadPoolExecutor
import requests

url1 = "https://fakerestapi.azurewebsites.net/api/v1/Books"
url2 = "https://fakerestapi.azurewebsites.net/api/v1/Authors"
url3 = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
url4 = "https://fakerestapi.azurewebsites.net/api/v1/B"

urls = [url1,url2,url3,url4]

def fetch(url):
    response = requests.get(url = url)
    print(response.status_code)  # 200? 404? 500?
    print(repr(response.text))  # the raw body — repr shows if it's empty ''
    if response.headers.get("Content-Type") == 'application/json':
        data = response.json()
    return f"data from {url}: {response.content} "

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch, urls))

print(results)