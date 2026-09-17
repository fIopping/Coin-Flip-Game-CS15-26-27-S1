# Activity 4: Coin Flip Game

In this activity, we will walk through how to create a game where the user attempts to guess whether a coin will land "Heads" or "Tails".

When you have completed the tutorial be sure to also complete the [Extension Activity](#extension-activity-coin-flip-game-with-a-twist)!

It is also important to note, that for this unit going forwards, some activities will not be fully spelled out in terms of the actual code. Instead, activities will focus on demonstrating the programming structure through pseudocode and flowcharts, giving you the opportunity to build the actual code out!

## 1. Create the Root Folder

Whenever you are creating a new Python project, it is best to stay organized by placing all the files related to the project in the same folder. Create a new folder called `root`.

Inside the folder, create a new `root/main.py` file.

## 2. Planning the Game Loop Structure

The way that our coin game will work is that there will be an infinite loop that requests input from the user. There will also be a loop to validate the user input before continuing. Once a valid input has been received, we will check to see if the user guessed correctly. Then we will output their result, and start the loop over again.

A flowchart for this might look like this:

![Example coin game flowchart](./example-coin-game.jpg)

## 3. Planning the Program Structure

The pseudocode structure for this program might look like this:

```txt
PROGRAM START
WHILE True
    coin = random choice from ("Heads", "Tails)
    INPUT guess
    IF guess == coin THEN:
        OUTPUT "Correct"
    ELSE:
        OUTPUT "Incorrect"
    END IF
END WHILE
END PROGRAM
```

## 4. Implementing the Program

With a structure outlined, it's time to turn our pseudocode into code! 

While our Pseudocode mostly looks like regular Python, there are some specific tweaks than you'll need to make, especially when it comes to random values.

Python has a library called "random" that can be imported at the top of your program with the following code:

```python
import random
```

Some key uses for random are generating a randome number between 0 and 1:

```python
# Random float between 0 and 1
value = random.random()
```

A random integer in an inclusive range (meaning the random number can be either the highest or lowest number):

```python
# Random integer where 1 <= integer <= 10
value = random.randint(1, 10)
```

A random value from a list:
```python
# Random choice between "Left" or "Right"
value = random.choice(["Left", "Right"])

# Another valid syntax for random choice
choices = ["Left", "Right"]
value = random.choice(choices)
```

Using Python syntax, create the program and test it. Does it work? What if the user inputs random text, like "hello?".

If your program matches the structure above exactly, you'll notice that it's missing input validation. Input validation is crucial to creating working programs because it prevents the user from typing in nonsense and breaking your program.

We should restructure our program to look more like this:

![Flowchart with input validation](./example-flowchart-input-validation.jpg)

```txt
PROGRAM START
WHILE True
    coin = random choice from ("Heads", "Tails)
    WHILE True
        INPUT guess
        IF guess is "Heads" or guess is "Tails" THEN:
            BREAK
        ELSE:
            OUTPUT "Invalid input."
        END IF
    END WHILE
    IF guess == coin THEN:
        OUTPUT "Correct"
    ELSE:
        OUTPUT "Incorrect"
    END IF
END WHILE
END PROGRAM
```

**Tip:** Python has a special method for string values that can set them to lowercase: `string.lower()`.

To get and check the lowercase input from the user, your code might look something like this:

```python
guess = input("What is your guess?\n")

guess = guess.lower()
```

Remember that it can be easier to validate and use input if we set it all to lowercase. This means that our input is effectively no longer case-sensitive.

# Extension Activity: Coin Flip Game with a Twist

Create your own version of the Coin Flip Game. Your program should keep the same basic structure from the tutorial, but add one of the game mechanics below.

## Requirements

* Keep the original coin flip gameplay: the player guesses **Heads or Tails**, and the program randomly determines the result.

* Use a loop so the game continues for multiple rounds.

* Validate the player's input so only valid guesses are accepted.

* Add **one** of the following twists:

  * **Three Strikes:** The game continues until the player makes **3 incorrect guesses in a row**. A correct guess resets the incorrect-guess counter to 0.
  * **Streak Bonus:** Keep track of the player's score and consecutive correct guesses. After **5 correct guesses in a row**, all points earned are **doubled** until the streak is broken by an incorrect guess.
  * **Wager System:** The player starts with **10 points**. Before each coin flip, the player chooses how many of their current points to wager. A correct guess adds the wager to their score, while an incorrect guess subtracts the wager. The player cannot wager more points than they currently have.

* Display the information needed for the chosen twist after each round, such as the current score, streak, incorrect-guess count, or remaining points.

