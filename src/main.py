import utils.menu
import utils.input
import utils.scanner

def main():
	utils.menu.getMenu()
	selectedCommand = utils.input.getCommand()
	if selectedCommand is 1:
		selectedTarget = utils.input.getTarget()
		print(f"\nScanning ports 1 to 1024 for target {selectedTarget}\n")
		utils.scanner.quickScan(selectedTarget)

if __name__ == "__main__":
	main()
