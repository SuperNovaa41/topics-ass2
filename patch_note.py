from ollama import chat
import json

#You must rewrite bullets only to make them concise.


prompt = f"""
You are a strict patch-note generator.
You must ALWAYS output valid JSON matching the schema.
You must NEVER output anything before or after the JSON.
You must categorize items based on keywords.
You must not add periods.
You must include every bullet exactly once.
You must not infer version or date.
Version increment is always "patch" unless specified.
You must NEVER output empty lists in the JSON.
You must ALWAYS capitalize the first letter of each bullet and lowercase the rest unless it is a proper noun or an acronym.

"""

schema = f"""
The JSON you output MUST match this structure exactly, except in cases where sections are missing items:

{{
    "title": "Patch Notes - v{{{{version}}}} ({{{{date}}}})",
    "sections": {{
        "Features": ["string"],
        "Improvements": ["string"],
        "Fixes": ["string"],
        "Removals": ["string"],
        "Security": ["string"],
        "Other": ["string"]
    }},
    "version_request": {{"increment": "path|minor|major"}},
    "date_request": "current_date"
}}

If the bullet contains 'added', 'new', 'introduced', 'implemented', 'created', categorize as Features
If the bullet contains 'reworked', 'improved', 'enhanced', 'made faster', 'optimized', 'refined', 'updated', 'reworked', 'tweaked', categorize as Improvements
If the bullet contains 'fixed', 'resolved', 'addressed', 'corrected', categorize as Fixes
If the bullet contains 'removed', 'deleted', 'deprecated', 'incompatible', categorize as Removals
If the bullet contains 'vulnerability', 'hardened', 'xss', 'csrf', 'permission issue', categorize as Security
Do not guess, do not infer meaning, only use these keyword mappings.
"""

task = f"""
TASK:
    First output "Parsed Input:" followed by the exact user bullets.

    Then output "Final Patch Notes:" and produce the JSON.

    All bullets must follow this exact casing style:

    Correct: "Added new lighting system"
    Incorrect: "Added New Lighting System"
    Incorrect: "Added new Lighting System"
    Incorrect: "added new lighting system"

    Always use sentence case exactly like the first example.
    If it doesn't follow this exact casing style, regenerate.

    Do NOT output any empty lists in the JSON.
    Do NOT modify the bullets beyond capitalization.
    Do NOT add or remove anything.
    Do NOT add periods.
    Do NOT change the schema.
    Do NOT infer version or date.
    Do NOT rearrange the sections.

    USER BULLETS:\n
"""

class patch_note:
    def __init__(self):
        #self.model = "llama3.1:8b"
        #self.model = "qwen2.5:7b"
        #self.model = "qwen2.5:7b-instruct"
        self.model = "gpt-oss:120b-cloud"

        with open("rules.json") as f:
            sys_rules = json.load(f)

        #good_ex = json.loads("{\"title\": \"Patch Notes - v{{version}} ({{date}})\", \"sections\": {\"Features\": [\"Added new leaderboard animations\"], \"Fixes\": [\"Fixed crash when opening settings\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")
        #bad_ex = json.loads("{\"title\": \"Patch Notes - v1.0 (current_date)\", \"sections\": {\"Features\": [\"Reworked the item rarity system\"], \"Improvements\": [\"Improved keyboard navigation in menus\", \"Tweaked fog density in mountains\"], \"Fixes\": [\"Fixed double-jump exploit\"], \"Other\": [\"Added missing sound effects to combat\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")
        #corrected_ex = json.loads("{\"title\": \"Patch Notes - v{{version}} ({{date}})\", \"sections\": {\"Features\": [\"Added missing sound effects to combat\"], \"Improvements\": [\"Reworked item rarity system\", \"Improved keyboard navigation in menus\", \"Tweaked fog density in mountains\"], \"Fixes\": [\"Fixed double-jump exploit\"]}, \"version_request\": {\"increment\": \"patch\"}, \"date_request\": \"current_date\"}")


        #self.sys_prompt = f"""
        """
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
        Corrected example: {json.dumps(corrected_ex)}



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

        self.sys_prompt = prompt
        self.schema = schema
        self.task = task


    def get_response(self, prompt) -> str:
        response = chat(
            model=self.model,
            messages=[
                {'role': 'system', 'content': self.sys_prompt},
                {'role': 'user', 'content': f"{self.schema}\n{self.task}\n{prompt}"}
            ]
        )
        out = response.message['content']

        return out[out.find('{'):]


