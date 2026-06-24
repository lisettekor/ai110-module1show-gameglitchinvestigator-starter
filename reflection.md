# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Initially, the hint was incorrect. The message was “Go LOWER!” when it should be “Go HIGHER!”, while the message was “Go HIGHER!” when it should be “Go LOWER!”. Also, nothing happens when the "New Game" button is clicked. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret is 35. Guess is 9.|Hint shown is “Go HIGHER!”|Hint shown is “Go LOWER!”|None|
|Click “New Game” button.|The page is refreshed to initial state where a new secret number is generated, attempt is zero, history is empty and score is reset to initial value.|Nothing happens.|None|
|Change difficulty dropdown from Normal to Easy |“Guess a number between 1 and 20.” |It is always showing “Guess a number between 1 to 100.” Regardless of difficulty. | None|
|Enter any guess number and click enter.  |Since there is a message that says “Press Enter to apply”, when you press enter, it should submit the guess. |There's a message "Press Enter to apply" on the text box. However, when I click enter, nothing happens. It does not submit the Guess.| None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude Haiku 4.5.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
AI fixed the "New Game" button handler which used to do nothing. Claude fixed it to reset the attempts and score to initial value, status to "playing" (to re-enable gameplay), cleared guess history. Additionally, it decided to also do the proper refactoring since logic_utils.py currently has stubs, it made updates to complete the implementation there and have app.py import from it. I verified the result by running the program to see if clicking the "New Game" button will restart the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude added st.rerun(). However, the hint was being displayed and then immediately cleared by the st.rerun() call. I manually tested and reported. Claude revised the code such that the hint message is stored in session state and displayed persistently below the buttons, so it will survive the page reruns.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
I tested by running the Streamlit app and checked if the behavior matched my expected outcome. I repeated the process after each code change to confirm that the bug is fully resolved.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested by clicking the "New Game" button. However, nothing happened. It revealed a bug since it was not properly resetting state variables.
- Did AI help you design or understand any tests? How?
  For every bug I reported, AI explained what had to be fixed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" refreshes the screen back to its initial state. While session state keeps track of your interactions during a session. So it remembers values like the secret number, score, and attempts to keep the game running.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? - This could be a testing habit, a prompting strategy, or a way you used Git.
  Test every change by running the app. Not every code change works the first time, so testing immediately helps catch issues early before the changes become too big too track.
  
- What is one thing you would do differently next time you work with AI on a coding task?
I would be more strategic with my prompts. Since every prompt costs money, I want to rely on AI for parts that truly need help and fix the smaller, obvious bugs myself before asking.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI can help me accomplish a lot very quickly. However I also realized that I cannot assume that the model will get it right all the time.