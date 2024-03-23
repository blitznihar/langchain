import yaml

with open('config.yaml','r') as file:
    config = yaml.safe_load(file)


openai_api_prompt = config['development']['keys']['openai_api_prompt']
googleai_api_prompt = config['development']['keys']['googleai_api_prompt']