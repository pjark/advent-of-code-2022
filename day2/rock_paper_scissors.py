player_score_dict = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissors
}

def get_outcome(opp_move, player_move)->int: 
    if (player_move == "X"): # rock
        if (opp_move == "A"):
            return 3
        elif (opp_move == "B"):
            return 0
        elif (opp_move == "C"):  
            return 6
    elif (player_move == "Y"): # paper
        if (opp_move == "A"):
            return 6
        elif (opp_move == "B"):
            return 3
        elif (opp_move == "C"):
            return 0
    elif (player_move == "Z"): #scissor
        if (opp_move == "A"):
            return 0
        elif (opp_move == "B"):
            return 6
        elif (opp_move == "C"):
            return 3

    return -1

def get_round_score(opp_move, result)->int:
    if (result == "X"): # lose
        if (opp_move == "A"):
            return player_score_dict["Z"]
        elif (opp_move == "B"):
            return player_score_dict["X"]
        elif (opp_move == "C"):
            return player_score_dict["Y"]
    elif (result == "Y"): # draw
        if (opp_move == "A"):
            return (3 + player_score_dict["X"])
        elif (opp_move == "B"):
            return (3 + player_score_dict["Y"])
        elif (opp_move == "C"):
            return (3 + player_score_dict["Z"])
    elif (result == "Z"): # win
        if (opp_move == "A"):
            return (6 + player_score_dict["Y"])
        elif (opp_move == "B"):
            return (6 + player_score_dict["Z"])
        elif (opp_move == "C"):
            return (6 + player_score_dict["X"])

    return -1

def part1():
    total_score = 0
    with open(sys.argv[1]) as f:
        for line in f:
            opp_move, player_move = line.split()
            total_score += player_score_dict[player_move] + get_outcome(opp_move, player_move)
    print("\nTotal score is: "+str(total_score))

def part2():
    with open(sys.argv[1]) as f:
        total_score = 0
        for line in f:
            opp_move, result = line.split()
            total_score += get_round_score(opp_move, result)
    print("\ntotal_score is: "+str(total_score))

import sys

### cli input checking ###
if len(sys.argv) != 2:
    sys.exit("[ERROR: Carmy] Input error!")

# part1()
part2()
