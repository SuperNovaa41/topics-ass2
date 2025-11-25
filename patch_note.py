from ollama import chat
import json


class patch_note:
    def __init__(self):
        self.model = "llama3.1:8b"

        with open("rules.json") as f:
            sys_rules = json.load(f)


        self.sys_prompt = f"""
        You are a patch-note writer. Follow the rules in this JSON object exactly:

        {json.dumps(sys_rules, indent=2)}

        BEFORE writing patch notes, first rewrite the user’s input bullets EXACTLY as "Parsed Input:".
        This step MUST contain all bullets, unchanged.
        Then write "Final Patch Notes:" and produce the template.

        If any bullet is missing, the answer is invalid — regenerate.


        YOU MUST INCLUDE EVERY USER BULLET EXACTLY ONCE.

        Do NOT drop any bullet.
        Do NOT merge bullets.
        Do NOT rewrite bullets beyond making them concise.
        If unsure where to classify something, put it under the closest section.
        If a bullet does not fit any section, place it under "Other".


        YOU MUST FOLLOW THESE OUTPUT RULES:

        1. OUTPUT ONLY VALID JSON.
        2. DO NOT write explanations.
        3. DO NOT write markdown.
        4. DO NOT write section headers unless inside JSON fields.
        5. MUST follow the format rules for the bullet points. Ensure that the format rules are being follow EXACTLY.
        6. EVERY SINGLE PATCH NOTE MUST BE INCLUDED.
        7. Do not infer a date or a version.
        8. The JSON schema MUST be:

        {{
            "title": "string",
            "sections": {{
                "Features": ["string"],
                "Fixes": ["string"],
                "Removals": ["string"],
                "Security": ["string"],
                "Other": ["string"
            }},
            "version_request": {{"incremenet": "patch|minor|major"}},
            "date_request": "current_date"
        }}

        If a section has no entries, use an empty list.
        NEVER hallucinate version numbers or dates.
        NEVER output anything before or after the JSON.
        """


    def get_response(self, prompt) -> str:
        response = chat(
            model=self.model,
            messages=[
                {'role': 'system', 'content': self.sys_prompt},
                {'role': 'user', 'content': prompt}
            ]
        )
        out = response.message['content']

        return out[out.find('{'):]


