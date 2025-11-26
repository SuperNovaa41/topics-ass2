# Patch-note Generator

Generate a nicely JSON-formatted and organized patch notes from a list of quick bullet points!


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


[Demo Video](https://youtu.be/9fWKSfVWvsQ)


[Technical Note](./NOTE.md)
