# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?\
Shows a guessing number game from 1 to 100. Shows three difficulty settings and debug menu to see if output is expected.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").\
  Shown attempts are not syncing with the actual attempts.\
  Hint says to go lower but the guess is already lower.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Click New Game | New Game Should Start | New Game didnt start | 'none' |
| Click Hint  | Hint should show correct direction | Hint directed further from target | 'none' |
| Number into guess | Number should be in range of difficulty | Game processd as normal | 'none' |
<!-- |Diffioculty spike|
|Attempts be 1 lower than the supposed attempt|
|Secret is outside of range of difficulty|
| new game added extra attempts. history just didnt sync| -->

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?\
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It pinpointed how the secret on every second attempt was being turned into a string. The guess and secret were being compared lexiographically and led into wrong guesses. Verified with the streamlit application.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).\
I asked to showcase the error of how the hint straying further from the secret but it discovered another error of how the secret sometimes turn into a string. This was my example of how it was correct but it didn't find the initial error until i did another session after I fixed the bug it discovered first.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Through pytest in test_game_logic.py.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
Helped design the tests to adjust to any changes that was made during our sessions.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Helps showcase your app in a UI friendly matter.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?\
Verify any changes and commands AI is trying to suggest.

- What is one thing you would do differently next time you work with AI on a coding task?
Add more context.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I definitely wanted to be specific in the issue I am looking for. And to always verify the changes it makes while being aware as a developer.
