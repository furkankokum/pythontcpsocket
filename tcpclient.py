from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Write your lowercase message: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('The server replied. ', modifiedSentence.decode())
clientSocket.close()
