# PDF-ChatGPT

A Python integrated with OpenAI project which answers questions related to your pdf, and if questions are asked outside your pdf it replies back with "I dont know".The steps involved in performing the project are:

1.def main():
    print('Hello,World!')


if __name__ == '__main__':
    main()
    Create a project and then a python file, write the code and check if the terminal shows Hello,World to test out your python file.

2.Download the dependecies for the project using pip for packages which are langchain, pypdf2, python-dotenv, tiktoken, faiss-cpu, openai by writing the following command:
  pip install [package_name]
If the pip doesnt work, write this command 
  python -m pip install [package_name]

3.Delete the print('Hello,World!') and paste the app.py code on the python file. Generate a OpenAI API key from the website https://platform.openai.com/account/api-keys and copy the api key and store it in .env file. Now, run the code by writing the command writing python -m streamlit run app.py, and there is your project which is displayed on the streamlit.




The basic understanding of the app.py can be understood from the comments which are written on every line in the app.py.But to understand the functioning properly, see this:

-Take the pdf, extract the context/data from the pdf, split it in chunks. Then the chunks are represented as embeddings or vectors. These vectors get stored in your knowledge base.Embeddings are the numeric representations of the text from the a file or source.The embeddings help us more conviently on processing the data mor effiecently and effectively.

-The question is asked from the user which performs a semantic search on the text embeddings.

-When the embedding or the chunk is found,we give these results to a AI language model which then provides the value to the user.We also calculate the cost involved to use OpenAI API to help us in finding these values for the user.
