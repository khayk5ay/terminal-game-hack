from terminal import Terminal

def __main__():
    list_of_candidates = []
    candidates = [item for item in input("Please give a list of the words ").split(", ")]

    game = Terminal(candidates)

    print("Game Initiated")
    
    while len(game.candidates) > 1:
        print(f"Available candidates are {game.candidates}")
        print(f"Number of candidates : {len(game.candidates)}")
        likely = input("Would you like to know a highly likely candidate? Y/N ")

        if likely == "Y":
            game.most_likely()

        
        guess = input("What is your guess? ") 
        clue = input("What is the clue? ")
        clue = int(clue)
        game.update_candidates(guess, clue)
            
    print(f"Last Candidate Standing is {game.candidates[0]}")
    

__main__()
