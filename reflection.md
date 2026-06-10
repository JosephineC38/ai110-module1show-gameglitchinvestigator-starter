# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The first time I ran it, it was very buggy and confusing. I tested 0 as my first input and I didn't get an error message that it 
  was out of range, which was odd. The history array wasn't updating and I had to put another input for my first input to show.
  Afterwards, I had to click the "Submit Guess" button to get the correct hint and it defaulted to the "Too Low" hint for the first input. 

  Concrete Bugs
  - After losing a game, when clicking the "New Game" button, none of the variables in the developer log updated and nothing is indicated to the user that their game has reset. 
  - If entering nothing, it appear in the history array as an empty string. It is allowed to go over a size of 7, however if a valid input is given and the array's length > 6, then the game is considered over. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 0     | Received error message stating out of number range. | "Too Low" hint shown, the secret number was 76. History array didn't update. | "none"
| 101 | Received error message stating out of number range. | "Too Low" hint shown, the secret number was 79. History array didn't update. | "none"
| Clicked "New Game" button without finishing current game. | Variables in the devloper log would reset | Attempts left on user-side is set to 8, score is unchanged, history array is unchanged. Only the secret number is chaned from the previous game. | "none"

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
