
import streamlit as st

from utils.utility import hit_backend

st.header("Online khabar news category classifier 📰")
st.markdown("This is a simple web application that classifies news article class based on the input from online khabar english.")
st.divider()
txt = st.text_area("Enter the news article text here to predict the category ...", height=200)
prediction_btn = st.button("Predict", type="primary")


if prediction_btn:
    if not txt:
        st.warning("Please write something.", icon="⚠️")
    else:
        response_dict = hit_backend(txt)
        st.success(f"The category of news article is {response_dict['category']}.", icon="✅")