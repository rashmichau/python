#current thread
# import threading
# print("current thread is :",threading.current_thread().getName())

#thread without using class
from threading import *
import time 
# def desplay():
#     for i in range(1,11):
#         print("child thread")
#         time.sleep(1)
#t=Thread(target=desplay)
#t.start()
# for i in range(1,11):
#     print("compleated")
#     time.sleep(2) 

# with multithreading
# def square(numbers):
#     for n in numbers:
#         print("square",n*n)
#         time.sleep(1)

# def cube(numbers):
#     for n in numbers:
#         print("cube",n*n*n)
# begintime=time.time()
# numbers=[6,4,8,7,9,2]
# t1=Thread(target=square,args=(numbers,))
# t2=Thread(target=cube,args=(numbers,))
# t1.start()
# t2.start()
# print("threads available",active_count())
# l=enumerate()
# print(l)
# t1.join()
# t2.join() 

# print("completed")
# print("The total time taken:",time.time()-begintime)  
# print(t1.ident) 
# print(t2.ident)
# print("threads available",active_count())


# Synchronization
# l=Lock()
# def wish(name):
#     l.acquire()
#     for i in range(1,5):
#         print("Good evening",end="")
#         time.sleep(2)
#         print(name)
#     l.release()

# t1=Thread(target=wish,args=("Raam",))
# t2=Thread(target=wish,args=("krishna",))
# t3=Thread(target=wish,args=("shivay",))
# t1.start()
# t2.start()
# t3.start()

#Synchronization with the use of RLock
# l=RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     l.release()
#     return result
# def results(n):
#     print("the factorial of",n,"is",factorial(n))
# t1=Thread(target=results,args=(5,))
# t2=Thread(target=results,args=(9,))
# t1.start()
# t2.start()

#synchronization by use of Semaphore
s=Semaphore(3)
def wish(name):
    s.acquire()
    for i in range(1,11):
        print("good evening :",name)
        time.sleep(1)
        #print(name)
    s.release()
t1=Thread(target=wish,args=("raam",))
t2=Thread(target=wish,args=("radhey",))
t3=Thread(target=wish,args=("krishna",))
t1.start()
t2.start()
t3.start()