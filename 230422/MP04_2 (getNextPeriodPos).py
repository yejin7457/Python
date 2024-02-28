# 방법 1
# t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."

# def getNextPeriodPos(txt, startPos):
#     if startPos >= len(txt):
#         return -1
#     return txt.find('.', startPos, len(txt))

# def getNextLine(txt, startPos):
#     if startPos >= len(txt):
#         return None
#     idx = getNextPeriodPos(txt, startPos)
#     if idx == -1:
#         return txt[startPos:]
#     else:
#         return txt[startPos:idx + 1]

# def main():
#     idx = -1
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)
#     idx = getNextPeriodPos(t, idx + 1)
#     print(idx)

#     idx = 0
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s)
#     idx += len(s)
#     s = getNextLine(t, idx)
#     print(s) 

# main()

# 방법 2
t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."

def getNextPeriodPos(txt, startPos):
#    if startPos >= len(txt):
#        return -1
    return txt.find('.', startPos, len(txt))

def getNextLine(txt, startPos):
    if startPos >= len(txt):
        return None
    idx = getNextPeriodPos(txt, startPos)
    if idx == -1:
        return txt[startPos:]
    return txt[startPos:idx + 1]

def printNextPeriodPos(idx):    
    idx = getNextPeriodPos(t, idx + 1)
    if idx == -1:
        return
    print(idx)
    printNextPeriodPos(idx)

def printNextLine(idx):
    s = getNextLine(t, idx)
    if s == None:
        return
    print(s)
    idx += len(s)
    printNextLine(idx)

def main():
    printNextPeriodPos(-1)
    printNextLine(0)

main()