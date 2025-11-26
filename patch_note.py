from ollama import chat

prompt = """
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

schema = """
The JSON you output MUST match this structure exactly, except in cases where sections are missing items:

{
    "title": "Patch Notes - v{{version}} ({{date}})",
    "sections": {
        "Features": ["string"],
        "Improvements": ["string"],
        "Fixes": ["string"],
        "Removals": ["string"],
        "Security": ["string"],
        "Other": ["string"]
    },
    "version_request": {"increment": "patch|minor|major"},
    "date_request": "current_date"
}}

If the bullet contains 'added', 'new', 'introduced', 'implemented', 'created', categorize as Features
If the bullet contains 'reworked', 'improved', 'enhanced', 'made faster', 'optimized', 'refined', 'updated', 'reworked', 'tweaked', categorize as Improvements
If the bullet contains 'fixed', 'resolved', 'addressed', 'corrected', categorize as Fixes
If the bullet contains 'removed', 'deleted', 'deprecated', 'incompatible', categorize as Removals
If the bullet contains 'vulnerability', 'hardened', 'xss', 'csrf', 'permission issue', categorize as Security
Do not guess, do not infer meaning, only use these keyword mappings.
"""

task = """
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
        self.model = "gpt-oss:120b-cloud"

        self.sys_prompt = prompt
        self.schema = schema
        self.task = task

    def get_response(self, prompt) -> str:
        response = chat(
            model=self.model,
            messages=[
                {'role': 'system', 'content': self.sys_prompt},
                {'role': 'user', 'content':
                    f"{self.schema}\n{self.task}\n{prompt}"}
            ]
        )
        out = response.message['content']

        return out[out.find('{'):]
