## Model:

Local / Ollama

App: CLI

App idea: Patch-note write: turn bullet changes into concise patch notes with a style goode (tool: date/version tagging)



Basic flow:


Input will either be piped in as a file containing patch notes as bullet points, or can write it through an input prompt within the app


The LLM will take these and format them according to the style guide

then will output it in some format that will be sent to a version/date tagger tool. (preferabbly in a json format, also i want the tool to be made by me)
