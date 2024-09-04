string = str(input("enter your own word"))
char = str(input("enter your character that is in the word"))
i = 0
count = 0
while(i<len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("the total number of times ", char, " has occured is ", count)