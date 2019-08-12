import socket               # 導入socket模塊
import threading
import time

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

        self.client=0
        self.client_addr=0

    def sendToClient(self):
        if(self.client != 0):
            try:
                msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.client.send(msg.encode())
            except:
                pass
        
    def listen(self):
        self.sock.listen(5)
        print("\n-----server start-----")
        threading.Thread(target = self.listen_thread).start()            

    def listen_thread(self):
        while True:
            self.client, self.client_addr = self.sock.accept()
            self.client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (self.client,self.client_addr)).start()

    def listenToClient(self, client, address):
        print(address)
        size = 1024
        client.send("welcome!".encode())
        while True:
            try:
                data = client.recv(size)
                if data:
                    print(address," message:",data)
                else:
                    pass
            except:
                print('-----Client disconnected-----')
                self.client=0
                self.client_addr=0
                client.close()
                return False

def main():
    while True:
        host,port = socket.gethostname(),12345

        try:
            port = int(port)
            break
        except ValueError:
            print("-----port error-----")
            pass
 
    server=ThreadedServer(host,port)
    server.listen()
    while True:
        server.sendToClient()
        time.sleep(1)

if __name__ == '__main__':
    main()
