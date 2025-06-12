#importing dependencies 
import streamlit as st
from edge_scrape import scrape_edge_website
from chrome_scrape import scrape_chrome_website,parse_html
from ai import output_data



#app name
st.title("Rack Data AI")

st.session_state.url = st.text_input("Input a Website URL:")   

    
st.session_state.browser = st.radio(label="Select Your Browser",   options=["Google", "Edge"], horizontal=True)



if st.button("Scrape/Analyze"):
    st.write("Scraping the site...")
    try:
        if st.session_state.browser == "Google":
            site_data = scrape_chrome_website(st.session_state.url)
            page_content = parse_html(site_data)
            
            st.write(output_data(page_content))
            
            
        elif st.session_state.browser == "Edge":
            site_data = scrape_edge_website(st.session_state.url)
            
        
        st.success("Scraping completed successfully!")    
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.warning("Please check the URL and try again.")



