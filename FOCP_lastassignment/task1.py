print("Stop! Who would cross the Bridge of Death \nMust answer these question three, 'ere the other side he see.\n")

name=input("What is your name? ")            #ask user to enter their name

#lower() function is used to convert name input in lowercase
a=name.lower()                         
if a=="arthur":
    print("My leige! You may pass")
    exit()                                   #terminates the program if the condition is true

quest=input("What is your quest? ")          #ask user to input their quest

#lower() function is used to convert entered quest in lowercase
b=quest.lower()
if "grail" not in b:                        #if "grail" keyword is not present in b
    print("Only those who seek Grail may pass!")
    exit()

color=input("What is your favorite color? ") #ask the user to input their favorite color

#if zeroth position of the name and color entered is same  
if name[0]==color[0]:
    print("You may pass!")
else:
    print("Incorrect! You must now face the Gorge of Eternal Peril.")