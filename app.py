import streamlit as st
st.write('#streamlit calculator')

number1 = st.number_input('number 1')
number2 = st.number_input('number 2')
number3 = number1 + number2

st.write('# Answer is', number3)