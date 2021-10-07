from socket import *
serverPort = 11001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('192.168.43.3',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence)
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
