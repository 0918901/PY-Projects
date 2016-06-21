__author__ = 'reube'

for i in range (0,10):
    for j in range (0,10):
        dist = (i-5) * (i-5) + (j-5) * (j-5)
        if dist < 3:
            print("#"),
        elif dist < 7:
            print("+"),
        elif dist < 10:
            print("."),
        else:
            print(" ")
    print ('\n')

