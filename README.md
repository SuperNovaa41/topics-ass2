## Model:

Local / Ollama

App: CLI

App idea: Patch-note write: turn bullet changes into concise patch notes with a style goode (tool: date/version tagging)



Basic flow:


Input will either be piped in as a file containing patch notes as bullet points, or can write it through an input prompt within the app


The LLM will take these and format them according to the style guide

then will output it in some format that will be sent to a version/date tagger tool. (preferabbly in a json format, also i want the tool to be made by me)


Core feature: at least one real user flow that calls an LLM. -- DONE
One enhancement (pick exactly one): -- DONE
    Tool use: call 1 external API (e.g., weather, search, calendar) from the LLM’s output. -- DONE
Safety/robustness:
    A system prompt with explicit do/don’t rules. -- DONE
    Input length guard + error fallback message. -- DONE
    Basic prompt-injection check (e.g., refuse “ignore previous instructions”). -- DONE
Telemetry: log per request: timestamp, pathway (RAG/tool/none), latency, and (if available) tokens/cost.
Offline eval: a tests.json with ≥15 inputs + expected patterns; a script that runs them and prints a pass rate. -- DONE
Repro: README.md, requirements.txt/environment.yml, .env.example, seed data, and a one-command run.



