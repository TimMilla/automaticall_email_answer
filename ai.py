import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ.get("YOUR_API_KEY")
)

prompt = """You answer my mails automatically. Be nice and do not make any promises. The Mail:
\"\"\"
{0}
\"\"\"
"""

mail= "Hello World"

formatted_prompt= prompt.format(mail)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello World",
        }
    ],
    model="gpt-3.5-turbo",
)

