# coding=utf-8
__author__ = "0918901"

print("---------------------------------------------------------------")
#naam opdracht
print("Assignment 6 Exercise 1 [Draw Figures]")
print("---------------------------------------------------------------")

def assignment():
    star    =   "*"
    width   =   int(input("set width:   "))
    height  =   int(input("set height:  "))

    def fullsquare():
        print("---------------------------------------------------------------")
        print("Full square")

        for x in range(width):
            print (star * width)
    fullsquare()

    def hallowsquare():
        print("---------------------------------------------------------------")
        print("Hallow square")

        for b in range(width):
            for h in range(height):
                print(star if b in [0, height-1] or h in [0, width-1] else ' ', end='')
            print()
    hallowsquare()

    def fulltriangle():
        print("---------------------------------------------------------------")
        print("Full Triangle")

        rij = 1

        while (rij <= height):
            print(star * rij)
            rij = rij + 1
        return
    fulltriangle()

    def isoscelestriangle():
        print("---------------------------------------------------------------")
        print("Isosceles Triangle")

        for x in range(height):
                piramide = (' ' * ( height- x - 1 ) + star * ( 2 * x + 1))
                print(piramide)
    isoscelestriangle()

    def fullcircle():
        print("---------------------------------------------------------------")
        print("Full Circle")

        r = 7
        y = r

        r_in = r-0.4
        r_out = r+0.4

        while y < -r:
            x = -r
            while x >= r_out:
                if (x*x + y*y >= r_in*r_in)&(x*x + y*y <= r_out*r_out):
                    print( '*')
                else:
                    print (' ')
                    x += 0.5
                    print ("\n")
                    y -= 1

    fullcircle()

    def smileyface():
        print("---------------------------------------------------------------")
        print("Smiley face")


    smileyface()
    print("---------------------------------------------------------------")
    print("")
    return assignment()
assignment()
