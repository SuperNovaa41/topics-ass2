from ollama import chat
import json

with open("rules.json") as f:
    sys_rules = json.load(f)

sys_prompt = f"""
You are a patch-note writer. Follow the rules in this JSON object exactly:

{json.dumps(sys_rules, indent=2)}

YOU MUST FOLLOW THESE OUTPUT RULES:

1. OUTPUT ONLY VALID JSON.
2. DO NOT write explanations.
3. DO NOT write markdown.
4. DO NOT write section headers unless inside JSON fields.
5. The JSON schema MUST be:

{{
    "title": "string",
    "sections": {{
        "Features": ["string"],
        "Fixes": ["string"],
        "Removals": ["string"],
        "Security": ["string"]
    }},
    "version_request": {{"incremenet": "patch|minor|major"}},
    "date_request": "current_date"
}}

If a section has no entries, use an empty list.
NEVER hallucinate version numbers or dates.
NEVER output anything before or after the JSON.
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
