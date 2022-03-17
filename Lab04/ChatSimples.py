import socket  #importa modulo socket
  
contatos = {
    "guilherme":"172.16.18.39",
    "bruno":"172.16.19.60",
    "gusta":"172.16.18.36",
    "vitu":"172.16.18.40"
}

PORTA_destino = 14287
TEMP = "> Vitu De Marqui: "

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    MENSAGEM = input("Mensagem: ")

    if MENSAGEM.upper() == "QUIT":
        exit()
        
    IP_destino = input("Destino: ").lower()
    while (IP_destino not in contatos):
        IP_destino = input("Digite um Destino VALIDO: ").lower()
    print()

    sock.sendto((TEMP+MENSAGEM).encode('UTF-8'), (contatos[IP_destino], PORTA_destino))
