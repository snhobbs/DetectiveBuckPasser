titleColor = "\033[38;5;0m\033[48;5;243m"
clear = "\033[0m"
yellow = "\033[38;5;226m"
titleUpper = '''  ____       _            _   _             ____             _      
 |  _ \  ___| |_ ___  ___| |_(_)_   _____  | __ ) _   _  ___| | __  
 | | | |/ _ \ __/ _ \/ __| __| \ \ / / _ \ |  _ \| | | |/ __| |/ /  
 | |_| |  __/ ||  __/ (__| |_| |\ V /  __/ | |_) | |_| | (__|   <   
 |____/ \___|\__\___|\___|\__|_| \_/ \___| |____/ \__,_|\___|_|\_\  '''
titleLower = ''' ____                         
|  _ \ __ _ ___ ___  ___ _ __ 
| |_) / _` / __/ __|/ _ \ '__|
|  __/ (_| \__ \__ \  __/ |   
|_|   \__,_|___/___/\___|_|   
'''
symbols = '''
      ,   /\   ,             |=|                     .-.            
     / '-'  '-' \           /   \                   /  /            
    |    NYPD    |         /     \                 /. /             
    \    .--.    /        /       \       )       /c\/              
     |  (9th )  |        |         |       (     /'\/               
     \   '--'   /        | _______ |      )     /  /                
      '--.  .--'         | Colt 45 |     (     /  /                 
          \/             | ------- |      )   /  /                  
                         |  40 Oz  |       ( /. /                   
                         |         |       .`.'.                    
                         |         |        `'``                    
                         |         |                                
                         |;;;;;;;;;|                                
                                                                    
'''

def printScreen():
	import userInput
	columns = userInput.getTerminalSize()[0]
	
	def printTitleSect(title, cols):
		titleSplit = title.split('\n')
		titleWidth = len(titleSplit[0])
		whiteSpace = int((columns - titleWidth)/2)
		for titleLine in titleSplit:
			userInput.printToScreen(titleColor, end = '')
			userInput.printToScreen('|' + titleLine.center(columns)[1:-1] + '|')
			userInput.printToScreen(clear, end = '')
			
	printTitleSect(titleUpper, columns)
	printTitleSect(titleLower, columns)
	for line in symbols.split('\n'):
		userInput.printToScreen(line.center(columns))
	userInput.printToScreen("The developers would like to apologize right at the beginning".center(columns))
	userInput.inputUniversal('...'.center(columns))
	userInput.printToScreen("Truly and deeply".center(columns))
	userInput.inputUniversal('...'.center(columns))