import socket
import threading

bind_ip = "192.168.60.76"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("Le serveur attend une connexion")

def thread_recevoir_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print("[*] Received: %s" %request)


client,addr = server.accept()
print("[*] Accepted connection from: %s:Sd" %(addr[0]))
thread_recevoir_client = threading.Thread(target=thread_recevoir_client,args={client,})
thread_recevoir_client.start()

while True:
    texte = input()
    client.send(str.encode(texte))