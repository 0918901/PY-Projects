import math


class Empty:
    def __init__(self):
        self.isEmpty = True

class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

    Empty = Empty()

class Vector2 :
    def __init__ (self , x, y):
        self .X = x
        self .Y = y
    def Length ( self ):
        return math.sqrt ( self .X * self .X + self .Y * self .Y)
    def __neg__ ( self ):
        return Vector2 (- self .X, -self .Y)
    def __add__ (self , other ):
        return Vector2 ( self .X + other .X, self .Y + other .Y)
    def __sub__ (self , other ):
        return self + (- other );
    def __mul__ (self , k):
        return Vector2 ( self .X * k, self .Y * k)
    def __str__ ( self ):
        return "(" + str ( self .X) + "," + str ( self .Y) + ")"
    def Zero (self):
        return Vector2 (0.0 , 0.0)
    def UnitX (self):
        return Vector2 (1.0 , 0.0)
    def UnitY (self):
        return Vector2 (0.0 , 1.0)

class Station :
    def __init__ (self , p, wp , wc):
        self.Position = p
        self.WaitingPassengers = wp
        self.WaitingContainers = wc

class Train :
    def __init__ (self , p):
        self.Position = p
        self.Passengers = 0
        self.Containers = 0
    def NavigateTo (self , port ):
        self.Position = port.Position
        self.Passengers = port.WaitingPassengers
        port.WaitingPassengers = 0
        self.Containers = port.WaitingContainers
        port.WaitingContainers = 0

## EXAM QUESTION ##

class Airport :
    def __init__ (self , p,):
        self.Position = p

class Plane :
    def __init__ (self , p, f):
        self.Position = p
        self.Fuel = f
        self.Passengers = 0

    def LoadPassengers(self, n):
        self.Passengers = self.Passengers + n

    def Flyto (self , airport):
        self.Fuel = self.Fuel - (airport.Position - self.Position).Length()
        self.Position = airport.Position