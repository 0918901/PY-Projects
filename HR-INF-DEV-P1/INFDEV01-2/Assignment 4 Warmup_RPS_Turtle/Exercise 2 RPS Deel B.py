# coding=utf-8
__author__ = '0918901'
print("---------------------------------------------------------------")
#Naam opdracht
print("Assignment 4 Exercise 2 RPS Deel B")
print("---------------------------------------------------------------")

#declaratie RPS
def RPS():
    #Spel naam
    print("Player VS Player [Rock,Paper,Scisscors,Lizzard,Spock]")
    print("---------------------------------------------------------------")
    #spel uitleg
    print("Game Choices")
    print("1 = Rock")
    print("2 = Scissors")
    print("3 = Paper")
    print("4 = Lizzard")
    print("5 = Spock")
    print("---------------------------------------------------------------")

    #Mogelijke keuzes spelers
    player1_choice  = 1,2,3,4,5
    player2_choice  = 1,2,3,4,5

    #Player 1
    #Zolang bovenstaande klopt wordt het onderstaande wordt uitgevoerd
    while True:
        #Tekst die aangeeft wie er aan de beurt is
        print("Player 1")
        #Invoer keuze Speler 1
        print("choose a number:")
        choice = input('=')
        print("---------------------------------------------------------------")
        #Detect Invoer keuze Rock Speler 1
        if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
            player1_choice = 1
            break
        #Detect Invoer keuze Scissors Speler 1
        elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
            player1_choice = 2
            break
        #Detect Invoer keuze Paper Speler 1
        elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
            player1_choice = 3
            break
        #Detect Invoer keuze Lizzard Speler 1
        elif choice == 'L' or choice == 'l' or choice == 'Lizzard' or choice == 'lizzard' or choice == '4':
            player1_choice = 4
            break
        #Detect Invoer keuze Spock Speler 1
        elif choice == 'SP' or choice == 'sp' or choice == 'Spock' or choice == 'spock' or choice == '5':
            player1_choice = 5
            break
        #Als bovenstaande niet van toepassing is wordt onderstaande gebruikt
        else:
            #Foutmelding bij ongeldige invoer
            print("---------------------------------------------------------------")
            print('That\'s not possible!!')
            #Tekst die aangeeft wat er moet gebeuren
            print('Please try again')
            print("---------------------------------------------------------------")
            #Probeer nog eens
            continue

    #Player 2
    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        #spel uitleg
        print("Game Choices")
        print("1 = Rock")
        print("2 = Scissors")
        print("3 = Paper")
        print("4 = Lizzard")
        print("5 = Spock")
        print("---------------------------------------------------------------")
        #Tekst die aangeeft wie er aan de beurt is
        print("Player 2")
        #Invoer keuze Speler 2
        print("choose a number:")
        choice = input('=')
        print("---------------------------------------------------------------")
        #Detect Invoer keuze Rock Speler 2
        if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
            player2_choice = 1
            break
        #Detect Invoer keuze Scissors Speler 2
        elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
            player2_choice = 2
            break
        #Detect Invoer keuze Paper Speler 2
        elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
            player2_choice = 3
            break
        #Detect Invoer keuze Lizzard Speler 2
        elif choice == 'L' or choice == 'l' or choice == 'Lizzard' or choice == 'lizzard' or choice == '4':
            player2_choice = 4
            break
        #Detect Invoer keuze Spock Speler 2
        elif choice == 'SP' or choice == 'sp' or choice == 'Spock' or choice == 'spock' or choice == '5':
            player2_choice = 5
            break

        #als bovenstaande niet wordt gebruikt wordt onderstaande van toepassing
        else:
            #Foutmelding bij ongeldige invoer
            print("---------------------------------------------------------------")
            print('That\'s not possible!!')
            #Tekst die aangeeft wat er moet gebeuren
            print('Please try again')
            print("---------------------------------------------------------------")
            #Probeer nog eens
            continue

    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        #Bij gelijk spel
        if player1_choice ==  player2_choice:
            print('It\'s a draw!')
            print("---------------------------------------------------------------")
    #Rules for Rock
        #Speler 1 Rock - Speler 2 Scissors
        elif (player1_choice == 1 and  player2_choice == 2 and print("Player 1 Wins! Because Rock smashes Scissors")):
            print("")

        #Speler 1 Rock - Speler 2 Paper
        elif (player1_choice == 1 and  player2_choice == 3 and print("Player 2 Wins! Because Paper covers Rock")):
            print("")

        #Speler 1 Rock - Speler 2 Lizzard
        elif (player1_choice == 1 and  player2_choice == 4 and print("Player 1 Wins! Because Rock crushes Lizzard")):
            print("")

        #Speler 1 Rock - Speler 2 Spock
        elif (player1_choice == 1 and  player2_choice == 5 and print("Player 2 Wins! Because Spock yaporizes Rock")):
            print("")
    #Rules for Scissors
        #Speler 1 Scissors - Speler 2 Rock
        elif (player1_choice == 2 and  player2_choice == 1 and print("Player 2 Wins! Because Rock smashes Scissors")):
            print("")

        #Speler 1 Scissors - Speler 2 Paper
        elif (player1_choice == 2 and  player2_choice == 3 and print("Player 1 Wins! Because Scissors cuts Paper")):
            print("")

        #Speler 1 Scissors - Speler 2 Lizzard
        elif (player1_choice == 2 and  player2_choice == 4 and print("Player 1 Wins! Because Scissors decapitates Lizzard")):
            print("")

        #Speler 1 Scissors - Speler 2 Spock
        elif (player1_choice == 2 and  player2_choice == 5 and print("Player 2 Wins! Because Spock smashes Scissors")):
            print("")
    #Rules for Paper
        #Speler 1 Paper - Speler 2 Rock
        elif (player1_choice == 3 and  player2_choice == 1 and print("Player 1 Wins! Because Paper covers Rock")):
            print("")

        #Speler 1 Paper - Speler 2 Scissors
        elif (player1_choice == 3 and  player2_choice == 2 and print("Player 2 Wins! Because Scissors cuts Paper")):
            print("")

        #Speler 1 Paper - Speler 2 Lizzard
        elif (player1_choice == 3 and  player2_choice == 4 and print("Player 2 Wins! Because Lizzard eats Paper")):
            print("")

        #Speler 1 Paper - Speler 2 Spock
        elif (player1_choice == 3 and  player2_choice == 5 and print("Player 1 Wins! Because Paper disproves Spock")):
            print("")
    #Rules for Lizzard
        #Speler 1 Lizzard - Speler 2 Rock
        elif (player1_choice == 4 and  player2_choice == 1 and print("Player 2 Wins! Because Rock cruches Lizzard")):
            print("")

        #Speler 1 Lizzard - Speler 2 Scissors
        elif (player1_choice == 4 and  player2_choice == 2 and print("Player 2 Wins! Because Scissors decapitates Lizzard")):
            print("")

        #Speler 1 Lizzard - Speler 2 Paper
        elif (player1_choice == 4 and  player2_choice == 3 and print("Player 1 Wins! Because Lizzard eats Paper")):
            print("")

        #Speler 1 Lizzard - Speler 2 Spock
        elif (player1_choice == 4 and  player2_choice == 5 and print("Player 1 Wins! Because Lizzard Poisons Spock")):
            print("")
    #Rules for Spock
        #Speler 1 Spock - Speler 2 Rock
        elif (player1_choice == 5 and  player2_choice == 1 and print("Player 1 Wins! Because Spock yaporizes Rock")):
            print("")

        #Speler 1 Spock - Speler 2 Scissors
        elif (player1_choice == 5 and  player2_choice == 2 and print("Player 1 Wins! Because Spock smashes Scissors")):
            print("")

        #Speler 1 Spock - Speler 2 Paper
        elif (player1_choice == 5 and  player2_choice == 3 and print("Player 2 Wins! Because Paper disproves Spock")):
            print("")

        #Speler 1 Spock - Speler 2 Lizzard
        elif (player1_choice == 5 and  player2_choice == 4 and print("Player 2 Wins! Because Lizzard poisons Spock")):
            print("")

        #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
        while True:
            print("---------------------------------------------------------------")
            #Tekst met bedankt voor het spelen
            print("Thanks for playing!")
            #Wachten op enter om opnieuw te beginnen
            answer = input("Play again? Press enter")
            print("---------------------------------------------------------------")
            #Terug naar het begin
            return RPS()
#einde declaratie RPS
RPS()