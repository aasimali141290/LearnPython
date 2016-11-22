dict = {}
for i in range(3):
    name = input("name of fruit  ")
    if name in dict:
        a=dict[name]
        dict[name] = a+1
    else:
        dict[name]=1

print(dict)
