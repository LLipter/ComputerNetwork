from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
name = 'LLipter'
clientSocket.send(name.encode())
resp = clientSocket.recv(1024)
print('From Server:', resp.decode())
clientSocket.close()
