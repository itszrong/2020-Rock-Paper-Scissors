import random

choices = ["rock", "paper", "scissors"]
print (choices)

#Number_of_players = int(input("How many players are there?"))

number_of_players = 5
noPlayers = number_of_players
Players_choices = []
noGames = 0
noGames_list = []
iterations = 500000

def counter(Players_choices, noPlayers, Str):
    noStr = 0
    for i in range(noPlayers):
        if Players_choices[i] == Str:
            noStr += 1
    return noStr

def game(noPlayers, noGames, noGames_list):


#    print(noGames)
#    print("No. of plcayers is", noPlayers)

    if noPlayers == 1:
        noGames_list.append(noGames)

        """print("Number of players is", number_of_players)"""

        noPlayers = number_of_players
        noGames = 0
    else:
        noGames += 1
        Players_choices = []
        for i in range (noPlayers):
            Players_choices.append(random.choice(choices))

        #print (Players_choices)


        if ("rock" in Players_choices):
            noRock = counter(Players_choices, noPlayers, "rock")
            if ("scissors" in Players_choices):
                noScissors = counter(Players_choices, noPlayers, "scissors")
                if ("paper" in Players_choices):
                    game(noPlayers, noGames, noGames_list)
                    #all are in so no winner so start again
                else:
                    #only rock and scissors
                    noPlayers-=noScissors
                    game(noPlayers, noGames, noGames_list)

            else:

                #no scissors only rock so far
                if ("paper" in Players_choices):
                    noPaper = counter(Players_choices, noPlayers, "paper")
                    #paper and rock only
                    noPlayers-=noRock
                    game(noPlayers, noGames, noGames_list)
                else:
                    # only rock, no paper and no scissors
                    game(noPlayers, noGames, noGames_list)
        else: # no rock
            if ("scissors" in Players_choices):
                noScissors = counter(Players_choices, noPlayers, "scissors")
                if ("paper" in Players_choices):
                    noPaper = counter(Players_choices, noPlayers, "paper")
                    noPlayers-=noPaper
                    #scissors and paper
                    game(noPlayers, noGames, noGames_list)
                else:
                    #only scissors
                    game(noPlayers, noGames, noGames_list)


            else: #only paper
                game(noPlayers, noGames, noGames_list)


for i in range (iterations):
#    print(i)
    game(noPlayers, noGames, noGames_list)

#print("The", noGames_list)
print("The number of iterations is", len(noGames_list))
ave = 0
for i in range (iterations):
    ave+=noGames_list[i]
print("average is", ave/iterations)

