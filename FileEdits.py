with open("Arsenal.txt","r") as teams:
    temp = teams.readlines()

with open("Arsenal.txt","w") as teams:
    teams.write("This is a new line \n")
    for x in range(1,len(temp)):
        teams.write(temp[x])


with open("Arsenal.txt","r") as teams:
    for x in range(5):
        print("line %d: " %(x+1), teams.readline())