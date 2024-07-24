import PyPDF2
import docx
import io
import datetime
from components.candidate_data_schema import candidate
import re

def read_pdf_text(resume_file):
    """
    Extracts text from a PDF file.

    Args:
        resume_file (file-like object): The PDF file to be read.

    Returns:
        str: The extracted text from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(resume_file.read()))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text().strip()
    return text


def read_docx_text(word_file):
    """
    Extracts text from a DOCX file.

    Args:
        word_file (file-like object): The DOCX file to be read.

    Returns:
        str: The extracted text from the DOCX file.
    """
    doc = docx.Document(io.BytesIO(word_file.read()))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text.strip() + "\n"
    return text


def extract_resume_text(resume_file):
    """
    Extracts text from a resume file, either PDF or DOCX.

    Args:
        resume_file (file-like object): The resume file to be read.

    Returns:
        str: The extracted text from the resume file.
    """
    file_type = resume_file.name.split(".")[-1]
    if file_type == "pdf":
        return read_pdf_text(resume_file)
    elif file_type == "docx":
        return read_docx_text(resume_file)


def date_to_datetime(input):
    """
    Converts a dictionary representing a date to a datetime.date object.

    Args:
        input (dict): Dictionary with keys 'year', 'month', 'day'.

    Returns:
        datetime.date or None: The corresponding datetime.date object or None if input is invalid.
    """
    for _, value in input.items():
        if value is None:
            return None
        
    return datetime.date(**input)


def convert_dates_to_datetime(candidate_data: candidate):
    """
    Returns the model_dump() dictionary of a "candidate" pydantic class after converting dates to datetime.date objects.

    Args:
        candidate_data (candidate): The candidate object containing date fields.

    Returns:
        dict: The candidate model_dump dictionary with date fields converted to datetime.date objects.
    """
    candidate_dict = candidate_data.model_dump()
    
    if "degrees" in candidate_dict.keys():
        for degree in candidate_dict["degrees"]:
            if degree["graduation_date"]:
                degree["graduation_date"] = date_to_datetime(degree["graduation_date"])
    
    if "jobs" in candidate_dict.keys():
        for job in candidate_dict["jobs"]:
            if job["started_at"]:
                job["started_at"] = date_to_datetime(job["started_at"])
            if job["ended_at"]:
                job["ended_at"] = date_to_datetime(job["ended_at"])

    return candidate_dict


def is_valid_email(email):
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None