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

| Input | Expected Behavior | Actual Behavior |   Fixes Applied        |
|-------|-------------------|-----------------|------------------------|
|Secret is 35. Guess is 9.|Hint shown is “Go HIGHER!”|Hint shown is “Go LOWER!”|Outcome of “Too High” or “Too Low” was correct but the message is flipped between the two. 4 lines of code were updated.|
|Click “New Game” button.|The page is refreshed to initial state where a new secret number is generated, attempt is zero, history is empty and score is reset to initial value.|Nothing happens.|AI fixed the "New Game" button handler which used to do nothing. Claude fixed it to reset the attempts and score to initial value, status to "playing" (to re-enable gameplay), cleared guess history. Additionally, it decided to also do the proper refactoring since logic_utils.py currently has stubs, it made updates to complete the implementation there and have app.py import from it.|
|Change difficulty dropdown from Normal to Easy |“Guess a number between 1 and 20.” |It is always showing “Guess a number between 1 to 100.” Regardless of difficulty. |The message is hardcoded to "Guess a number between 1 and 100." It should use the low and high variables that are already calculated based on difficulty.
•	Easy: 1-20
•	Normal: 1-100
•	Hard: 1-50|
|Enter any guess number and click enter.  |Since there is a message that says “Press Enter to apply”, when you press enter, it should submit the guess. |There's a message "Press Enter to apply" on the text box. However, when I click enter, nothing happens. It does not submit the Guess.|The fix wraps the text input and submit button in a form using st.form() and st.form_submit_button(). Now when you press Enter in the text box, it will submit the form instead of just clearing the input.|



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
