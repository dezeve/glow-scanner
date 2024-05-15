import socket

def scanPort(selectedTarget, port):
    try:
        selectedSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        selectedSocket.settimeout(1)
        result = selectedSocket.connect_ex((selectedTarget, port))
        if result == 0:
            print(f"Port {port} is open")
    except socket.error as err:
        print(f"Error checking port {port}: {err}")
    finally:
        selectedSocket.close()

def quickScan(selectedTarget):
    for port in range(1, 1025):
        scanPort(selectedTarget, port)
    print("\nQuick Scan Completed")

def fullScan(selectedTarget):
    for port in range(1, 65536):
        scanPort(selectedTarget, port)
    print("\nFull Scan Completed")
 
def customScan(selectedTarget, startPort, endPort):
	for port in range(startPort, endPort):
		scanPort(selectedTarget, port)
	print("\nCustom Scan Completed")

