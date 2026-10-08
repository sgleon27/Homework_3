def divisibility_2(x):
    if x % 2 == 0:
        print(x, "is divisible by 2")
    return(x)

divisibility_2(12)

def divisibility_3(x):
     if 9 < x < 100:
            y = (x //10 ) + (x % 10)
            if y % 3 == 0:
                 print(x, "is divisible by 3")
            return(y)
     else:
        if x == 3 or x == 6 or x == 9:
            print(x, "is divisible by 3")

divisibility_3(9)

def divisibility_5(x):
     if x % 10 == 5 or x % 5 == 0: 
        print(x, "is divisible by 5")
        return(x)

divisibility_5(20)

def divisibility_6(x):
    if x == 6:
        print(x, "is divisible by 6")
    elif 9 < x < 100:
        y = (x //10 ) + (x % 10)
        if x % 2 == 0 and y % 3 == 0:
            print(x, "is divisible by 6")


divisibility_6(18)