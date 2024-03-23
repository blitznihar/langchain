# LangChain End to End
#### _Step to run the project_

Add Environment file. Create a .env file and add below configurations
```sh
OPENAI_API_KEY=""
GOOGLE_API_KEY=""
```
Fill the OPENAI_API_KEY and GOOGLE_API_KEY values

In the Terminal 
```sh
pipenv install
pipenv shell
```

Once the app is running type below command in the Terminal
```sh
python . --language javascript --task 'print hello world'
```