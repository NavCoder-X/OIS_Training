year = int(input())+1
y = str(year)

while(len(y) != len(set(y))):
    year += 1
    y = str(year)

print(y)


