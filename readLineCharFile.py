def readLineCharFile():
    a = 0
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    for line in file:
        print(line)
        words=line.split()
        for word in words:
            print(word)
            a=0
            for char in word:
                if char!=" ":
                   a=a+1
                else:
                      break
            print(a)

readLineCharFile()
