import random

def main():
    points = 0
    streak = 0
    word_choice = ("heads" or "tails")

    print("Welcome!\n")
    print("Heads or Tails\n")

    while True:

        coin = random.choice(["heads", "tails"])


        while True:
            guess = input("Guess a coin:")
            if guess != "heads" and guess != "tails":
                print ("Type in heads or tails")

            else:
                break


        if coin != guess:
            points -= 1
            if points <0:
                points = 0
            streak = 0
            print (f"Incorrect! You failed.\n Your current points: {points}\n Your current streak: {streak}\n")




        if coin == guess:
            points += 1
            streak += 1
            print(f"Correct!\n Your current points: {points}\n Your current streak: {streak}\n")

            if streak >= 5:
                points *=2

main()






