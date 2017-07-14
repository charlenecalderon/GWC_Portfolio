#to have an empty defintion 
#myDict = {}

#to have a pre-set dictionary
myDict = {"indespensable":"absolutely necessary","boisterous":"Scandalous",
          "present":["Existing or occuring now","A gift"]}
#myDict = {}

addWords = True

while addWords == True:
    print("Would you like to add a word to the dictionary?")
    answer = input().lower()
    if(answer == "yes"):
        print("What is the word?")
        word = input().lower()
        print("What is the definition of the word?")
        definition = input().lower()
        myDict[word] = definition

    elif(answer == "no"):
         print("Your dictionary has been saved!")
         addWords = False
    else:
         print("Please enter Yes or No")

#print(myDict)
print("MY DICTIONARY")
print()
for item in myDict:
    print("word " + item)
    definition = myDict[item]
    defineType = type(definition)
    if(defineType == str):
        print("definition: " + str(myDict[item]))
    elif(defineType == list):
        for x in definition:
            print("- " + x)
    print()

