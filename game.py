import streamlit as st
import requests
from datetime import datetime
import random

# कंप्यूटर एक नंबर चुनता है (1 से 10 के बीच)
secret_number = random.randint(1, 10)

print("नमस्ते! मैंने 1 से 10 के बीच एक नंबर सोचा है।")
print("क्या आप बता सकते हैं कि वह कौन सा नंबर है?")

# यूज़र का इनपुट
guess = int(input("आपका अनुमान लिखें: "))

# चेक करना कि अनुमान सही है या नहीं
if guess == secret_number:
    print("बधाई हो! आपने बिल्कुल सही अनुमान लगाया।")
else:
    print(f"ओह! सही नंबर {secret_number} था। अगली बार कोशिश करें!")
