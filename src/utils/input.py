from . import resolve

def getCommand():
	while True:
		try:
			selectedCommand = int(input("Enter Command: "))
			if selectedCommand not in (1, 2, 3, 4):
				raise Exception
			return selectedCommand
		except:
			print("\nError: Please Enter a Valid Command\n")

def getTarget():
	while True:
		try:
			selectedTarget = str(input("Enter Target: "))
			if any(char.isalpha() for char in selectedTarget):
				selectedTarget = resolve.resolveHostname(selectedTarget)
				if not selectedTarget:
					raise Exception
				return selectedTarget
			else:
				return selectedTarget

		except:
			print("\nError: Please Enter a Valid Target\n")

def getPorts():
	while True:
		try:
			startPort = int(input("\nPlease Enter Start Port Number: "))
			endPort = int(input("Please Enter End Port Number: "))
			if startPort <= endPort and 0 < startPort < 65534 and 1 < endPort < 65536:
				return startPort, endPort
			else:
				raise Exception
		except:
			print("\nError: Please Enter Appropriate Port Numbers\n")

