class Empty:
    def __init__(self):
        self.isEmpty = True

class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

    Empty = Empty()

def event(l,u):
    while l > u:
        print (l)
        return Empty()
    else:
        if 1 % 2 == 0:
            print (l)
            return Node(1, event(l+1,u))
        else:
            print (l)
            return  event(l+1,u)

l = event(1,5)

print (l)