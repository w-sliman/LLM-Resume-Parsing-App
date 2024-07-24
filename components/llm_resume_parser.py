from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from components.candidate_data_schema import candidate
from components.llm_model import llm

parser = PydanticOutputParser(pydantic_object=candidate)

prompt_template = """\
You are tasked with extracting data from resume for a {job_title} job and retruning a JSON structre.\n
{format_instructions}\n

Resume text: {resume_text}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["job_title", "resume_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm_resume_parser = prompt | llm | parser

