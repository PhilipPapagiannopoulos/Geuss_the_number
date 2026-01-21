## Guess the Number (Python)

This project is a **Guess the Number** game written in **Python**, where the player must guess a randomly generated number between **1 and 1000**.

The player starts with **10 lives**. After each guess, the game gives a hint:

* **“go up”** if the guessed number is too low
* **“go down”** if the guessed number is too high

Each incorrect guess costs one life. The game continues until the player correctly guesses the number or runs out of lives. At the end of the game, the program displays whether the player won, how many attempts were used, and reveals the secret number.

### Features

* Random number generation between 1 and 1000
* Hint system to guide the player
* Life-based attempt limit (10 lives)
* Attempt counter
* Clear win/lose outcome

### Technologies Used

* Python
* `random` module
