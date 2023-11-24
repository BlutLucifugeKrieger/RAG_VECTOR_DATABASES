import os

from langchain import PromptTemplate, OpenAI, LLMChain

os.environ["OPENAI_API_KEY"] = "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"


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What is at the core of Popper's theory of science?"

response = llm_chain.run(question)
print(response)

