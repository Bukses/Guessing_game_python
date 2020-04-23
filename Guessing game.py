print(''' 
 Welcome to the Guessing Game!

 Please input a level 

 Easy > You are required to guess the secret number between 1 - 10 with SIX guesses.
 Medium > You are required to guess the secret number between 1 - 20 with FOUR guesses.
 Hard > You are required to guess the secret number between 1 - 50 with THREE guesses.
 
 Goodluck!
 ''')

level=""
guess_count = 1
while True:
    level = input("Type a level: ")
    if level == "easy":
        print (" You have selected the EASY level \n You have 6 guesses \n You are only allowed to pick a number between 1 and 10")
        guess_limit = 6
        correct_no = 7
        guess = int(input("Guess a number: "))
        while guess_count < guess_limit:
            guess_limit-=1
            if guess > 10:
                print (f" Your number must be less than or equal to 10 \n You have {guess_limit} guess(es) left.")
                guess = int(input("Make another guess: "))
            elif guess != correct_no:
                print (f" That was wrong. \n You have {guess_limit} guess(es) left.")
                guess= int(input("Guess Again: "))
            elif guess == correct_no:
                print ("You won!")
                break
        else:
            print ("Game over. You have exhausted all your guesses.")

    elif level == "medium":
        print (''' You have selected the MEDIUM level
 You have 4 guesses.
 You are only allowed to pick a number between 1 and 20 ''')
        guess_limit_m = 4
        correct_no_m = 3
        guess = int(input("Guess a number: "))
        while guess_count < guess_limit_m:
            guess_limit_m-=1
            if guess > 20:
                print (f" Your number must be less than or equal to 20 \n You have {guess_limit_m} guess(es) left.")
                guess = int(input("Make another guess: "))
            elif guess != correct_no_m:
                print (f" That was wrong. \n You have {guess_limit_m} guess(es) left.")
                guess= int(input("Guess Again: "))
            elif guess == correct_no_m:
                print ("You won!")
                break
        else:
            print ("Game over. You have exhausted all your guesses." )

    elif level == "hard":
        print (''' You have selected the HARD level
 You have 3 guesses.
 You are only allowed to pick a number between 1 and 50 ''')
        guess_limit_h = 3
        correct_no_h = 14
        guess = int(input("Guess a number: "))
        while guess_count < guess_limit_h:
            guess_limit_h-=1
            if guess > 50:
                print (f" Your number must be less than or equal to 50 \n You have {guess_limit_h} guess(es) left.")
                guess = int(input("Make another guess: "))
            elif guess != correct_no_h:
                print (f" That was wrong. \n You have {guess_limit_h} guess(es) left.")
                guess= int(input("Guess Again: "))
                continue
            elif guess == correct_no_h:
                print ("You won!")
                break
        else:
            print ("Game over. You have exhausted all your guesses." )





    

        