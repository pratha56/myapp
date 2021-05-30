import streamlit as st

st.title('Classification Algorithms')
st.write("""
# Heading1
Which one is the best?
""")

value = st.number_input('Enter a number',None,None)
st.write(f'The value entered is {value}')
C = st.sidebar.slider('C', 0.01, 10.0)
st.write(f'The SLIDER value  is {C}')
