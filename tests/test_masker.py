# import os
# import openai
# from masked_ai import Masker

# # Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
# text = "Hello, my name is Adam, say my name"
# masker = Masker(text)
# # This sends "Hello, my name is <NamesMask_1>, say my name" to OpenAI
# # response = openai.Completion.create(model="text-davinci-003", prompt=masker.masked_data)
# unmask = masker.unmask_data(response)
# # This prints "Hello, Adam!"
# print('Result:', unmask)