print("Assignment 2 Filter Nodes")
print("------------------------------------------------------------------------------------------------")


class Empty:
    def __init__(self):
        self.isEmpty = True
Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

def add (l, n):
    x = l
    while not l.isEmpty:
        l.Value += n
        print (l.Value)
        l = l.Tail
    return x

def filter (l, n):
    x = l
    while not l.isEmpty:
        if l.Value % 2 == 0:
            l.Value += n
            print (l.Value)
        l = l.Tail
    return x

l = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Empty))))))

print("Huidige Lijst")
add(l,0)
print("------------------------------------------------------------------------------------------------")

print("Maakt nieuwe lijst met even getallen")
print("------------------------------------------------------------------------------------------------")

print("Nieuwe Lijst")
filter(l,0)
print("------------------------------------------------------------------------------------------------")
