#day 2
from utils import read_lines_from_file
#rock
#A = 1
#X = 0 lose
#paper
#B = 2
#Y = 3 draw
#scissors
#C = 3
#Z = 6 win

#conditions
win = 6
draw = 3
rock = 1
paper = 2
scissors = 3

def rock_paper_scissors_score(game):
    opp = game[0]
    user = game[2]
    result = 0

    #opponent chooses rock
    if opp == "A":
        if user == "Y":
            result += rock + draw
        elif user == "X":
            result += scissors # lose
        else:
            result += paper + win

    #opponent chooses paper
    elif opp == "B":
        if user == "Z":
            result += scissors + win
        elif user == "Y":
            result += paper + draw
        else:
            result += rock # lose

    #opponent chooses scissors
    else:
        if user == "X":
            result += paper # lose
        elif user == "Z":
            result += rock + win
        else:
            result += scissors + draw

    return result

total_score = 0
games_list = read_lines_from_file("acday2.txt")
print(games_list)
for game in games_list:
    score = 0
    opp = game[0]
    user = game[2]
    score += rock_paper_scissors_score(game)
    print(f"game: {game}, opp: {opp}, user: {user}, score: {score}")
    total_score += score

print(total_score)
