import socket
HOST = "0.0.0.0"
PORT = "5555"
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)
print(f"[*]listenig as{HOST}:{PORT}")
client_s, clent_addr = s.asccapt()
print(f"client connected {clent_addr}")
client_s.send("welcome".encode())
while True:
    cmd = input(">>> ")
    client_s.send(cmd.encode())
    if cmd.lower() == "exit":
        break
    result = client_s.recv(1024).decode()
    print(result)

client_s.close()
s.close()