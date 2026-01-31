playerName=input("Enter the player's name:")
gamesPlayed=int(input("Enter games played:"))
score=int(input("Enter score achieved:"))
aveScore=score/gamesPlayed

print(f"Player:{playerName}\nGames Played:{gamesPlayed}\nTotal Score:{score}\nAverage Score:{aveScore}")