from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
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
        input_variables=["task","language"]
    )

    code_chain = LLMChain(
        llm = llm,
        prompt = code_prompt,
        output_key = "code"
    )

    result_code = code_chain.invoke({
        "language": args.language,
        "task": args.task
        })
    
    print('\n------------------------- result_code --------------------------------\n')
    print(result_code)
    print('\n------------------------- result_code_END --------------------------------\n')


    test_prompt = PromptTemplate(
        template = "Write a test for the following {language} code:\n {code}",
        input_variables=["language", "code"]
    )
    
    test_chain = LLMChain(
        llm = llm,
        prompt = test_prompt,
        output_key = "test"
    )
    result_test = test_chain.invoke({
        "language": args.language,
        "code": result_code['code']
        })
    
    print('\n------------------------- result_test --------------------------------\n')
    print(result_test)
    print('\n------------------------- result_test_END --------------------------------\n')





    chain = SequentialChain(
        chains = [code_chain, test_chain],
        input_variables=["task","language"],
        output_variables = ["language","code", "test"]
    )

    result_chain = chain.invoke({
        "language": args.language,
        "task": args.task
        })
    
    print('\n------------------------- result_chain --------------------------------\n')
    print(result_chain)