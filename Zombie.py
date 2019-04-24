import socket
import threading

serveurIP = "192.168.60.76"
serveurPort = 9999

def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        print(response)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serveurIP, serveurPort))

thread_recevoir = threading.Thread(target=thread_recevoir, args={client,})
thread_recevoir.start()

while True:
    texte = input()
    client.send(str.encode(texte))