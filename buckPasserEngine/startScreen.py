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
			userInput.printToScreen('|' + titleLine.center(columns)[1:-1] + '|', color='BLACK', backColor='WHITE')
	
	printTitleSect(titleUpper, columns)
	printTitleSect(titleLower, columns)
	for line in symbols.split('\n'):
		userInput.printToScreen(line.center(columns))
	userInput.printToScreen("The developers would like to apologize right at the beginning".center(columns), color='CYAN')
	userInput.inputUniversal('...'.center(columns))
	userInput.printToScreen("Truly and deeply".center(columns), color='CYAN')
	userInput.inputUniversal('...'.center(columns))
