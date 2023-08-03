import socket
from loguru import logger

logger.add(".\logger\logger.log", format="{time} {level} {message}", level="DEBUG")



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 2234))
server.listen(4) #вроде бы кол-во соединений, но надо гуглить
clientSocket, clientAddress = server.accept() # ждем пока подключиться клиент и записываем его сообщение и адрес
data = clientSocket.recv(1024) # записываем переданное сообщение + размер сообщения в байтах
logger.info("Client Address:" + str(clientAddress))
logger.info("Client Socket:" + str(clientSocket))
HEADERS ='HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

tempContent = 'oh...baby'.encode("utf-8")
clientSocket.send(HEADERS.encode("utf-8") + tempContent)
print(dir(data))
print(data.decode("utf-8"))