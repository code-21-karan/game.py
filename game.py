import streamlit as st
import random

st.title("Number Guessing Game")

# Secret number generate karna (Session State use karna zaroori hai taaki number reload na ho)
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

st.write("नमस्ते! मैंने 1 से 10 के बीच एक नंबर सोचा है!")

# User input
guess = st.number_input("अपना अनुमान लिखें:", min_value=1, max_value=100, step=1)

if st.button("चेक करें"):
    if guess == st.session_state.secret_number:
        st.success("बधाई हो! आपने बिल्कुल सही अनुमान लगाया!")
       st.write (f"sahi jawab the {st.session_state, secret_number}")
    else:
        st.error(f"ओह! सही नंबर {st.session_state.secret_number} था। अगली बार कोशिश करें!")
        # Naya game shuru karne ke liye
        if st.button("फिर से खेलें"):
            st.session_state.secret_number = random.randint(1, 10)
            st.rerun()
