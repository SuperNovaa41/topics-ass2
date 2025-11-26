from ollama import chat
import json


class patch_note:
    def __init__(self):
        #self.model = "llama3.1:8b"
        self.model = "qwen2.5:7b"

        with open("rules.json") as f:
            sys_rules = json.load(f)

        good_ex = json.loads("{\"title\": \"Patch Notes - v{{version}} ({{date}})\", \"sections\": {\"Features\": [\"Added new leaderboard animations\"], \"Fixes\": [\"Fixed crash when opening settings\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")
        bad_ex = json.loads("{\"title\": \"Patch Notes - v1.0 (current_date)\", \"sections\": {\"Features\": [\"Reworked the item rarity system\"], \"Improvements\": [\"Improved keyboard navigation in menus\", \"Tweaked fog density in mountains\"], \"Fixes\": [\"Fixed double-jump exploit\"], \"Other\": [\"Added missing sound effects to combat\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")
        corrected_ex = json.loads("{\"title\": \"Patch Notes - v{{version}} ({{date}})\", \"sections\": {\"Features\": [\"Added missing sound effects to combat\"], \"Improvements\": [\"Reworked item rarity system\", \"Improved keyboard navigation in menus\", \"Tweaked fog density in mountains\"], \"Fixes\": [\"Fixed double-jump exploit\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")


        self.sys_prompt = f"""
        You are a patch-note writer. Follow the rules in this JSON object exactly:

        {json.dumps(sys_rules, indent=2)}

        BEFORE writing patch notes, first rewrite the user’s input bullets EXACTLY as "Parsed Input:".
        This step MUST contain all bullets, unchanged.
        Then write "Final Patch Notes:" and produce the template.

        If any bullet is missing, the answer is invalid — regenerate.


        Here are some examples:

        GOOD:
        Input:- added new leaderboard animations\n- fixed crash when opening settings
        Output: {json.dumps(good_ex)}
        BAD:
        Input:- reworked item rarity system\n- added missing sound effects to combat\n- improved keyboard navigation in menus\n- tweaked fog density in mountains\n- fixed double-jump exploit
        Output: {json.dumps(bad_ex)}
        Corrected: {json.dumps(corrected_ex)}



        YOU MUST INCLUDE EVERY USER BULLET EXACTLY ONCE.

        Do NOT drop any bullet.
        Do NOT merge bullets.
        Do NOT rewrite bullets beyond making them concise.
        DO NOT REWRITE BULLETS BEYOND MAKING THEM CONCISE.

        Make sure that if the example word matches one listed in classification rules, that it uses that exact section. YOU CONTINUE TO MISS THESE, ENSURE YOU DO IT CORRECTLY.

        DROP THE "-" ON THE OUTPUT.

        Version increment should always be patch, unless otherwise specified.

        Capitilize only the first letter of the first word of each sentence.
        Do not place periods at the end of sentences.
        DO NOT. PLACE PERIODS.

        If there are periods located in the sentence, the answer is invalid - regenerate.



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

        NEVER hallucinate version numbers or dates.
        NEVER output anything before or after the JSON.


        After following all of these rules, evaluate the output. If it does not strictly follow all of the rules above, regenerate.
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


