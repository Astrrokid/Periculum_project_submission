import os
from src.utils import get_data_from_pdf, align_content, save_as_json, find_pdf
from src.extract_data import extract_data

input_dir_name = "data_in"
output_dir_name = "output_data"

def run_pipeline(path_to_pdf):
    """
    Runs the entire pipeline for processing a PDF file:
    - Extracts text from the PDF.
    - Aligns the extracted content into a structured format.
    - Processes the aligned content to generate a response.
    - Saves the response as a JSON file.

    Args:
        path_to_pdf (str): The path to the PDF file to be processed.
    """
    raw_text = get_data_from_pdf(path_to_pdf)
    aligned_content = align_content(raw_text)
    response_json_str = extract_data(aligned_content)
    output_json_basename = os.path.basename(path_to_pdf.replace('.pdf', '.json'))
    output_json_path = os.path.join(output_dir_name, output_json_basename)
    save_as_json(response_json_str, output_json_path)
    print(f"Saved JSON to {output_json_path}")

if __name__ == "__main__":
    path_to_input_pdf = find_pdf(input_dir_name)[0]
    run_pipeline(path_to_input_pdf)
