from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("--language", default="python")
parser.add_argument("--task", default="return a list of numbers")
args = parser.parse_args()

def getResults():
    llm = OpenAI()

    code_prompt = PromptTemplate(
        template = "Write a very short {language} function that will {task}",
        input_variables=["language", "task"]
    )
    code_chain = LLMChain(
        llm = llm,
        prompt = code_prompt
    )

    
    result = code_chain.invoke({
        "language": args.language,
        "task": args.task
        })
    #llm.invoke("write a simple haiku.")
    print(result["text"])
