# Client Server Communcation
  The server and client listen and connect on the given port and ip \
  Using the python struct library, client packs a header for the server to unpack with the given (13 byte) header format \
  The server then logs the header and payload of the send message \
  The With the header information, the server then decides the appropriate response with the given Syn Ack and Fin values and sends the response to the client \
