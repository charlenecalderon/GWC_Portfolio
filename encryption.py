

newWords = []
codeWords = []


#FUNCTION
def createCodeWords():
    codingWords = True
    while codingWords:
        print("Would you like to add a word to your code word bank?")
        answer = input()
        if(answer.upper() == "YES" or "YEAH" or "Y"):
            print("What is the REAL WORD?")
            real = input().lower()
            
            newWords.append(real)
            print("What is the CODE WORD?")
            code = input().lower()
            codeWords.append(code)
        elif(answer.upper() == ("NO" or "N" or "NO THANKS")):
            print("Your code words have been saved!!")
        else:
            print("Don't break me!")
            exit()

def encryptMessage():
    print()
    print("___________________________________")
    print()

    print("What is your message you would like to encrypt?")
    message = input().lower()
    wordList = message.split()

    codeMessage = ""
    for word in wordList:
        for realWord in wordList:
            print("checking words" + word + " and " + realWord)
        
                  
   




#RUNNING CODE
createCodeWords()
encryptMessage()


    
    
    

