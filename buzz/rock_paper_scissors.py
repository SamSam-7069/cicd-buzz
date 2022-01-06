import random



choose = ["rock", "paper", "scissors"]

def rock_paper_scissors():
    print(choose)
    speler_1 = choose[(random.randrange(0,3))]
    speler_2 =  choose[(random.randrange(0,3))]

    if speler_1 == speler_2:
        winnaar = "gelijk spel"
    elif speler_1 == "rock":
        if speler_2 == "scissor":
            winnaar = "Rock smashed scissor"
        else:
            winnaar = "Paper covers rock! You lose."
    elif speler_1 == "paper":
        if speler_2 == "rock":
            winnaar = "Paper covers rock! You win!"
        else:
            winnaar = "Scissors cuts paper! You lose."
    elif speler_1 == "scissors":
        if speler_2 == "paper":
            winnaar = "Scissors cuts paper! You win!"
        else:
            winnaar = "Rock smashes scissors! You lose."
    

    return speler_1, speler_2, winnaar
