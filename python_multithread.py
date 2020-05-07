import threading 
 
"""
create a global variable
""" 
x = 0
  
def increment():
    
    """
    the global variable x is
    recognized here,and increased by 1
    """   
    global x 
    x += 1
  
def thread_task(lock): 
    """
    a for loop is created where the iterator, usually i, is
    not acknowledged for use which is shown by _
    
    inside the for loop, a thread is locked
    increases a variable by one
    then a lock is opened on the thread
    
    """
    
    for _ in range(100000): 
        lock.acquire() 
        increment() 
        lock.release() 
  
def main_task():
    """
    the global variable x is recognized here and intialized to 0,
    a thread lock is created,
    two threads are created and passed a function with the thread lock as a parameter,
    both threads are started with .start()
    but the entire program waits for each thread to finish due to .join()
    """
    
    global x 

    x = 0
  
 
    lock = threading.Lock() 
  

    t1 = threading.Thread(target=thread_task, args=(lock,)) 
    t2 = threading.Thread(target=thread_task, args=(lock,)) 
  

    t1.start() 
    t2.start() 
  

    t1.join() 
    t2.join() 


"""
once the program is ran
main_task() is run 10 times and
each iteration returns the variable x at the end
"""  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 