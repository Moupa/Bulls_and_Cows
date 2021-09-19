### Bulls & Cows

#### Task Description

Your task is to create a program that would simulate **Bulls and Cows** game.

 * First of all, the computer will generate a 4-digit secret number. The digits must be all different.
 * Then, in turn, the user tries to guess their computer's number. The computer prompts the user for a number and after the input has been received, the computer responds with the number of matching digits.
 * If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".

For example, let's say the number is 2017. A sample interaction might look like this:

```
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number
>>> 1234
0 bulls, 2 cows
>>> 6147
1 bull, 1 cow
>>> 2417
3 bulls, 0 cows
>>> 2017
Correct, you've guessed the right number in 4 guesses!
That's {amazing, average, not so good, ...}
```

##### Bonus

Extend the functionality of the program as you wish. For example

 * Counting time it took to guess the number
 * Count the number of guesses and store them in a file and at the end depict user's stats (the best player etc.)

#### Source Code

The source code can be found in the file **bulls_and_cows.py**
