import random

def main():
    points = 1
    streak = 0
    word_choice = ("heads" or "tails")

    print("Welcome!")
    print("Heads or Tails\n")

    while True:
        coin = random.choice(["heads", "tails"])
        guess = input("Guess a coin\n:")
        if guess != word_choice:
            print("Wrong!")
        if coin == guess:
            points += 1
            streak +=1
            if streak >= 5:
                points *=2

main()






