# coding=utf-8
__author__ = '0918901'
#importeer zoekfunctie
import re

print("---------------------------------------------------------------")
#naam opdracht
print("Assignment 5 Exercise 2 [Passwords]")
print("---------------------------------------------------------------")

#defineer Exercise2
def Exercise2():

    #vraagt om invoer van wachtwoord
    password = input("Enter password: ")
    print("---------------------------------------------------------------")
    #controleerd of het aantel tekens minder is dan 1 dan is het onderliggende van toepassing
    if len(password) <= 1:
        #controleer of in wachtwoord a tot z of 0 tot 9 of A tot Z of speciale characters zitten zo ja het onderliggen is dan van toepassing
        if re.search('[a-z]',password) or re.search('[0-9]',password) or re.search('[A-Z]',password or re.search('.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]'),password):
            #als bovengenoemde klopt print wachtwoord sterkte
            print("Your password is: weak")
            print("---------------------------------------------------------------")
            #Tekst met bedankt voor het testen
            print("Thanks for testing!")
            #Wachten op enter om opnieuw te beginnen
            answer = input("test again? Press enter")
            print("---------------------------------------------------------------")
            #als bovenstaande klopt ga terug naar begin Exercise2
            return Exercise2()

    #controleerd of het aantel tekens meer is dan 15 zo ja,dan is het onderliggende van toepassing
    elif len(password) >= 15:
        #controleer of in wachtwoord a tot z of 0 tot 9 of A tot Z of speciale characters zitten zo ja het onderliggen is dan van toepassing
        if re.search('[a-z]',password) or re.search('[0-9]',password) or re.search('[A-Z]',password or re.search('.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]'),password):
            #als bovengenoemde klopt print wachtwoord sterkte
            print("Your password is: strong")
            print("---------------------------------------------------------------")
            #Tekst met bedankt voor het testen
            print("Thanks for testing!")
            #Wachten op enter om opnieuw te beginnen
            answer = input("test again? Press enter")
            print("---------------------------------------------------------------")
            #als bovenstaande klopt ga terug naar begin Exercise2
            return Exercise2()

    #controleerd of het aantel tekens tussen de 2 en de 14 zit zo ja,dan is het onderliggende van toepassing
    elif len(password) == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14:
        #controleer of in wachtwoord a tot z en 0 tot 9 of A tot Z of speciale characters zitten zo ja het onderliggen is dan van toepassing
        if re.search('[a-z]',password) or re.search('[0-9]',password) or re.search('[A-Z]',password or re.search('.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]'),password):
            #als bovengenoemde klopt print wachtwoord sterkte
            print("Your password is: medium")
            print("---------------------------------------------------------------")
            #Tekst met bedankt voor het testen
            print("Thanks for testing!")
            #Wachten op enter om opnieuw te beginnen
            answer = input("test again? Press enter")
            print("---------------------------------------------------------------")
            #als bovenstaande klopt ga terug naar begin Exercise2
            return Exercise2()

    #als
    else:
        #geen van boven genoemde klopt print wachtwoord incorrect, aub probeer opnieuw
        print("Password incorrect, Please try again!!")
        #open regel
        print("---------------------------------------------------------------")
        #als bovenstaande klopt ga terug naar begin Exercise2
        return Exercise2()

#sluit definitie Exercise2 af
Exercise2()