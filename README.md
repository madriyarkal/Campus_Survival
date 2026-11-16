# Campus Survival - A Terminal-Based University Game

## In Class Project Title

**Campus Survival - A Terminal-Based University Game**

## Student Developer

- **Full Name:** Ekin Uğur Panko
- **Student Number:** 250416018

## Course Info

- **Course Code and Name:** EEM2005 - Programming in Engineering
- **Academic Term:** Fall 2026-2027

## Instructor

Asst. Prof. Dr. Ulya Bayram

## University

Canakkale Onsekiz Mart University

## Faculty

Faculty of Engineering

## Department

Electrical and Electronics Engineering

---

## Description

**Campus Survival** (Turkish: *Kampüste Hayatta Kal*) is a simple, text-based game played entirely in the terminal. The player is an engineering student at Canakkale Onsekiz Mart University who has to survive a typical (and slightly absurd) day on campus.

During the day, the player faces random everyday situations such as a LED that does not light up in the lab, a projector that fails during a presentation, or a computer that shuts down before the homework is submitted. For each situation the player chooses one of three options. Some options are logical, some are funny and some are clearly bad ideas.

The goal is to make the right decisions and finish the day with the highest possible score. All in-game texts are in Turkish.

## How to Play

- The player starts with **100 points** and **3 lives**.
- The game consists of **10 rounds**.
- In every round a random event is selected. The same event never appears twice in one game.
- Each event has **3 options**. Type `1`, `2` or `3` and press Enter to choose.
- The current round, score and lives are shown at the start of every round.
- A **correct choice** keeps your score.
- A **wrong choice** costs **5, 10, 15 or 20 points**.
- Some **serious mistakes** also cost **1 life**.
- The score can never go above 100.
- Invalid input (letters, other numbers, empty input) is rejected and the question is asked again.

**Winning and losing:**

| Result | Condition |
|---|---|
| Game over | Score drops to 0 **or** lives drop to 0 |
| Successful | All 10 rounds completed with **70 or more points** and at least 1 life |
| Not successful | All 10 rounds completed with **less than 70 points** |

At the end of the game, the final result is shown and the player can choose to play again (`e` = yes, `h` = no).

## Requirements

- Python 3
- No external libraries are required (only the built-in `random` module is used).
- Jupyter Notebook is not required.

## Installation

1. Open the GitHub page of the `campus-survival` repository.
2. Click the green **Code** button and select **Download ZIP**, then extract the ZIP file.

   Or clone the repository with Git:

   ```bash
   git clone https://github.com/madriyarkal/campus-survival.git
   ```

3. Open a terminal inside the project folder:

   ```bash
   cd campus-survival
   ```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

On some systems the command may be `python3 main.py`.

## Python Concepts Used

- **Class:** The `Game` class keeps the game state (score, lives, round, selected events) and contains the methods that run the game.
- **if / elif / else:** Used to check the player's choice, apply penalties, keep the score between 0 and 100, and decide the final result.
- **Loops:** A `for` loop plays the 10 rounds and prints the options; `while` loops repeat questions until a valid input is given and allow the player to play again.
- **Functions:** Tasks are split into small functions and methods such as `show_status()`, `get_choice()`, `apply_result()`, `play_round()`, `show_final()` and `main()`.
- **Lists:** All events are stored in a list, and every event's options are stored in a list.
- **Dictionaries:** Each event is a dictionary with the keys `title`, `text` and `options`.
- **random:** `random.sample()` selects 10 different events, so no event repeats in the same game.
- **Input / Output:** `input()` reads the player's choices and `print()` shows the events, results and status in the terminal.

## Project Structure

```
campus-survival/
├── main.py      # The complete game code (events, Game class and main loop)
└── README.md    # Project documentation
```

- **main.py:** Contains all the game code: the list of events, the `Game` class and the `main()` function that starts the game.
- **README.md:** Explains the project, the student and course information, how to install, run and play the game.
