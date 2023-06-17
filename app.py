#The place where our application is being made
from dotenv import load_dotenv      #loads the environment variable from the environment file
import streamlit as st              #a platform to show your ML and data science web apps
from PyPDF2 import PdfReader        #PyPDF2 is used to work with pdfs whereas PdfReader is used to read PDF
from langchain.text_splitter import CharacterTextSplitter       #a class which is being imported responsible for splitting texts in chunks
from langchain.embeddings.openai import OpenAIEmbeddings        #to produce embeddings on the chunks
from langchain.vectorstores import FAISS                        #a library which consists of algorithms for varrious operations
from langchain.chains.question_answering import load_qa_chain   #a package used for answering questions 
from langchain.llms import OpenAI                               #calls the OpenAi Algorithm
from langchain.callbacks import get_openai_callback             #calls get_openai_callback to calculate the total cost incurred for executing a line of code which uses the OpenAI API

text = ""                                                           #to create a new text variable
def main():                                                         #the main method
    load_dotenv()                                                   #loads the API key from the environment file
    st.set_page_config(page_title="Ask about your PDF")             #in streamlit the title of the page
    st.header("Ask about your PDF ")                                #gives the text-header
    pdf = st.file_uploader("Upload the required PDF", type="pdf")   #gives an option to the user to upload the image with a text saying Upload the required PDF
    global text                                                     #using the global keyword to allow modifications to the variable text
    
    if pdf is not None:                         #to perform the steps if a pdf is being uploaded
        pdf_reader = PdfReader(pdf)             #to read the pdf and store the pdf in pdf_reader                            
        for page in pdf_reader.pages:           #going through every page in the pdf
            text += page.extract_text()         #to extract the text from each page and store it in text

        text_splitter = CharacterTextSplitter(      #calls the class CharacterTextSplitter
            separator="\n",                         #in the chunk if there is a new line its considered as a new line and the new line is removed
            chunk_size=1000,                        #each chunk has 1000 words 
            chunk_overlap =200,                     #every chunk has 200 words from the previous chunk
            length_function=len                     #used to calculate the length of each chunk
        )
        chunks = text_splitter.split_text(text)     #we call the split_text function which splits the text into chunks whose characteristics are present in the text_splitter

        embeddings = OpenAIEmbeddings()                             #produce embeddings on the chunks of data by calling OpenAIEmbeddings
        knowledge_base = FAISS.from_texts(chunks, embeddings)       #takes the embeddings and puts it in the knowledge base

        user_question = st.text_input("Ask a question about your PDF:")        #displays it on the screen of the streamlit after the pdf is uploaded
        if user_question:                                                      #if there is content present,then proceed
            docs = knowledge_base.similarity_search(user_question)             #perform a semantic search/similiarity test on the embeddings in the knowledge base and stores the result in docs
            
            llm = OpenAI()                                                          #different langauge models can be used to solve the problem, but we use OpenAI in this case
            chain = load_qa_chain(llm, chain_type="stuff")                          #used for loading the llm algorithm on the chain variable
            with get_openai_callback() as cb:                                       #this function is used to tell the numbers of token used and total cost for the running the next statement
                response = chain.run(input_documents=docs, question=user_question)  #runs the llm algorithm by calling chain on the document docs with the user_question
                print(cb)                                                           #prints out value of the callback function on the terminal which has the values of total cost incurred and number of token used
                
            st.write(response)                                                      #prints on the response on the streamlit screen



if __name__ == '__main__':                                                          #calls the main method
    main()
