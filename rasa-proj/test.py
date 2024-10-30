import os
import openai
openai.organization = "org-Cj2t9ysorjWogKjfwU2TdN9O"
openai.api_key = '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'
response = openai.Completion.create(
model="text-davinci-002",
prompt="what do allstate do?",
temperature=0.9,
max_tokens=150,
    top_p=1,
frequency_penalty=0.0,
presence_penalty=0.6,
stop=[" Human:", " AI:"])
print(response['choices'][0]['text'])