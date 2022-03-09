import re
pre = 0
crnt = True

def performMath():
    global crnt
    global pre
    eq = ""
    if pre == 0:
        eq = input("Enter equation or quit to exit\n")
    else:
        eq = input(str(pre) + '\n')

    if eq == 'quit':
        print("Exit successfully")
        crnt = False
    else:
        eq = re.sub('[a-zA-Z,.():" "]','',eq)
        if pre == 0:
            pre = eval(eq)
        else:
            pre = eval(str(pre)+eq)



while crnt:
    performMath()
