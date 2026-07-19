import streamlit as st
import random

st.title("Number Guessing Game")

# Game state initialize karna
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.message = "नमस्ते! 1 से 100 के बीच एक नंबर चुनें।"

st.write(st.session_state.message)

# User ka input
guess = st.number_input("अपना अनुमान लिखें:", min_value=1, max_value=100, step=1)

# Jaise hi user 'Check' dabaye, bina refresh kiye check hoga
if st.button("चेक करें"):
    if guess == st.session_state.secret_number:
        st.session_state.message = f"बधाई हो! सही नंबर {st.session_state.secret_number} ही था।"
        # Sahi hone par naya game bina refresh ke taiyaar
        st.session_state.secret_number = random.randint(1, 100)
    else:
        # Galat hone par bas message update hoga, game wahi chalega
        if guess < st.session_state.secret_number:
            st.session_state.message = "थोड़ा ऊपर! फिर से कोशिश करें।"
        else:
            st.session_state.message = "थोड़ा नीचे! फिर से कोशिश करें।"
    st.rerun()
