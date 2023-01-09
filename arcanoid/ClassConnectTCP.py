import socket
from threading import Thread
import time
import json #временное решение (надо придумать протокол)

counter = 2

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.accept_code = 123456
        self.max_attempt = 10
        print("Соединение...")
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.sock.connect((self.ip, self.port))
            #self.connect = Telnet(self.ip, self.port);
        except TimeoutError:
            print("Время ожидания подключения истекло")
        except Exception:
            print("Непредвиденная ошибка")
        else:
            print("Соединение установлено")
            if(self.checkConnect()):
                print("Код получен!")
        
    def checkConnect(self):
        for attempt in range(self.max_attempt):
            print("Попытка ", attempt)
            self.sendData({'-code': self.accept_code})
            if(self.recvData().get('-code') == self.accept_code):
                return True
        return False


    def sendData(self, data):
        self.sock.send(json.dumps(data).encode('utf-8'))

    def recvData(self):
        return json.loads(self.sock.recv(10240).decode('utf-8'))

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.accept_code = 123456
        self.max_clients = 1
        self.clients = set()

    def sendData(self, data, address = False):
        if not address:
            for address in self.clients:
                self.sock.sendto(json.dumps(data).encode('utf-8'), address)
        else:
            self.sock.sendto(json.dumps(data).encode('utf-8'), address)

    def send_accept(self, address):
        self.sendData({'-code' : self.accept_code}, address)
        self.clients.add(address)

    def recvData(self):
        data , address = self.sock.recvfrom(1024)
        data = json.loads(data.decode('utf-8'))     #временно
        
        if isinstance(data, dict) and data.get('-code') == self.accept_code:
            print(data)
            print(self.clients)
            self.send_accept(address)
        elif address in self.clients:
            return data
        #if data[0]=="-code-":
        #    if len(self.clients) < self.max_clients or address in self.clients:
        #        self.send_accept(address)
        

    #def recvData(self):
    #    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #        sock.bind((self.ip, self.port))
    #        sock.listen()
    #        conn, addr = sock.accept()
    #        with conn:
    #            while True:
    #                data = conn.recv(1024)
    #                if not data:
    #                    break
    #                print(data)
    #                conn.sendall(data)
    #                global counter
    #                counter+=1
    #                print(counter)


if __name__ == '__main__':
    #test = Server('', 8888)
    ##test.recvData()
    #p1 = Thread(target = test.recvData, daemon = True)
    #p2 = Thread(target = HelloWorld, args = ('Masha',), daemon = True)
    #p1.start()
    #p2.start()
    #print("Hello Server!")
    #p2.join()
    #p1.join()
    type = input('type')
    if(type == '1'):
        test = Server('192.168.1.104',8888)
        while 1:
            print(test.recvData())
    else:
        test = Client('192.168.1.104',8888)
        #test.checkConnect()
        while 1:
            data = input()
            data_list = list()
            data_list.append(data)
            test.sendData(data_list)
    