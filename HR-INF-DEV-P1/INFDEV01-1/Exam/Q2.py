class Empty:
    def __init__(self):
        self.isEmpty = True

class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

    Empty = Empty()


def range (l, u):
    while l < u:
        l = l + 1
        if l % 2 == 0:
            print(l)


x = range(0,5)
print(x)