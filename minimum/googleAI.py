from langchain_google_genai import GoogleGenerativeAI
from configuration import configuration

def getResults():
    llm = GoogleGenerativeAI(model="models/text-bison-001")
    result = llm.invoke(configuration.googleai_api_prompt)
    print(result)