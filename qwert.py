def readFile():
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        else:
            print(line)


readFile()