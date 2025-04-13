import socket
import logging
import struct

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER_FORMAT = '!HHIBBBH'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s - %(message)s',
	filename = 'server_logs.txt',
	filemode = 'w'
)

def parse_header(header):
	return struct.unpack(HEADER_FORMAT, header)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	logging.info(f"New connection from {addr}")

	connected = True
	while connected:

		header = conn.recv(13)
		if not header:
			break

		if len(header) < 13:
			print("Malformed header receieved")
			break

		src_port, dest_port, seq, ack, syn, fin, payload_size = parse_header(header)

		payload = conn.recv(payload_size).decode()

		header_msg = (f"Received Header:\n	Src Port: {src_port}\n	Dest Port: {dest_port}\n	Seq: {seq}\n	Ack: {ack}\n	Syn: {syn}\n	Fin: {fin}\n	Payload Size: {payload_size}")

		logging.info(header_msg)
		print(header_msg)

		logging.info(f"Received from {addr}: {payload}")
		print(f"[{addr}] {payload}")

		if syn == 1:
			acknowledgement = "Syn received - connection intiated"
		elif ack == 1:
			acknowledgement = "Ack received - message acknowledged"
		elif fin == 1:
			acknowledgement = "Fin received - connection closing"
		else:
			acknowledgement = f"Data received - payload length: {payload_size}"

		conn.send(acknowledgement.encode())

	conn.close()
	logging.info("f{addr} disconnected.")
	print(f"[CONNECTION CLOSED] {addr} removed.")

def start():
	server.listen(5)
	print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
	conn, addr = server.accept()
	with conn:
		print(f"Connected on {addr}")
		handle_client(conn, addr)
print("[STARTING] server is starting...")
start()
