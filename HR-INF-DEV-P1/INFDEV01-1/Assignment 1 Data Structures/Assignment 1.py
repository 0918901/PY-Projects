print("Assignment 1 Data Structures")
print("------------------------------------------------------------------------------------------------")

class Tyre:
    def __init__(self, type, model, dimension):
        self.Type       = type
        self.Model      = model
        self.Dimension  = dimension

class Wheel:
    def __init__(self, type, model, material, dimension):
        self.Type       = type
        self.Model      = model
        self.Material   = material
        self.Dimension  = dimension

class Engine:
    def __init__(self, type, model, power, speed, soundlvl):
        self.Type       = type
        self.Model      = model
        self.Power      = power
        self.Speed      = speed
        self.Soundlvl   = soundlvl

class Seat:
    def __init__(self, position, material):
        self.Position   = position
        self.Material   = material

class Light:
    def __init__(self, model, type, lumen, watt, voltage):
        self.Model      = model
        self.Type       = type
        self.Lumen      = lumen
        self.Watt       = watt
        self.Voltage    = voltage

class Cars:
    def __init__(self, brand, model, build, switch, doors):
        self.Brand      = brand
        self.Model      = model
        self.Build      = build
        self.Switch     = switch
        self.Doors      = doors

class Person:
    def __init__(self, name, gender, dateofBirth, height, carlicense):
        self.Name           = name
        self.Gender         = gender
        self.DateofBirth    = dateofBirth
        self.Height         = height
        self.Carlicense     = carlicense

class Passenger:
    def __init__(self, position, material, name, gender, dateofBirth, height, carlicense):
        self.Seat       = Seat (position, material)
        self.Person     = Person(name, gender, dateofBirth, height, carlicense)

p1 = Passenger ("FR",   "Rubber",   "BEN",  "M",    "12-02-1990",   "176",  "B")
p2 = Passenger ("FL",   "Rubber",   "ANNA", "V",    "20-03-1995",   "165",  "A")
p3 = Passenger ("BL",   "Rubber",   "GERT", "M",    "06-07-1992",   "167",  "None")

print("Information Passenger 1")
print ("Seat position:  \t", (p1.Seat.Position))
print ("Seat material:  \t", (p1.Seat.Material))
print ("Name:           \t", (p1.Person.Name))
print ("Gender:         \t", (p1.Person.Gender))
print ("Date of Birth:  \t", (p1.Person.DateofBirth))
print ("Height:         \t", (p1.Person.Height))
print ("Carlicense:     \t", (p1.Person.Carlicense))
print("------------------------------------------------------------------------------------------------")
print("Information Passenger 2")
print ("Seat position:  \t", (p2.Seat.Position))
print ("Seat material:  \t", (p2.Seat.Material))
print ("Name:           \t", (p2.Person.Name))
print ("Gender:         \t", (p2.Person.Gender))
print ("Date of Birth:  \t", (p2.Person.DateofBirth))
print ("Height:         \t", (p2.Person.Height))
print ("Carlicense:     \t", (p2.Person.Carlicense))
print("------------------------------------------------------------------------------------------------")
print("Information Passenger 3")
print ("Seat position:  \t", (p3.Seat.Position))
print ("Seat material:  \t", (p3.Seat.Material))
print ("Name:           \t", (p3.Person.Name))
print ("Gender:         \t", (p3.Person.Gender))
print ("Date of Birth:  \t", (p3.Person.DateofBirth))
print ("Height:         \t", (p3.Person.Height))
print ("Carlicense:     \t", (p3.Person.Carlicense))
print("------------------------------------------------------------------------------------------------")
