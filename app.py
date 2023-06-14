#The place where our application is being made
from dotenv import load_dotenv      #loads the environment variable from the environment file
import streamlit as st              #a platform to show your ML and data science web apps
from PyPDF2 import PdfReader        #PyPDF2 is used to work with pdfs whereas PdfReader is used to read PDF

def main():
    load_dotenv()                                                   #loads the API key from the environment file
    st.set_page_config(page_title="Ask about your PDF")             #in streamlit the title of the page
    st.header("Ask about your PDF ")                                #gives the text-header
    pdf = st.file_uploader("Upload the required PDF", type="pdf")   #gives an option to the user to upload the image with a text saying Upload the required PDF

    if pdf is not None:                         #to perform the steps if a pdf is being uploaded
        pdf_reader = PdfReader(pdf)             #to read the pdf and store the pdf in pdf_reader
        text = ""                               #to create a new text variable
        for page in pdf_reader.pages:           #going through every page in the pdf
            text += page.extract_text()         #to extract the text from each page and store it in text
                                                #a line gap to show the end of the for loop
        st.write(text)                          #write all the text from the pages into the streamlit


   
if __name__ == '__main__':
    main()
