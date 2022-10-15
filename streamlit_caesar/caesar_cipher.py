import streamlit as st
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode": # this makes the program switch between encoding/decoding
        shift_amount *= 1   
    elif cipher_direction == "decode": # this makes the program switch between encoding/decoding
        shift_amount *= -1
    else:
        st.write("Das ist keine zulässige Eingabe!")
    for letter in start_text:
        if letter not in alphabet: 
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

st.write("Willkommen bei Florians Kodierungsprogramm!")
st.write("(auch bekannt unter dem Namen Caesar Cipher)")

# while True: 
direction = st.text_input("Schreibe 'encode' um zu kodieren, schreibe 'decode' um zu dekodieren:\n")
text = st.text_input("Schreibe deine Nachricht:\n").lower()
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
  # repeat = st.text_input("Willst du einen weiteren Text kodieren/dekodieren? Bitte schreibe 'ja' oder 'nein'. ")
  # if repeat == "ja":
  #   True
  # else: 
  #   st.write("Auf Wiedersehen!")
  #   break
    