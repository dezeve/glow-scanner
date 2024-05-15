import utils.menu
import utils.input
import utils.scanner

def main():
	utils.menu.getMenu()
	showCommandMenu = False
	doExit = False
	while True:
		if doExit:
			exit()
		if showCommandMenu:
			utils.menu.getCommandMenu()
		showCommandMenu = True
		selectedCommand = utils.input.getCommand()
		if selectedCommand == 1:
			selectedTarget = utils.input.getTarget()
			print(f"\nScanning ports 1 to 1024 for target {selectedTarget}\n")
			utils.scanner.quickScan(selectedTarget)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 2:
			selectedTarget = utils.input.getTarget()
			print(f"\nScanning ports 1 to 65535 for target {selectedTarget}\n")
			utils.scanner.fullScan(selectedTarget)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 3:
			selectedTarget = utils.input.getTarget()
			selectedPorts = utils.input.getPorts()
			startPort = selectedPorts[0]
			endPort = selectedPorts[1]
			print(f"\nScanning ports {startPort} to {endPort} for target {selectedTarget}\n")
			utils.scanner.customScan(selectedTarget, startPort, endPort)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 4:
			exit()

if __name__ == "__main__":
	main()
