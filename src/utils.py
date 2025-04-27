import pdfplumber
import os
import pickle
def get_data_from_pdf(path_to_pdf):
    with pdfplumber.open(path_to_pdf) as pdf:
        raw_text = ""
        for page in pdf.pages:
            raw_text += page.extract_text() + "\n"
    return raw_text

def align_content(raw_text):   
    return raw_text.split('\n')

def save_as_json(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

def find_pdf(folder_path):
    pdf_files = []
    filename = os.listdir(folder_path)[0]
    if filename.endswith(".pdf"):
        pdf_files.append(os.path.join(folder_path, filename))
    return pdf_files


