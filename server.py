import socket
import time
import threading

f_recv_s = socket.socket()
f_recv_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

f_send_s = socket.socket()
f_send_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

f_recv = 2025
f_send = 2027

ip = ""

f_recv_s.bind((ip, f_recv))
f_send_s.bind((ip, f_send))

f_recv_s.listen()
f_send_s.listen()

f_recv_session, f_recv_addr = f_recv_s.accept()
f_send_session, f_send_addr = f_send_s.accept()

print(f_recv_addr)
print(f_send_addr)

s_recv_s = socket.socket()
s_recv_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s_send_s = socket.socket()
s_send_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s_recv = 2026
s_send = 2028

ip = ""

s_recv_s.bind((ip, s_recv))
s_send_s.bind((ip, s_send))

s_recv_s.listen()
s_send_s.listen()

s_recv_session, s_recv_addr = s_recv_s.accept()
s_send_session, s_send_addr = s_send_s.accept()

print(s_recv_addr)
print(s_send_addr)
def f_recv1():
  while True:
    data = f_recv_session.recv(100000000)
    time.sleep(0.2)
    f_send_session.send(data)
    
def s_recv1():
  while True:
    data = s_recv_session.recv(100000000)
    time.sleep(0.2)
    s_send_session.send(data)

x1 = threading.Thread(target=f_recv1)
x2 = threading.Thread(target=s_recv1)
x1.start()
x2.start()
