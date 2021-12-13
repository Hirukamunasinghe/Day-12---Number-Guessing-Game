from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answer(user_guess, answer, turns):
    """Checks the answer against the user guess. Returns the number of turns remaining"""
    if user_guess > answer: 
        print("Too high")
        return turns -1
    elif user_guess < answer: 
        print("Too low") 
        return turns -1
    elif user_guess == answer: 
        print(f"You got it! The answer was {answer}")

def difficulty():
     level = input("Choose difficulty, 'easy' or 'hard'? ")
     if level == "easy": 
         return EASY_LEVEL_TURNS
     else: 
         return HARD_LEVEL_TURNS



def game():
    print(logo)
    #Choose a random number between 1 and 100
    print("Welcome to the number guessing game! ")
    print("I'm thinking of a number between 1 and 100.")
    import random
    answer = random.randint(1, 100)
    print(f"The correct answer is {answer}")


    turns = difficulty()

    #Build function to choose difficulty
    #Let the user guess the number
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts to guess the number." )
        user_guess = int(input("Guess the number between 1 and 100. "))

        turns = check_answer(user_guess, answer, turns)
        if turns == 0: 
            print("You are out of attempts. You loose")
            return
        elif user_guess != answer: 
            print("Guess again!")






#function to check the user's guess against the actual answer

#Track the number of turns and reduce by 1 if the answer is wrong


 #Repeat the function if they get it wrong
game()


