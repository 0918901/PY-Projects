print("Assignment 1 Add Nodes")
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

l = Node(1, Node(2, Node(3, Empty)))

print("Huidige Lijst Tellen")
add(l,0)
print("------------------------------------------------------------------------------------------------")

print("Nieuwe Lijst Verder Tellen")
add(l,int(input("Beginnen bij =")))
print("------------------------------------------------------------------------------------------------")
