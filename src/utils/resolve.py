import socket

def resolveHostname(targetName):
	while True:
		try:
			targetID = socket.gethostbyname(targetName)
			return targetID
		except:
			return None
