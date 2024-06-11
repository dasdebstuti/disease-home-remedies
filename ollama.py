from langchain import PromptTemplate
from langchain_community.llms import Ollama


class OllamaModelForDisease:
    def __init__(self):
        # Ollama LLM
        self.llm = Ollama(model='llama3')
        self.prompt = PromptTemplate.from_template("Give response for following question: {question}. Give easy to "
                                              "understand responses. Your responses should be in {language}")



    def invoke(self, disease_name):
        # create the prompt, here we use multiple inputs

        cause_query = f'causes of {disease_name}'
        symptom_query = f'symptoms of {disease_name}'
        remedies_query = f'remedies for {disease_name}'
        harmful_food_query = f'harmful foods for {disease_name}'
        beneficial_food_query = f'beneficial foods for {disease_name}'

        queries = [cause_query, symptom_query, remedies_query, harmful_food_query, beneficial_food_query]
        answers = []

        for query in queries:
            # format the prompt to add variable values
            prompt_formatted_str: str = self.prompt.format(
                question=query,
                language="English")

            # make a prediction
            answers.append(self.llm.predict(prompt_formatted_str))
        return answers


