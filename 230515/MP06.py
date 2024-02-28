s = "Lorem ipsum dolor sit amet, consecteturadipiscingelit. Suspendissesagittisnisi at dapibussemper. Utquissapienvulputate, pharetra sapienvel, commododiam. Nam tinciduntnullasit ametnequeiaculis, at interdumeratultrices. Donecnecturpissagittis, malesuadadui ut, pellentesquemagna. Integer ultriciespharetra ex utsemper. Pellentesqueex orci, rhoncusvitae dolor in, vulputatevolutpatfelis. Fuscequisornarepurus."

# def findChar(cList, ch):
#     if len(cList) > 0:
#         for lst in cList:
#             if lst[0] == ch:
#                 return lst
#         return None
#     else: 
#         return None

def findChar(cList, ch):
    if len(cList) > 0:
        for lst in cList:
            if lst[0] == ch:
                return lst
    return None

def countChars(txt):
    clist = []
    txt = txt.lower()
    for ch in txt:
        lst = findChar(clist, ch)
        if lst == None:
            clist.append([ch, 1])
        else:
            lst[1] += 1
    return clist

def printList(cList):
    for lst in cList:
        print(f"문자: {lst[0]}, 횟수: {lst[1]}")

#lst = countChars("Loreml")
#printList(lst)
def main():
    lst = countChars(s)
    printList(lst)

main()