import socket
HOST = 'localhost'
PORT = 4900

clienteCalc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pedido = input("Insira a operação que deseja realizar:")
byte_msg = pedido.encode('utf-8')

clienteCalc.sendto(byte_msg, (HOST, PORT))
modifiedMessage, serverAddress = clienteCalc.recvfrom(2048)
#print(result)
print(modifiedMessage.decode('utf-8'))
clienteCalc.close()
