#importing dependencies 
import streamlit as st
from ai import output_data
import requests



#app name
st.title("Rack Data AI")

st.session_state.url = st.text_input("Input a Website URL:")   

    
st.session_state.browser = st.radio(label="Select Your Browser",   options=["Google", "Edge"], horizontal=True)

payload = { 'api_key': st.secrets["SCRAPER_API_KEY"], 'url': st.session_state.url, 'output_format': 'text', 'device_type': 'desktop' }


if st.button("Scrape/Analyze"):
    st.write("Scraping the site...")
    try:
        page_content = request.get('https://api.scraperapi.com/', params=payload)

        content = 
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.warning("Please check the URL and try again.")



