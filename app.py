import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please enter the monthly sales target and selct the region")

st.number_input("Enter Monthly Sales Target (in USD):", 
                min_value = 0,
                max_value = 100000,
                value = 50000)
                
