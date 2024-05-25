from . import resolve

def getCommand():
	while True:
		try:
			selectedCommand = int(input("Enter Command: "))
			if selectedCommand not in (1, 2, 3, 4):
				raise Exception
			return selectedCommand
		except:
			print("\nError: Command Not Valid\n")

def getTarget():
	while True:
		try:
			selectedTarget = str(input("Enter Target: "))
			if selectedTarget.lower() == "localhost":
				selectedTarget = "127.0.0.1"
			if any(char.isalpha() for char in selectedTarget):
				selectedTarget = resolve.resolveHostname(selectedTarget)
				if not selectedTarget:
					raise Exception
				return selectedTarget
			else:
				return selectedTarget

		except:
			print("\nError: Target Not Valid\n")

def getPorts():
	while True:
		try:
			startPort = int(input("\nEnter Start Port Number: "))
			endPort = int(input("Enter End Port Number: "))
			if startPort <= endPort and 0 < startPort < 65535 and 1 < endPort < 65536:
				return startPort, endPort
			else:
				raise Exception
		except:
			print("\nError: Port Numbers Not Valid\n")

def getExit():
	while True:
		try:
			exitValue = str(input("\nDo You Want to Exit (y/n): "))
			if exitValue == "y":
				return True
			if exitValue == "n":
				return False
			else:
				raise Exception
		except:
			print("\nError: Enter y or n\n")

def getContent():
	while True:
		try:
			contentValue = str(input("\nShould closed ports also be printed (y/n): "))
			if contentValue == "y":
				return "all"
			if contentValue == "n":
				return False
			else:
				raise Exception
		except:
			print("\nError: Enter y or n\n")
