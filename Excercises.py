file = open("Arsenal.txt", "w+")
file.write("Porto \n")
file.write("Bayern Munchen \n")
file.write("real Madrid \n")
file.write("Benfica \n")
file.write("Lyon \n")
file.seek(0)

for x in range(5):
    if x == 0 or x == 3:
        print("Line %d:" %(x+1), file.readline())
    else:
        file.readline()

(file.close)()