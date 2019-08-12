import os,sys,time
import socket
import threading

class ThreadedClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self):
        try :         
            self.sock.connect((self.host,self.port))
            print("\n-----server is connecting-----")
            threading.Thread(target = self.recFromServer).start()
            print("\n-----Thread start-----")
            return 1
        except :
            print("\n-----connect error-----")
            return 0

    def recFromServer(self):
        while True:
            try:
                print ("server:",self.sock.recv(1024))
            except:
                break
    
    def sendToServer(self):
        try :
            #msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            msg=input("please type something:")
            self.sock.send(msg.encode())
            print ("send msg ok:")
            return 1
        except socket.error :
            self.sock.close()
            time.sleep(3)
            return 0
        except :
            print ('-----other error occur -----')
            time.sleep(3)
            return 1
         
def main():
    host,port = socket.gethostname(),12345
    print (host,port)    

    while True:
        user=ThreadedClient(host,port)
        while not user.connect():
            print ("-----reconnect-----")
            continue
        
        while user.sendToServer():
            time.sleep(1)
            continue
        del user
     
if __name__ == "__main__" :
    main()
