import socket

def client(i):
    s = socket.socket()
    s.connect(('127.0.0.1',6665))
    print(f'Recv msg {s.recv(1024)} , Client {i}')
    s.close()




if __name__ == '__main__':
    for i in range(10):
      client(i)
