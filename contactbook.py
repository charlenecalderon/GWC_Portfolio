
myCont={"EMERGENCY":"911","MOM":"(909)111-1111","POLICE STATION":"(888)888-8888"}

addContact = True
addNumber = True
addAddress = True

while addContact == True:
    print("Would you like to add a contact?")
    answer = input().lower()
    if(answer == "yes"):
        lit=[]
        print("What is the name for your new contact?")
        name = input().lower()
        
    elif(answer == "no"):
        addContact = False
    else:
        print("Please enter Yes or no")

while addAddress == True:
    print("Would you like to add an address?")
    answer2 = input().lower()
    if(answer2 == "yes"):
        print("What is the address?")
        address = input().lower()
        lit.append(address)
    elif(answer2 == "no"):
        addAddress = False
    else:
        print("Please enter Yes or No")

while addNumber == True:
    print("Would you like to enter a phone number?")
    answer3 = input().lower()
    if(answer3 == "yes"):
        print("What is the phone number?")
        phone = int(input())
        lit.append(phone)
    elif(answer3 == "no"):
        addNumber = False
    else:
        print("Please enter Yes or No")
mycont[name]= lit

print("CONTACTS")
print()
for name in myCont:
    print("Name " + name)
    name = myCont[name]
    defineType = type(name)
    if( 
    
        
        
    
