import socket

def scanPort(selectedTarget, port, content):
    try:
        selectedSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        selectedSocket.settimeout(1)
        result = selectedSocket.connect_ex((selectedTarget, port))
        if content == "all":
            if result == 0:
                print(f"{port}\t\t{identifyPortService(port)}\t\tOpen")
            else:
                print(f"{port}\t\t{identifyPortService(port)}\t\tClosed")
        else:
            if result == 0:
                print(f"{port}\t\t{identifyPortService(port)}\t\tOpen")
    except socket.error as error:
        print(f"Error: Port {port}: {error}")
    finally:
        selectedSocket.close()

def quickScan(selectedTarget, content):
    print(f"Port\t\tService\t\tStatus\n{"-" * 39}")
    for port in range(1, 1025):
        scanPort(selectedTarget, port, content)
    print("\nQuick Scan Completed")

def fullScan(selectedTarget, content):
    print(f"Port\t\tService\t\tStatus\n{"-" * 39}")
    for port in range(1, 65536):
        scanPort(selectedTarget, port, content)
    print("\nFull Scan Completed")
 
def customScan(selectedTarget, startPort, endPort, content):
    print(f"Port\t\tService\t\tStatus\n{"-" * 39}")
    for port in range(startPort, endPort + 1):
        scanPort(selectedTarget, port, content)
    print("\nCustom Scan Completed")

def identifyPortService(port):
    try: 
        return socket.getservbyport(port)
    except:
        return "Unknown"
