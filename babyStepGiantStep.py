from ecFiniteField import Point, EllipticCurve

def babyStepGiantStep(curve, P, Q):
    if not isinstance(curve, EllipticCurve) or not isinstance(P, Point) or not isinstance(Q, Point):
        return "Please pass an EllipticCurve and two Point objects."

    N = curve.orderOfCurve()
    m = int(N**(1/2) + 1)

    i = 0
    iP = []
    while i < m:
        iP.append(i*P)
        i+=1

    j = 0
    isMatch = 0
    while j < m and isMatch == 0:
        point = Q - j*m*P
        i = 0
        while i < m and isMatch == 0:
            if point == iP[i]:
                isMatch = 1
            i+=1
        j+=1

    k = ((i-1) + (j-1)*m) % N

    return k

#### Current testing code ####
curve = EllipticCurve(5, 5, 1, 1)
P = Point(0, 1, curve)
Q = Point(4, 2, curve)

k = babyStepGiantStep(curve, P, Q)
print("Q = kP" + "\nk = " + str(k))
