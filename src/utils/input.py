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
