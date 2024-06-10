from terminal import Terminal

def __main__():
    candidates = [item for item in input("Please give a list of the words ").split(", ")]

    game = Terminal(candidates)
    # Check that all words are the same length
    length_check = game.check_candidates_length()
    print(length_check)
    
    while length_check != None:
        
        print(f"All candidates are not the same length, Check '{length_check}'")
        new_word = str.lower(input(f"Replace '{length_check}' with a new word: "))
        game.replace_candidate(length_check, new_word)
        length_check = game.check_candidates_length()    

    
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
