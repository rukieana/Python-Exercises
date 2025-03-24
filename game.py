def main():
    difficulty = input ("Difficult or Casual?")
    if not(difficulty == "Difficult" or difficulty == "Casual" ):
        print ("Enter a valid difficulty")
        return
    
    players = input ("Multiplayers or SinglePlayers?")
    if not( players == "Multiplayers" or  players == "SinglePlayers" ):
        print ("Enter a valid difficulty")
        return

    if ( difficulty == "Difficult" and  players == "Multiplayers"):
        recommend("Poker")
    elif (difficulty == "Difficult" and  players == "inglePlayers"):
        recommend("Klond Like")
    elif( difficulty == "Casual" and  players == "Multiplayers"):
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)

main()


