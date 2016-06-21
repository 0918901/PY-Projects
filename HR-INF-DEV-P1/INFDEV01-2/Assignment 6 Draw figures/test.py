__author__ = 'reube'


star    =   "*"
width   =   10
height  =   10

for b in range(width):
    for h in range(height):
        print(star
              if b in [0, height-1]
                 or h in [0, width-1]
              else '#', end='')
    print()