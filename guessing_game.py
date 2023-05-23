import random


def input_validator():
    while True:
        entry = input("ok, what number do you think I have? \n")
        try:
            entry = int(entry)
        except ValueError:
            print("enter an integer!")
        else:
            return entry


def guessing_game():
    tries_left = int(input("In how many attempts do you bet you'll guess it? :)\n"))
    while tries_left <= 0:
        print("please input a value greater than 0\n")
        tries_left = int(input("In how many attempts do you bet you'll guess it? :)\n"))

    num_to_guess = random.randint(0, 50)
    print(num_to_guess, "is the target")
    guess = input_validator()

    while num_to_guess != guess and tries_left > 1:
        if guess < num_to_guess:
            tries_left = tries_left - 1
            print("Number too low\n"
                  "you have ", tries_left, " tries left")
            guess = input_validator()
        elif guess > num_to_guess:
            tries_left = tries_left - 1
            print("Number too high\n"
                  "you have ", tries_left, " tries left")
            guess = input_validator()
    if num_to_guess == guess:
        print("Excellent, the correct number was ", num_to_guess)
        quit()
    elif num_to_guess != guess:
        print("Sorry, you ran out of tries, the correct number was ", num_to_guess)


if __name__ == '__main__':
    guessing_game()
