import csv                      #importing a csv module

class Team:                     #creating a class Team
    
    #creating two empty list for country and result
    list1_country=[]
    list2_result=[]
    #setting the counter to 0 for all the points scored
    p=0
    w=0
    l=0
    d=0
    f=0
    a=0
    gd=0
    pts=0

    def __init__(self):         #initialize the attributes of class Team

        #opening the team csv file in reading mode as newfile
        with open("team.csv","r") as newfile:
            for i in newfile:
                Team.list1_country.append(i.rstrip()) #removes the "\n" from the list
            print(Team.list1_country)

        #opening the result csv file in reading mode as newfile2
        with open("result.csv","r") as newfile2:
            fileread=csv.reader(newfile2)
            for j in fileread:
                Team.list2_result.append(j)  #appends the content in list2_result list
            print(Team.list2_result)

x=Team()    #calling the class Team