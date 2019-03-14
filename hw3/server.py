from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    name = connectionSocket.recv(1024).decode()
    resp = 'Hi, ' + name + '. How are you?'
    connectionSocket.send(resp.encode())
    connectionSocket.close()