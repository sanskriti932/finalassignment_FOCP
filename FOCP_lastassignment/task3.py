import random 

print("Welcome to Popchat \nOne of our operators will be pleased to help you today.")

#names contains the list of operators
names=["Arthur","Fiona","Janice","Noah","Alyssa","Sequira"]

#my_responses contains the list of random responses
my_responses=["Hmmm", "Oh, yes, I see","Tell me more","Try Working On this System","Seek help from department in college compound"]

#my_answer contains the keyword which when entered exits the program
my_answer=["bye","exit","goodbye","thankyou"]

def my_function(email,domain="pop.ac.uk"):      #my_function function consist of parameter email and default parameter domain
    email=input("Enter your University of Popleton e-mail: ")
    if "@" in email:
        a=email.count("@")                     #counts the number of "@" in email
        if a>1:
            print("The Popleton e-mail you entered is wrong!!")
        else:
            x=email.index("@")                #x finds the position of "@" in email
            y=email[0:x]                      #y gives the position of character before "@" in email
            z=email[x:]                       #z gives the position of character after "@" in email
            if len(y)>2:                      #len(y) the length of character before "@"
                if domain in z:           
                    #capitalize() function makes the first letter of the word capital
                    print(f"Hi, {y.capitalize()}! Thankyou and Welcome to PopChat!")
                    v=random.choice(names)    #choice() function randomly selects the operator name
                    print(f"My name is {v} and it will be my pleasure to help you")

                    list1=[1,0,1,1,1,1,1,1,1,1]     #list1 contains the list combination of nine 1 and one zero
                    number=random.choice(list1)    
                    if number==0:                   #if randomly chosen number is zero
                        print("*** NETWORK ERROR ***")
                        print(f"\nThanks, {y.capitalize()}, for using PopChat. See you again soon!")
                        exit()
                    else:
                        while True:                #using while loop
                            my_input=input("-->")
                            my_change=my_input.lower()  #lower() function converts the entered input to lowercase
                            query={}               #creating an empty dictionary named query
                            
                            # following consists of list which contains tuple and 
                            # iterating over it to store as dictionary keys
                            x=[("files","library","books")]
                            for i in x:
                                for q in i:
                                    query[q]=random.choice(["The library is closed today.","The books enrollment is available on Sundays only.","Please find library timings in SSD."])

                            a=[("wifi","internet","connection")]
                            for i in a:
                                for b in i:
                                    query[b]=random.choice(["The WiFi is excellent across the campus.","The network connection is strong.","The internet password is abc$$."])

                            c=[("deadline","assignnment","tutorial")]
                            for i in c:
                                for z in i:
                                    query[z]=random.choice(["Your deadline has been extended by two days.","The assignment given should be submitted on Tuesdays.","The tutorial is available on Popleton University portal."])

                            d=[("cafeteria","food","tea")]
                            for i in d:
                                for e in i:
                                    query[e]=random.choice(["The cafe is closed today.","The food available is amazing.","The tea is very hot.","Both hot coffee and cold coffee is available."])

                            f=[("football","rugby","basketball")]
                            for i in f:
                                for g in i:
                                    query[g]=random.choice(["The selection of football team is being on room number 2.","The rugby ball is not available right now.","Play badminton instead."])

                            h=[("fees","money","balance")]
                            for i in h:
                                for j in i:
                                    query[j]=random.choice(["Your current balance can be checked by the mobile banking.","You should pay your fees by the end of this month.","The money should be handed over in form of cheque."])

                            for o in query.keys():   #using for loop to iterate over dictionary keys
                                if o in my_change:   
                                    my_values=query.get(o) #get() function to get dictionary key
                                    print(my_values)
                                    break             #breaks the loop
                            else:
                                for p in my_answer:  #using for loop
                                    if p in my_change:
                                        print(f"Thanks,{y.capitalize()}, for using PopChat. See you again soon!")
                                        exit()      #terminates the program if the condition is true
                                print(random.choice(my_responses))

                else:
                    print("The domain you entered is wrong at University of Poppleton! Please enter correctly!")
            else:
                print("Please enter at least two characters before using '@'")
    else:
        print("The email you entered is completely invalid.")

if __name__=="__main__":    # check if executed as a script
    my_function("email")    #function call