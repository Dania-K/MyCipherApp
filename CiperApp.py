

import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Dania's Cipher App")
st.write("Encrypt your text using the Caesar cipher. Begin by entering your preferred choice of text.  Begin by entering your preferred choice of text. Then, proceed to click the Encode button, and it runs before your eyes! If you wish to return back to the original text, enter the decrypted text to the text book. Click Decode to unmask the text.")

# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (1-25):", min_value=1, max_value=25, value=5)

# Button to encrypt
if st.button("Encode"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")

if st.button("Decode"):
    if text:
        decrypted_text = caesar(text, -shift)  # Use negative shift for decryption
        st.write('**Input text:**', text)
        st.write('**Decrypted text:**', decrypted_text)
    else:
        st.warning("Please enter a text to decrypt.")
