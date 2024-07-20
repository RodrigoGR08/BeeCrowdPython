#Write an algorithm that reads two floating values (x and y), which should represent the coordinates of a point in a plane. Next, determine which quadrant the point belongs, or if you are at one of the Cartesian axes or the origin (x = y = 0).

X,Y = map(float, input().split())
if X>0:
    if Y>0:
        print("Q1")
    elif Y<0:
        print("Q4")
    elif Y==0:
        print("Eixo X")
elif  X<0:
    if Y>0:
        print("Q2")
    elif Y<0:
        print("Q3")
    elif Y==0:
        print("Eixo X")
elif X==0:
    if Y==0:
        print("Origem")
    else:
        print("Eixo Y")