__author__ = '0918901'
import random

print("---------------------------------------------------------------")
#Naam Spel
print("Kaasrenners")
print("---------------------------------------------------------------")

#declaratie Kaasrenners
def KAASRENNERS():
    #Spel naam
    print("Digitale Tegenstander")
    print("---------------------------------------------------------------")
    #spel uitleg
    print("Speluitleg")
    print("- Het doel is om zo snel mogelijk al je pionnen bij \n  de markt te brengen.")
    print("- Leg het spelbord in het midden van de speelruimte\n  zodat iedereen er goed bij kan.")
    print("- Elke speler krijgt 4 pionnen van dezelfde kleur.")
    print("- Zolang de speler minimaal 1 pion op het veld heeft \n  gooit de speler met 2 dobbelstenen.")
    print("- Als de speler geen pionnen op het veld heeft, gooit \n  de speler met 1 dobbelsteen.")
    print("- Omdat je tegenstander niet zelf de pionnen kan bewegen \n  is het handig als een van de andere spelers \n  de pionnen bewegen.")
    print("- De dobbelstenen voor de digitale tegenstander wordt \n  digitaal gegooid.")
    print("---------------------------------------------------------------")

    #Mogelijke keuzes dobbelstenen
    comp_ds2    = random.randint(1,6)
    comp_ds1    = random.randint(1,6)
    comp_ds     = comp_ds1 + comp_ds2

    #Digitale Tegenstander
    while True:
        #Tekst die aangeeft wie er aan de beurt is
        print("Computer")
        print ("de computer gebruikt 1 dobbelsteen")
        #Dobbelsteen uitslag computer
        print ("de computer heeft",comp_ds1,"gegooid.")
        print("---------------------------------------------------------------")
        # Detect uitslag dobbelsteen speler1 is 1
        if comp_ds1 == '1':
            comp_stappen = 1
            break
        #Detect uitslag dobbelsteen speler1 is 2
        elif comp_ds1 == '2':
            comp_stappen = 2
            break
        #Detect uitslag dobbelsteen speler1 is 3
        elif comp_ds1 == '3':
            comp_stappen = 3
            break
        #Detect uitslag dobbelsteen speler1 is 4
        elif comp_ds1 == '4':
            comp_stappen = 4
            break
        #Detect uitslag dobbelsteen speler1 is 5
        elif comp_ds1 == '5':
            comp_stappen = 5
            break
        #Detect uitslag dobbelsteen speler1 is 6
        elif comp_ds1 == '6':
            comp_stappen = 6
            break
        else:
            break

        #Tekst die aangeeft wie er aan de beurt is
    while True:
        print("Computer")
        print ("de computer gebruikt 2 dobbelstenen")
        #Dobbelstenen uitslag computer
        print ("de computer heeft",comp_ds1,"en",comp_ds2,"gegooid","dus totaal.",comp_ds)
        print("---------------------------------------------------------------")

        #Detect uitslag dobbelsteen2 computer is 1
        if comp_ds2 == '1':
            comp_stapen2 = 1
            break
        #Detect uitslag dobbelsteen2 computer is 2
        elif comp_ds2 == '2':
            comp_stappen2 = 2
            break
        #Detect uitslag dobbelsteen2 computer is 3
        elif comp_ds2 == '3':
            comp_stappen2 = 3
            break
        #Detect uitslag dobbelsteen2 computer is 4
        elif comp_ds2 == '4':
            comp_stappen2 = 4
            break
        #Detect uitslag dobbelsteen2 computer is 5
        elif comp_ds2 == '5':
            comp_stappen2 = 5
            break
        #Detect uitslag dobbelsteen2 computer is 6
        elif comp_ds2 == '6':
            comp_stappen2 = 6
            break
        else:
            break

    #Speler 1
    #Zolang bovenstaande klopt wordt het onderstaande wordt uitgevoerd
    while True:
        #Tekst die aangeeft wie er aan de beurt is
        print("Speler 1")
        #Invoer dobbelsteen Speler 1
        print("Hoeveel heb je gegooid?")
        speler1_ds1 = int(input("ik heb:"))
        print ("de Speler 1 heeft",speler1_ds1,"gegooid.")
        print ("---------------------------------------------------------------")

        #Detect uitslag dobbelsteen speler1 is 1
        if speler1_ds1 == '1':
            sp1_stappen = 1
            break
        #Detect uitslag dobbelsteen speler1 is 2
        elif speler1_ds1 == '2':
            sp1_stappen = 2
            break
        #Detect uitslag dobbelsteen speler1 is 3
        elif speler1_ds1 == '3':
            sp1_stappen = 3
            break
        #Detect uitslag dobbelsteen speler1 is 4
        elif speler1_ds1 == '4':
            sp1_stappen = 4
            break
        #Detect uitslag dobbelsteen speler1 is 5
        elif speler1_ds1 == '5':
            sp1_stappen = 5
            break
        #Detect uitslag dobbelsteen speler1 is 6
        elif speler1_ds1 == '6':
            sp1_stappen = 6
            break
        else:
            break

    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        print("---------------------------------------------------------------")
        #Tekst met bedankt voor het spelen
        print("Dankjewel voor het spelen van kaasrenners!")
        #Wachten op enter om opnieuw te beginnen
        answer = input("Nog een potje? Druk op enter")
        print("---------------------------------------------------------------")
        #Terug naar het begin
        return KAASRENNERS()
#einde declaratie RPS
KAASRENNERS()