# Client Server Communcation
  The server and client listen and connect on the given port and ip \
  Using the python struct library, client packs a header for the server to unpack with the given (13 byte) header format \
  The client for this project responds with a set of given messages to exemplify the various server responses \
  The server then logs the header and payload of the send message \
  The With the header information, the server then decides the appropriate response with the given Syn Ack and Fin values and sends the response to the client 

# Header Format

  Nonexistant or malformed headers cause the server to disconnect from the client\\

  | Field         | Size     | Description                               |\
  |---------------|----------|-------------------------------------------|\
  | Source Port   | 2 bytes  | Arbitrary port number from the client     |\
  | Dest Port     | 2 bytes  | Server's listening port                   |\
  | Sequence No   | 4 bytes  | Sequence number of the message            |\
  | ACK Flag      | 1 byte   | 0 or 1 – Indicates acknowledgment         |\
  | SYN Flag      | 1 byte   | 0 or 1 – Indicates connection initiation  |\
  | FIN Flag      | 1 byte   | 0 or 1 – Indicates connection termination |\
  | Payload Size  | 2 bytes  | Length of the message payload             |\

# Server Response Logic

  If SYN is 1, server responds: "SYN received – connection initiated"\
  If ACK is 1, server responds: "ACK received – message acknowledged"\
  If FIN is 1, server responds: "FIN received – connection closing"\
  Otherwise, server responds: "Data received – payload length: X"
