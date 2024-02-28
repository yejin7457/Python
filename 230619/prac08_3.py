def readFile(fileName):
    with open(fileName) as f:
        strLst = f.readlines()
    floatLst = []
    for s in strLst:
        floatLst.append(float(s))
    return floatLst

lst1 = readFile("MP09Data1.txt")
lst2 = readFile("MP09Data2.txt")
idx1 = 0
idx2 = 0
while idx1 < len(lst1) and idx2 < len(lst2):
    if lst1[idx1] >= lst2[idx2]:
        print(lst1[idx1])
        idx1 += 1
    else:
        print(lst2[idx2])
        idx2 += 1

while idx1 < len(lst1):
    print(lst1[idx1])
    idx1 += 1

while idx2 < len(lst2):
    print(lst2[idx2])
    idx2 += 1


#print(lst1)
#print(lst2)