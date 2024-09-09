import streamlit as st
from scrape import (scrapeWebsite, splitDomContent, cleanBodyContent, extractBodyContent)

from parse import parseWithOllama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    st.write("Scraping Website")
    result = scrapeWebsite(url)
    bodyContent = extractBodyContent(result)
    cleanedContent = cleanBodyContent(bodyContent)
    
    st.session_state.domContent = cleanedContent
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleanedContent, height=300)
    
    
if "domContent" in st.session_state:
    parseDescription = st.text_area("Describe what you want to parse?")
    if st.button("Parse Content"):
        if parseDescription:
            st.write("Parsing the content")
            domChunks = splitDomContent(st.session_state.domContent)
            result = parseWithOllama(domChunks, parseDescription)
            st.write(result)
            
            