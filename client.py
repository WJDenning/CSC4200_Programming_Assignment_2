import socket
import struct

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)
HEADER_FORMAT = '!HHIBBBH'

messages = [
	(5555, PORT, 1, 0, 1, 0, b''),
	(5555, PORT, 2, 1, 0, 0, b''),
	(5555, PORT, 3, 0, 0, 1, b''),
	(5555, PORT, 4, 0, 0, 0, b'This is a payload'),
]

def create_header(src_port, dest_port, seq, ack, syn, fin, payload):
	payload_size = len(payload)
	return struct.pack(HEADER_FORMAT, src_port, dest_port, seq, ack, syn, fin, payload_size)

def start_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	print(f"Connected to server at {HOST}:{PORT}")

	for src_port, dest_port, seq, ack, syn, fin, payload in messages:
		header = create_header(src_port, dest_port, seq, ack, syn, fin, payload)
		client.sendall(header + payload)

		acknowledgement = client.recv(1024).decode()
		print(f"Server: {acknowledgement}")

	client.close()
	print("Disconnected from the server.")

start_client()
