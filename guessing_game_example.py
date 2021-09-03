secret_word = "dog"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count == guess_limit:
        out_of_guesses = True
        break
    guess = input("Enter guess : ")
    guess_count += 1


if out_of_guesses:
    print("You lost!")
else:
    print("You win!")
