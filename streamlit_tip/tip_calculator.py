import streamlit as st

st.header("Welcome to the tip calculator!")
total_bill_in = st.text_input("What is the total bill? €")
if total_bill_in == "":
  total_bill = 0
else:
  try:
    total_bill = float(total_bill_in)
  except ValueError:
    st.write("This is not a valid input!")
    total_bill = 0
selection = [8, 10, 12, 15]
percentage = st.selectbox("What percentage tip would you like to give? 8, 10, 12 or 15? ", selection)
no_of_people_in = st.text_input("How many people to split the bill? ")
if no_of_people_in == "":
  no_of_people = 1
else:
  try:
    no_of_people = int(no_of_people_in)
  except ValueError:
    st.write("This is not a valid input!")
    no_of_people = 1

result_total = (total_bill + total_bill * percentage/100)
result =  result_total / no_of_people
st.write(f"The total amount is {round(result_total, 2)}.")
# rounded_result = round(result, 2)
rounded_result = "{:.2f}".format(result)

st.write(f"Each person should pay: ${rounded_result}")
