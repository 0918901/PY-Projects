# coding=utf-8
__author__ = '0918901'
#declaratie RPS
def warmpup():
    print("---------------------------------------------------------------")
    #naam opdracht
    print ("Assignment 4 Exercise 1 Warmup [Deel A Fahrenheit to Celsius]")
    print("---------------------------------------------------------------")
    #vraagt voor invoer van leeftijd
    age = int(input("What's your age: "))
    #print wat er gaat gebeuren
    print ("your age in Fahrenheit to Celsius.")
    #berekening die gebruikt wordt voor celsius
    Celsius = (age - 32) * 5.0/9.0
    #print de uitslag van berekening met 2 getallen achter de comma met round()
    print("Temperature:", age, "Fahrenheit = ", (round(Celsius,2)), " C")

    print("---------------------------------------------------------------")
    #naam opdracht
    print ("Assignment 4 Exercise 1 Warmup [Deel B Celsius to Kelvin]")
    print("---------------------------------------------------------------")
    #gebruikt leeftijd om celius te bereken
    Celsius = (age - 32) * 5.0/9.0
    #geeft aan aantal graden celsius afgerond met round functie
    print ("Celsius = ",(round(Celsius)))
    #berekening om kelvin te bereken met celsius met afgerond getal met round()
    Kelvin = (round(Celsius)) + 273,15
    #print uitkomst van berekening van celsius afgerond met round() naar kelvin
    print("Temperature:", (round(Celsius)), "Celsius = ", Kelvin, " Kelvin")

    print("---------------------------------------------------------------")
    #naam opdracht
    print ("Assignment 4 Exercise 1 Warmup [Deel C Absolute Value]")
    print("---------------------------------------------------------------")
    #berekening celsius
    Celsius = 1.0 * Celsius
    #print huidig graden in celsius afgerond met behulp van round()
    print("Your value:", (round(Celsius,2)))
    #print huidige graden in celcius zonder de - ervoor met behulp van abs()
    print("absolute value:", (abs((round(Celsius,2)))))
    print("---------------------------------------------------------------")

    #Tekst met bedankt voor het testen
    print("Thanks for testing!")
    #Wachten op enter om opnieuw te beginnen
    answer = input("test again? Press enter")
    print("---------------------------------------------------------------")
    #Terug naar het begin
    return warmpup()
#einde declaratie warmup
warmpup()