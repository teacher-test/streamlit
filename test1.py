import streamlit as st

col1, col2 = st.columns([2, 3])
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])
with col1 :
    st.title("here is column1 title")
    

with col2 :
    st.title("here is column2 title")
    st.checkbox("this is checkbox1 in col2 ")

col1.subheader("i am column1 subheader")
col2.checkbox("this i checkbox2 in col2")

with tab1 :
        st.write('hello111111111111111111ㄴㄴ1111111111111111111111111111111111111111111111111111111111111111111111')
with tab2 :
        st.write("hi")