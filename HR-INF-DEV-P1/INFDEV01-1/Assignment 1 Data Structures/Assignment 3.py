__author__ = '0918901'
print("---------------------------------------------------------------")
#Naam opdracht
print("Assignment 3 Exercise 1 [Add Node]")
print("---------------------------------------------------------------")

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
    while


l = Node

print("Type nummer voor aantal stappen")
number = int(input("="))

def length(l):
    if l.isEmpty:
        return 0
    else:
        return length(l.Tail) + number


print("Oude lijst")
print (length(Node(1,Empty)))
print (length(Node(1,Node(2,Empty))))
print (length(Node(1,Node(2,Node(3,Empty)))))

print("---------------------------------------------------------------")

print("Nieuwe lijst")
print (length(Node(1,Empty)))
print (length(Node(1,Node(2,Empty))))
print (length(Node(1,Node(2,Node(3,Empty)))))

print("Type nummer voor nieuw aantal stappen")
number2 = int(input("="))

print("Toegevoegd")
print (length(Node(1,Node(2,Node(3,Node(4,Empty))))))
print (length(Node(1,Node(2,Node(3,Node(4,Node(5,Empty)))))))
print (length(Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Empty))))))))
print("---------------------------------------------------------------")

l = Node(1,Node(2,Node(3,Empty)))

print(length(l))
