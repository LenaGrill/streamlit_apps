import streamlit as st
# import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode": # this makes the program switch between encoding/decoding
        shift_amount *= 1   
    elif cipher_direction == "decode": # this makes the program switch between encoding/decoding
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet: # any character that is not in the alphabet will not be encrypted and stays the same
            new_letter = letter
        else:
            position = alphabet.index(letter) # gets the index of the character in the alphabet
            shifted_position = position + shift_amount # returns the index of the new, encoded character
            #print(shifted_position)
            new_position = shifted_position % len(alphabet) # this is to avoid index error due to index out of range
            new_letter = alphabet[new_position]
            #print(new_char)
        end_text += new_letter
    
    st.write(f"Hier ist dein '{cipher_direction}' Resultat: {end_text}")

# prints the start logo
# st.write(art.logo)

st.header("Willkommen bei Florians Kodierungsprogramm!")
st.write("(Kodierung auch bekannt unter dem Namen Caesar Cipher)")

selection = ["encode", "decode"]
direction = st.selectbox( "Wähle 'encode' um zu kodieren oder 'decode' um zu dekodieren: ", selection)
text = st.text_input("Schreibe deine Nachricht:\n") # .lower()
shift_in = st.text_input("Gib die Kodierungszahl ein:\n")
if shift_in == "":
  shift = 0
else:
  try:
    shift = int(shift_in)
  except ValueError:
    st.write("Das ist keine zulässige Eingabe!")
    shift = 0
      

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    