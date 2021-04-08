def reset():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    a1 = ""
    a2 = ""
    a3 = ""
    b1 = ""
    b2 = ""
    b3 = ""
    c1 = ""
    c2 = ""
    c3 = ""
def showBoard(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    space = " | "
    print(a3 + space + b3 + space + c3)
    print(a2 + space + b2 + space + c2)
    print(a1 + space + b1 + space + c1)
reset()
while (a1==a2==a3):






    showBoard(a1, a2, a3, b1, b2, b3, c1, c2, c3)
