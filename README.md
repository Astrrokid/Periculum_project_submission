Periculum_project_submission/
│
├── data_in/
│   └── home_inventory.pdf
│
├── output_data/
│   └── home_inventory.json     
│
├── src/    
│   ├── extract_data.py
│   ├── inventory.py
│   ├── owner_info.py
│   ├── utils.py
│
├── main.py
├── README.md
├── requirements.txt


---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the main python script
#### - move the pdf file to the 'data_in/' folder 
```bash
mv path/to/the_pdf_file.pdf data_in/
```
#### - Run main.py
```bash
python main.py
```