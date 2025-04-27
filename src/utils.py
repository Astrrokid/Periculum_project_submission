import pdfplumber
import os
import pickle

def get_data_from_pdf(path_to_pdf):
    """
    Extracts raw text from a PDF file.

    Args:
        path_to_pdf (str): The file path to the PDF.

    Returns:
        str: The extracted text from the PDF.
    """
    with pdfplumber.open(path_to_pdf) as pdf:
        raw_text = ""
        for page in pdf.pages:
            raw_text += page.extract_text() + "\n"
    return raw_text

def align_content(raw_text):
    """
    Splits the raw text into a list of lines.

    Args:
        raw_text (str): The text to be split into lines.

    Returns:
        list: A list of lines from the raw text.
    """
    return raw_text.split('\n')

def save_as_json(data, output_path):
    """
    Saves data to a JSON file using pickle for serialization.

    Args:
        data (object): The data to be serialized and saved.
        output_path (str): The file path where the data should be saved.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

def find_pdf(folder_path):
    """
    Finds the first PDF file in a given folder.

    Args:
        folder_path (str): The path to the folder to search for PDFs.

    Returns:
        list: A list containing the full path of the first PDF file found, or an empty list if no PDF is found.
    """
    pdf_files = []
    filename = os.listdir(folder_path)[0]
    if filename.endswith(".pdf"):
        pdf_files.append(os.path.join(folder_path, filename))
    return pdf_files
