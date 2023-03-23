# import os
# import openai
# from masked_ai import Masker

# # Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
# data = "My name is Adam and my IP address is 8.8.8.8. Now, write a one line poem:"
# masker = Masker(data)
# print('Masked: ', masker.masked_data)
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=masker.masked_data,
#     temperature=0,
#     max_tokens=1000,
# )
# generated_text = response.choices[0].text
# print('Raw response: ', response)
# unmasked = masker.unmask_data(generated_text)
# print('Result:', unmasked)