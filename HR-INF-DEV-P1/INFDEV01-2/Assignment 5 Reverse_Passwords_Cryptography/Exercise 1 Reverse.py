# coding=utf-8
__author__ = '0918901'
print("---------------------------------------------------------------")
#Naam opdracht
print("Assignment 5 Exercise 1 [Reverse]")
print("---------------------------------------------------------------")

#declartie reverse
def reverse():
    #vraagt voor invoer voorbeeld
    excercise = input('Example input:  ')
    print("---------------------------------------------------------------")
    #print invoer voorbeeld achterstevoren uit met behulp van [::-1]
    print("Example output: ",(excercise[::-1]))
    print("---------------------------------------------------------------")
    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        #Tekst met bedankt voor het testen
        print("Thanks for testing!")
        #Wachten op enter om opnieuw te beginnen
        answer = input("test again? Press enter")
        print("---------------------------------------------------------------")
        #Terug naar het begin
        return reverse()
#einde declaratie reverse
reverse()