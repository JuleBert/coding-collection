import math

def FRACTRAN(Nin, f):
    N = Nin
    while True:
        [N,i] = Subroutine2(N,f)
        if i == 0:
            return(N)

def Subroutine(N,f):
    for f1 in f:
        prod = f1[0] * N / f1[1] # this is necessary because of rounding precision
        if prod == int(prod):
            return [prod,f1]
    return(N,0)

def Subroutine2(N,f):
    for f1 in f:
        prod = f1 * N
        if prod == int(prod):
            return [prod,1]
    return(N,0)

def SubtrOneFrac(a):
    # returns a - 1
    return(int(math.log(FRACTRAN((2**a)*(3),[1/6]),2)))

def AddOneFrac(a):
    return(int(math.log(FRACTRAN((2)*(3**a),[2/3]),2)))

def Frac3x1(x):
    # returns 3 * x
    return(int(math.log(FRACTRAN(3**x, [8/3]), 2)))

def MaxFrac(a,b):
    # returns max(a,b)
    return(int(math.log(FRACTRAN((2**a)*(3**b),[5/6,5/2,5/3]),5)))

def MinFrac(a,b):
    # returns min(a,b)
    return(int(math.log(FRACTRAN((2**a)*(3**b),[5/6,1/3,1/2]),5)))

def SubFrac(a,b):
    # if a > b returns a - b
    # else returns a
    return(int(math.log(FRACTRAN((2**a)*(3**b),[1/6]),2)))

def SubtrFrac(a,b):
    # returns abs(a-b)
    return(int(math.log(FRACTRAN((2**a)*(3**b),[5*7/6,5/2,5/3,1/35]),5)))

def AddFrac(a,b):
    # returns a + b
    return(int(math.log(FRACTRAN((2**a)*(3**b),[2/3]),2)))

def Add3Frac(a,b,c):
    # returns a + b + c
    return(int(math.log(FRACTRAN((2**a)*(3**b)*(5**c),[2/3,2/5]),2)))

def MultiFrac(a,b):
    # returns a * b
    return(int(math.log(FRACTRAN((2**a)*(3**b),[2/3]),2)))


def printPrimes():
    N = 2
    f = [[17,91],[78,85],[19,51],[23,38],[29,33],[77,29],[95,23],[77,19],[1,17],[11,13],[13,11],[15,14],[15,2],[55,1]]
    i3 = 0
    i4 = 0
    while i4 < 4: # this is because after 7 it takes a veeery long time
        i3 = i3 + 1
        [N, i2] = Subroutine(N, f)
        check = math.log(N, 2)
        if check == int(check):
            print(str(int(check)) + " bei Versuch: " + str(i3))
            i4 = i4 + 1


print('SubtrOneFrac(5)  : ' + str(SubtrOneFrac(5)))
print('AddOneFrac(7)    : ' + str(AddOneFrac(7)))
print('Frac3x1(7)       : ' + str(Frac3x1(7)))
print('MaxFrac(2,11)    : ' + str(MaxFrac(2, 11)))
print('MinFrac(7,10)    : ' + str(MinFrac(7, 10)))
print('SubFrac(17,5)    : ' + str(SubFrac(17, 5)))
print('SubtrFrac(7,10)  : ' + str(SubtrFrac(7, 10)))
print('AddFrac(8,17)    : ' + str(AddFrac(8, 17)))
print('Add3Frac(8,17,5) : ' + str(Add3Frac(8, 17, 5)))
print('MultiFrac(6,12)  : ' + str(MultiFrac(6, 12)))
printPrimes()
