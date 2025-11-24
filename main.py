from ollama import chat
import json

with open("rules.json") as f:
    sys_rules = json.load(f)

sys_prompt = f"""
You are a patch-note writer. Follow the rules in this JSON object exactly:

{json.dumps(sys_rules, indent=2)}
"""

user_prompt = """
- added a crazy new game
- fixed an issue with users not being able to login
- removed all admins
"""


response = chat(
        model='llama3.1:8b',
        messages=[
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
)

print(response.message['content'])
