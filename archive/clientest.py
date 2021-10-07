from socket import *
serverName = '192.168.43.3'
serverPort = 11001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(bytes(sentence,'ascii'))
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence)
clientSocket.close()
