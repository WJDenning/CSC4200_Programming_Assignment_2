import socket
import threading
import logging

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s - %(message)s',
	filename = 'server_logs.txt',
	filemode = 'w'
)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	logging.info(f"New connection from {addr}")

	connected = True
	while connected:
		msg = conn.recv(1024).decode()
		if not msg:
			break

		logging.info(f"Received from {addr}: {msg}")
		print(f"[{addr}] {msg}")

		acknowledgement = "Message Received"
		conn.send(acknowledgement.encode())

	conn.close()
	clients.remove(conn)
	logging.info("f{addr} disconnected.")
	print(f"[CONNECTION CLOSED] {addr} removed.")

def start():
	server.listen(5)
	print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target = handle_client, args=(conn, addr))
		thread.start()
		clients.append(conn)
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
