from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0, model_name="llama3-8b-8192", model_kwargs={"response_format": {"type": "json_object"}})
