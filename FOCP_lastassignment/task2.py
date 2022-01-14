from statistics import mean                #importing mean function from statistic module

print("Swallow Speed Analysis: Version 1.0\n")
list1=[]                                   #empty list1 is created

while True:                                #using while loop
    read=input("Enter next reading: ")     #ask the user to enter the reading

    #upper() function converts the read input into uppercase
    j=read.upper()
    if read:
        print("Reading Saved!")
        list1.append(j)                   #appends the data in list1
    else:
        if list1 == []:                   #if input is blank
            print("No readings. Nothing to do.")
            exit()                        #terminates the program if the condition is true
        break                             #breaks the loop

print("\nResult Summary\n")
a=len(list1)                              #a stores the length of list

#using ternary operator to find the number of reading/readings analyzed
print(str(a)+" Reading is analyzed" if a<=1 else str(a)+" Readings are analyzed.")

list2=[]                                 #creating an empty list2 

#iterating over list1
for i in list1:                          
    if "U"in i:
        a=i.replace("U","")              #replacing the alphabet "U" from integer in the list1
        s=float(a)                       #type casting the integers to floating point number
        list2.append(s)                  #appending the floating point number in list2
# print(list2)

list3=[]                                 #creating an empty list3

#iterating over list1
for i in list1:
    if "E"in i:                          
        b=i.replace("E","")              #replacing the alphabet "E" from integer in the list1
        y=float(b)/1.6                   #type casting the integers to floating point number and converting the value to "KPH"
        list3.append(y)                  #appending the converted floating point number in list3

#final_list is the list created by merging list2 and list3
final_list=list2+list3            

#max() function is used to find maximum speed from the final_list
my_max=max(final_list)                   #
print(f"Max Speed: {my_max:.2f} MPH, {my_max*1.6:.2f} KPH")

#min() function is used to find minimun speed from the final_list
my_min=min(final_list)
print(f"Min Speed: {my_min:.2f} MPH, {my_min*1.6:.2f} KPH")

#mean() function is used to find mean value of speed 
my_mean=mean(final_list)
print(f"Average Speed: {my_mean:.2f} MPH, {my_mean*1.6:.2f} KPH")