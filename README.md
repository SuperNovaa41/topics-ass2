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
Telemetry: log per request: timestamp, pathway (RAG/tool/none), latency, and (if available) tokens/cost. -- DONE
Offline eval: a tests.json with ≥15 inputs + expected patterns; a script that runs them and prints a pass rate. -- DONE
Repro: README.md, requirements.txt/environment.yml, .env.example, seed data, and a one-command run.



# Patch-note Generator

## Dependencies

- `ollama`
- `python3`


As well, ensure you install the python libraries needed using `pip install -r requirements.txt`


## Available tools

`SETUP.sh`


- This will pull the required ollama model that this application uses, also prompts you to log in, as it is a cloud model.


`gen_patch_notes.py`


- A one-command run script for interacting with the patch note generator.
- `-f`/`--filename` allows you to pipe a file for the prompt input. Otherwise, will use user entry.
- `-o`/`--output` allows you to change the name/destination of the file it outputs the json to. Defaults to `parsed_notes.json`.
- Also implements a version and date tagger tool which will automatically increment the version and tag the date of the release.
    - The version can be set in the `current_version` file, which is generated upon first run.
    - The patch note generator will automatically tag each update as a patch, but upon specifying, can tag as a major or minor update aswell.


`patch_note.py`


- The file where the patch note generator class is located, this can be implemented into your programs freely as you wish.



### Testing Suite

`run_tests.py`

- Runs a series of tests to ensure that the output of the LLM is following the desired pattern and formatting correctly.
- `-v`/`--verbose` provides a verbose print mode, allowing you to see the output of the generator, and the desired outcome its being compared to (these are all available in tests/tests.json). Defaults to false.
- `-i`/`--iterations` for every iterations it will run the 15 unit tests, allowing you to stress test the system. Defaults to 1.



## Deliverables


[https://youtu.be/9fWKSfVWvsQ](Demo Video)

[./NOTE.md](Technical note)
