secret_word = "girrafe"
guess = ""
guess_count = 0
total_guess = 3
out_of_guess = False
while secret_word != guess and not out_of_guess:
    if guess_count<total_guess :
        guess= input("Enter your guess: ")
        guess_count= guess_count + 1
    else:
        out_of_guess = True


if out_of_guess :
    print("Sorry you are out of guesses, You lose! ")
else:
    print("You won")