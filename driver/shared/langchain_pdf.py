from langchain_google_genai import ChatGoogleGenerativeAI
from functions import  load_pdf_from_file
import os 

def summarize(file_path , context_base = "summarize the following lec slide and transcript text" ):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    base_name = os.path.basename(file_path)
    pages = load_pdf_from_file(file_path=file_path)
    trans_file = os.path.join("/home/pk/Desktop/dbms/Transcripts/Week 3/", base_name)
    transcript = load_pdf_from_file(trans_file)
    # Setup the Google Generative AI model and invoke it using a human-friendly prompt
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    result = llm.invoke(f"{context_base}: \n {pages}: \n {transcript}")

    return result.content
