import streamlit as st
import random

st.title("Number Guessing Game")

# Secret number generate karna (1 se 100 tak)
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

st.write("नमस्ते! मैंने 1 से 100 के बीच एक number socha hai!")

# User input
guess = st.number_input("अपना अनुमान लिखें:", min_value=1, max_value=100, step=1)

if st.button("चेक करें"):
    if guess == st.session_state.secret_number:
        st.success("बधाई हो! आपने बिल्कुल सही अनुमान लगाया!")
        st.write(f"Sahi jawab tha: {st.session_state.secret_number}")
    else:
        st.error(f"ओह! गलत अनुमान।")
        st.write(f"Sahi jawab tha: {st.session_state.secret_number}")
        
        # Naya game shuru karne ke liye
        if st.button("फिर से खेलें"):
            st.session_state.secret_number = random.randint(1, 100)
            st.rerun()
