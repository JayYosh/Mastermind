#psuedocode
#Function that is the Mastermind Game
    #create a fuction that chooses difficulty
        #4 digits
            #change a counter that makes it 1
        #5 digits
            #change a counter that makes it 2
        #6 digits
            #change a counter that makes it 3
        #7 digits
            #change a counter that makes it 4
    #create a function that gets the randomly generated number that the number varys

def difficultyPicker():
    
    Difficulty = int(input("Choose a Difficulty: 4 Digits, 5 Digits, 6, Digits, or 7 digits. Answer with 4, 5, 6, or 7: "))
    while Difficulty not in [4,5,6,7]:
       Difficulty = int(input("Not a valid response, please answer 4, 5, 6, or 7: "))
    return Difficulty

def RandomCodeGenerator(Difficulty):
    

