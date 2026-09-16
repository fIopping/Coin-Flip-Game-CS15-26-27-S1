import random

def main():
    score = 0
    streak = 0

    print("coin flip game, streak bonus edition")
    print("Guess heads or tails. Get 5 correct in a row to double your points!\n")

    while True:
        coin = random.choice(["heads", "tails"])

        # Input validation loop
        while True:
            guess = input("What is your guess? (heads/tails/quit)\n").lower()
            if guess in ("heads", "tails", "quit"):
                break
            else:
                print("invalid input. please type 'heads', 'tails', or 'quit'.")

        if guess == "quit":
            print(f"\nfinal score: {score}")
            break

        if guess == coin:
            points = 1
            streak += 1
            if streak >= 5:
                points *= 2
                print(f"correct! streak bonus active - points doubled!")
            else:
                print("correct!")
            score += points
        else:
            print(f"incorrect! The coin was {coin}.")
            streak = 0

        print(f"Score: {score} | current streak: {streak}\n")

if __name__ == "__main__":
    main()