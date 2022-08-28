# Cryptocurrency Wallet

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0x8215d7733f11F9BC40f2C4EC2BA5c2411E39d975", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x38927C9F17A79c982387F9011F60B37C3c09A9B7", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x07D153A559B7f1fB39D473665ff7d8a5C1804891", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x82394C9a95E76e363f4c48D55b95D3c2a0Fe7De2", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

# Creates main streamlit page
def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")


# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Generate account instance
account = generate_account()

# Write the client's Ethereum account address and balance to the sidebar
st.sidebar.write('Address:', account.address)
st.sidebar.write('Balance:', get_balance(w3, address=account.address))

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write('Name:', candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write('Hourly Rate:', hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write('Candidate Address:', candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

# Calculating total wage to be paid and printing to streamlit
wage = hourly_rate * hours
st.sidebar.write('Total wage to be paid is',wage)

# Creating streamlit button to send transaction
if st.sidebar.button("Send Transaction"):

    # Calling the `send_transaction` function
    transaction_hash = send_transaction(w3, account=account, to=candidate_address, wage=wage)
    
    # Printing transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application & Writes FinTech Finder candidates to the Streamlit page
get_people(w3)