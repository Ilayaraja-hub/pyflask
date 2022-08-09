from multiprocessing import Pipe,Process
import time

st=time.time()
def process1():
    time.sleep(1)
    print("Hi process 1")

def process2():
    time.sleep(1)
    print("Hi process 2")

def run():
    p1=Process(target=process1,args=())
    p2=Process(target=process2,args=())

    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    run()
    print("Time taken is ",time.time()-st)

