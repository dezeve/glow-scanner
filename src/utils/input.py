def getCommand():
	try:
		selectedCommand = int(input("Enter Command: "))
		if selectedCommand not in (1, 2, 3, 4):
			raise Exception
		return selectedCommand
	except:
		print("\nError: Please Enter a Valid Command\n")
		getCommand()
