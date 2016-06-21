# coding=utf-8
__author__ = "0918901"
print("---------------------------------------------------------------")
#naam opdracht
print           ("Assignment 5 Exercise 3 [Cryptography]")
print("---------------------------------------------------------------")

#defineer Exercise3
def Exercise3():
    #de alphabet in een lijst gestopt
    alphabet    = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #vraagt voor invoer van tekst doormiddel van input()
    tekst       = input('Enter input: ')
    print("---------------------------------------------------------------")
    #vraagt voor invoer van getal doormiddel van int(input())
    shift       = int(input('Enter number: '))
    #maakt output aan voor uitkomst
    output      = ''
    print("---------------------------------------------------------------")

    #als letter in tekst staat "ga dan verder met onderliggende"
    for letters in tekst:
        #als letter in alphabet staat "ga dan verder met onderliggende"
        if letters in alphabet:
            #berekening "uitvoer het alphabet letter verplaatst met het aangegeven nummer [shift] en telt niet verder dan het aantal tekens in de lijst alphabet"
            output += alphabet[(alphabet.index(letters)+shift)%(len(alphabet))]
        #anders "als bovenliggende niet klopt"  is onderliggende van toepassing
        else:
            #print bericht niet goed, probeer opnieuw
            print       ("Output incorrect, please try again!!")
            print("---------------------------------------------------------------")
            #als bovenstaande klopt ga terug naar begin Exercise3
            return Exercise3()

    #geeft ingevoerde tekst en uiteindelijke uitkomt weer met de print functie
    print("Output:",tekst," => ", output)
    print("---------------------------------------------------------------")
    #Tekst met bedankt voor het testen
    print("Thanks for testing!")
    #Wachten op enter om opnieuw te beginnen
    answer = input("test again? Press enter")
    print("---------------------------------------------------------------")
    #als bovenstaande klopt ga terug naar begin Exercise3
    return Exercise3()

#einde declaratie Exercise 3
Exercise3()
