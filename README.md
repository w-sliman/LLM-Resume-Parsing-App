---
title: LLM Resume Parsing App
emoji: 🤗
colorFrom: indigo
colorTo: green
sdk: streamlit
sdk_version: "1.36.0"
app_file: app.py
pinned: true
---

# LLM Resume Parser APP

A job application form powered by a Large Language Model (LLM) Resume Parser using StreamLit, LangChain, Groq and LLAMA3.


This project combines `LangChain`, `StreamLit`, `Groq` and `LLAMA3`


## How it works:

Once applicant's upload their resume file (pdf or word), the resume text is extracted and sent to Groq API to LLAMA3 model. The model returned a `json blob` as prompted  and this data is automatically entered into the application form where the user can edit it or add to it.

## Notes

I included a variable called `job_title` and assigned it the value "Data Scientist", this variable is used in page title and on top of the page, more importantly, it's used in the llm model prompt to help the model pick skills  that are relevant to `job_title`. It possible to chang the job title or further more, include the full job description for evaluating and scoring resumes.<br>

I prefered to use an open source LLM as companies can host their own open source model and use it for resume parsing rather than having to rely on 3rd party providers which would help protect Applicants Data.

## Findings Throughout Development

One of the issues I encountered while testing was that the model would return a string date for dates like "December 2018" even when instructed to return a datetime string format. The reason, in addition to the imperfection of LLMs, is probably the long context as  the model has to extract a lot of data and is doing it all in one call to the API. The problem was solved after I instructed the model to return day, month and year instead.<br>

It was and still possible to divide the data extracting process to multiple parallel calls which would make it easier for the model as it would have to extract less data in each call. It would probably take 3 to 4 parallel calls.

## Final Comment

Thank you for taking the time to explore my code and looking forward to hearing your opinions and comments on the project.<br>

**Please take a look at code and live demo on the links below:**<br>

**Live Demo** on `Hugghingface` `Spaces`:

https://huggingface.co/spaces/w-sliman/LLM_Resume_Parser_App

`Github` Repo:

https://github.com/w-sliman/LLM-Resume-Parsing-App



