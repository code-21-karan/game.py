import streamlit as st
import random

st.title("Number Guessing Game")

# Agar koi number pehle se nahi hai, toh pehla number generate karo
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

st.write("नमस्ते! मैंने 1 से 100 के बीच एक नंबर सोचा है!")

# User input
guess = st.number_input("अपना अनुमान लिखें:", min_value=1, max_value=100, step=1)

# Game logic
if st.button("चेक करें"):
    if guess == st.session_state.secret_number:
        st.success("बधाई हो! आपने बिल्कुल सही अनुमान लगाया!")
    else:
        st.error(f"ओह! गलत! सही नंबर {st.session_state.secret_number} था।")

# "फिर से खेलें" button ka logic
if st.button("फिर से खेलें"):
    # Yaha naya number generate ho raha hai
    st.session_state.secret_number = random.randint(1, 100)
    st.rerun() # Yeh app ko refresh karega taaki naya number active ho jaye
