# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of the game is for the player to guess the secret number within the attempts allowed depending on the difficulty selected. When difficulty is Easy, the range is 1 to 20 with 6 attempts allowed; When difficulty is Normal, the range is 1 to 100 with 8 attempts allowed; When difficulty is Hard, the range is 1 to 50 with 5 attempts allowed. The player wins if he/she is able to guess the secret number within the number of attempts allowed. 
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The default difficulty is Normal, so a secret number is generated between 1 and 100.
2. The player enters a number between 1 and 100.
3. The app compares the guess with the secret number and returns the outcome with a message. 
4. The player wins when they guess correctly within 8 attempts since difficult is Normal. When the player wins, the final score is shown, balloons appear and the game ends.
5. The player loses when they reached 8 attempts without guessing the correct number. The final score is shown and the game ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
==================================== test session starts =====================================
platform win32 -- Python 3.13.14, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\CodePath\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 3 items                                                                             

tests\test_game_logic.py ...                                                            [100%]

===================================== 3 passed in 0.04s ======================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
