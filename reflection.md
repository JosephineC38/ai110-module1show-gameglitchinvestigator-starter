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
I used the built-in GitHub Copilot mode. One example of when an AI suggestion was correct was when it fixed the out of range error giving 
the incorrect "Too Low" hint. I verfied it by testing both 0 and 101, which were out of range, mutiple times to see if it worked correctly.
I also attempted to play the game as usual to see if the rest of the game worked. One example of an AI suggestion that didn't work
was fixing the hints pop on. Previosuly, you had to click the "Submit Guess" button twice for the correct hint to appear. However, because 
of the AI suggested change, it switched around the "Too Low" and "Too High" hints and removed an emoji. I manually fixed it and tested it through playing the game as normal to see if the hints were properly given. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I tested if a bug was truly fixed by testing the game multiple times in different situtations. For example, when testing
the "Out of Range" error, I tested many inputs outside of the 0 to 100 range, instead of just 0 and 101. Furthermore, I had 
basic in-range inputs like 23 or 60, to see if the game worked normally and repeated them after clicking the "New Game" button.
One test I ran with pytest was testing if the input was a number or not. When I ran the pytest, it came back functional, which
showed me that I should test for all edge cases and not just the intended output. As the test states "Guess a number between 1 and 100.", that means it should actually be a number. The AI helped me design certain edge cases like if the number inputted by the user was out of range or not with different difficulties. It used the numbers I tested from the Bug Reproduction Log to see if the "Out of Range" error occurred or not. While I still manually tested it, it helped remind me of what I needed to test and the different possibilities.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
