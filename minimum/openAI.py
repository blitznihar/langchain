from langchain_openai import OpenAI

from configuration import configuration


def getResults():
    llm = OpenAI()
    result = llm.invoke(configuration.openai_api_prompt)
    print(result)