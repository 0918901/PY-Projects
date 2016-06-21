##input userlist
class Empty:
    def __init__(self):
        self.isEmpty = True
Empty = Empty()

class Node:
    def __init__(self):
        self.isEmpty    = False
        self.Value      = value
        self.Tail       = tail


l = Empty
count = int(input("how many numbers?"))
for i in range(0,count):
    v = int(input("insert new number"))
    l = Node(v,1)
