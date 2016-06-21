class Empty:
    def __init__(self):
        self.isEmpty = True
Empty = Empty()


class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail


def lenght(l):
    cnt = 0
    x = l
    while not (x.isEmpty):
        cnt = cnt + 1
        x = x.Tail
    return cnt

print(lenght(Node(10, Empty)))

