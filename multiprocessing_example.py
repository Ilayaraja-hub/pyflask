from multiprocessing import Process,Pipe
import os,time
def worker(recever):
    while 1:
        msg=recever.recv()
        print(os.getpid())
        if msg=="END":
            print("end")
            break
        print("received msg : ",msg,os.getpid())
        p2=Process(target=sleep5,args={msg,})
        p2.start()
        
        
def sleep5(p):
    import time
    time.sleep(4)
    print(p,"completed",os.getpid())
if __name__=="__main__":
    print(os.getpid())
    st=time.time()
    sender,receiver=Pipe()
    p=Process(target=worker,args={receiver,})
    p.start()
    print(1,p.is_alive())
    for i in range(50):
        #print(os.getpid())
        # p1=Process(target=sleep5,args={i,})
        # p1.start()
        # sleep5(i)
        sender.send(i)
    print(2,p.is_alive())
    
    sender.send("END")
    time.sleep(5)
    print(4,p.is_alive())
    p.join()
    print(3,p.is_alive())
    print(time.time()-st)
    print("all completed")