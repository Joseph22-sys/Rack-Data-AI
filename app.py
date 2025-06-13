#importing dependencies 
import streamlit as st
from ai import output_data
import requests



#app name
st.title("Rack Data AI")

st.session_state.url = st.text_input("Input a Website URL:")   

 
payload = { 'api_key': st.secrets["SCRAPER_API_KEY"], 'url': st.session_state.url, 'output_format': 'text', 'device_type': 'desktop' }


if st.button("Scrape/Analyze"):
    st.write("Scraping the site...")
    try:
        page_content = requests.get('https://api.scraperapi.com/', params=payload).text
        
        
        content = output_data(page_content)
        st.write(content)

        st.success("Scraping/Analysis complete d")
        
         
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.warning("Please check the URL and try again.")



