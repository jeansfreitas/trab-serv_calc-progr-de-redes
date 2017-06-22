import socket
from math import sqrt

def calcSoma(a, b):
    c = float(a) + float(b)
    return str(c)

def calcRaiz(a):
    return str(sqrt(float(a)))

def operCalc(operacao):
    lOperacao = operacao.decode('utf-8').split()
#    print(modifiedMessage.decode('utf-8'))
    print(lOperacao[0])
    if lOperacao[0].upper() == 'SOMA':
        if lOperacao[1].isnumeric() and lOperacao[2].isnumeric():
            return calcSoma(lOperacao[1], lOperacao[2])
        else:
            sErro = 'Os valores passados não são numéricos.'
            return sErro
    elif lOperacao[0].upper() == 'RAIZ':
        if lOperacao[1].isnumeric():
            return calcRaiz(lOperacao[1])
        else:
            sErro = 'Os valores passados não são numéricos.'
            return sErro
    else:
        sErro = 'A operação passada não é válida.'
        return sErro



HOST = 'localhost'
PORT = 4900

serverCalc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverCalc.bind((HOST, PORT))
serverCalc.listen()

clienteCalc, addr = serverCalc.accept()

while True:
    pedido = clienteCalc.recv(2048)
    print('Conexão iniciada por: ', clientAddress)
    result = operCalc(message)
    print("\n", result)
    serverCalc.sendto(result.encode(), clientAddress)
