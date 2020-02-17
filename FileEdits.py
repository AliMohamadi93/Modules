with open("Arsenal.txt","r") as teams:
    temp = []
    for x in range(5):
        if x == 0:
            teams.readline()
        else:
            temp.append(teams.readline())

with open("Arsenal.txt","w") as teams:
    teams.write("This is a new line \n")
    for x in range(len(temp)):
        teams.write(temp[x])


with open("Arsenal.txt","r") as teams:
    for x in range(5):
        print("line %d: " %(x+1), teams.readline())