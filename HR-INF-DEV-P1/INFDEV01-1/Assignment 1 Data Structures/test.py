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

def sum (l):
    t = 0
    x = l
    while not x.isEmpty:
        t = t + x.Value
        x = x.Tail
    return t

l = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Empty))))))

print("Assignment 1 Add Nodes")
print("------------------------------------------------------------------------------------------------")

print("Huidige Lijst Tellen")
add(l,0)
print("------------------------------------------------------------------------------------------------")

print("Nieuwe Lijst Verder Tellen")
add(l,int(input("Beginnen bij =")))
print("------------------------------------------------------------------------------------------------")

print("Assignment 2 Filter Nodes")
print("------------------------------------------------------------------------------------------------")

print("Huidige Lijst")
add(l,0)
print("------------------------------------------------------------------------------------------------")

print("Maakt nieuwe lijst met even getallen")
print("------------------------------------------------------------------------------------------------")

print("Nieuwe Lijst")
filter(l,0)
print("------------------------------------------------------------------------------------------------")

print("Assignment 3 Sum Nodes")
print("------------------------------------------------------------------------------------------------")

print("Huidige Lijst")
add(l,0)
print("------------------------------------------------------------------------------------------------")

print("Alle getallen huidige lijst opgetelt")
print("------------------------------------------------------------------------------------------------")

print("Nieuwe Lijst")
print("Total: ",sum(l))
print("------------------------------------------------------------------------------------------------")
