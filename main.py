import streamlit as st
from scrape import scrapeWebsite

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    st.write("Scraping Website")
    result = scrapeWebsite(url)
    print(result)