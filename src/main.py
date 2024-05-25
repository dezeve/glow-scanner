
# A Note About Using This Program

# This program is provided for educational purposes only.
# It is not guaranteed to be bug-free or function as intended.
# Use it responsibly and ethically. Always obtain permission
# from the owner before scanning any system that does
# not belong to you. Scanning unauthorized systems can be
# a violation of law or security policy.

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
			content = utils.input.getContent()
			print(f"\nScanning ports 1 to 1024 for target {selectedTarget}\n")
			utils.scanner.quickScan(selectedTarget, content)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 2:
			selectedTarget = utils.input.getTarget()
			content = utils.input.getContent()
			print(f"\nScanning ports 1 to 65535 for target {selectedTarget}\n")
			utils.scanner.fullScan(selectedTarget, content)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 3:
			selectedTarget = utils.input.getTarget()
			selectedPorts = utils.input.getPorts()
			content = utils.input.getContent()
			startPort = selectedPorts[0]
			endPort = selectedPorts[1]
			print(f"\nScanning ports {startPort} to {endPort} for target {selectedTarget}\n")
			utils.scanner.customScan(selectedTarget, startPort, endPort, content)
			exitValue = utils.input.getExit()
			if exitValue:
				doExit = True
		if selectedCommand == 4:
			exit()

if __name__ == "__main__":
	main()
