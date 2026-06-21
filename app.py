import random
import streamlit as st
import pandas as pd
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


def get_temperature(guess, secret, range_size):
    """Return 'hot', 'warm', or 'cold' based on distance from secret."""
    distance = abs(guess - secret)
    threshold_hot = range_size * 0.1  # Within 10% is hot
    threshold_warm = range_size * 0.25  # Within 25% is warm
    
    if distance <= threshold_hot:
        return "🔥 VERY HOT!"
    elif distance <= threshold_warm:
        return "🌡️ WARM"
    else:
        return "❄️ COLD"


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "show_hint" not in st.session_state:
    st.session_state.show_hint = True

st.subheader("Make a guess")

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    st.checkbox("Show hint", value=st.session_state.show_hint, key="show_hint")

# FIXME: Logic breaks here
# FIX: Refactored logic into app.py using agent mode
if new_game:
    st.session_state.attempts = 1
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = random.randint(low, high)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    # FIX: Refactored logic into app.py using agent mode
    # Validate guess is within range
    if ok and (guess_int < low or guess_int > high):
        ok = False
        err = f"Enter a number between {low} and {high}."

    if not ok:
        st.error(err)
    else:
        # Only increment attempts for valid, in-range guesses
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if st.session_state.show_hint:
            # Color-coded feedback
            if outcome == "Too High":
                st.error(message)
            elif outcome == "Too Low":
                st.success(message)
            else:  # Win
                st.success(message)
            
            # Show temperature (hot/cold) indicator
            range_size = high - low
            temperature = get_temperature(guess_int, st.session_state.secret, range_size)
            st.info(f"Temperature: {temperature}")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# Display game session summary table only when game ends
if st.session_state.status in ["won", "lost"]:
    st.divider()
    st.subheader("📊 Game Session Summary")

    if st.session_state.history:
        # Create summary data
        summary_data = []
        for idx, guess in enumerate(st.session_state.history, 1):
            range_size = high - low
            distance = abs(guess - st.session_state.secret)
            temperature = get_temperature(guess, st.session_state.secret, range_size)
            
            # Determine if guess was correct, too high, or too low
            if guess == st.session_state.secret:
                result = "✅ Correct"
            elif guess > st.session_state.secret:
                result = "⬇️ Too High"
            else:
                result = "⬆️ Too Low"
            
            summary_data.append({
                "Attempt": idx,
                "Guess": guess,
                "Result": result,
                "Distance": distance,
                "Temperature": temperature
            })
        
        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Display game stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Guesses", len(st.session_state.history))
        with col2:
            st.metric("Current Score", st.session_state.score)
        with col3:
            attempts_left = attempt_limit - st.session_state.attempts
            st.metric("Attempts Left", max(0, attempts_left))
    else:
        st.info("No guesses yet. Make your first guess to get started!")


st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
