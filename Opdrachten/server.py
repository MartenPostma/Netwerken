from socket import socket, AF_INET, SOCK_DGRAM  # Importeren van Socket library voor UDP met IPv4.

server_ip = "0.0.0.0"
server_port = 1235

s = socket(AF_INET, SOCK_DGRAM) # Defineren van socket object.
s.bind((server_ip, server_port))  # Socket binden aan IP en PORT.

print()
print(f'server gestart op IP adres ({server_ip}) en poort ({server_port})')
print(f'aan het wachten op berichten.')

while True:
    data, address = s.recvfrom(1024)   # Ontvangen van bericht (in bytes) en adres van verzender.

    print()
    print(f'bericht ontvangen van {address}')
    print(f'bericht is: {data.decode("utf-8")}')

