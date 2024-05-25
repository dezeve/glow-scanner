import socket

def scanPort(selectedTarget, port):
    try:
        selectedSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        selectedSocket.settimeout(1)
        result = selectedSocket.connect_ex((selectedTarget, port))
        if result == 0:
            print(f"{port}\t{identifyPortService(port)}")
    except socket.error as error:
        print(f"Error: Port {port}: {error}")
    finally:
        selectedSocket.close()

def quickScan(selectedTarget):
    print("Port\tService\n----------------")
    for port in range(1, 1025):
        scanPort(selectedTarget, port)
    print("\nQuick Scan Completed")

def fullScan(selectedTarget):
    print("Port\tService\n----------------")
    for port in range(1, 65536):
        scanPort(selectedTarget, port)
    print("\nFull Scan Completed")
 
def customScan(selectedTarget, startPort, endPort):
    print("Port\tService\n----------------")
    for port in range(startPort, endPort + 1):
        scanPort(selectedTarget, port)
    print("\nCustom Scan Completed")

def identifyPortService(port):
    try: 
        return socket.getservbyport(port)
    except:
        return "Unknown"
