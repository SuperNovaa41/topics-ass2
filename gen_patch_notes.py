from patch_note import patch_note
from tools.tagging import tagger
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", required=False)
parser.add_argument("-o", "--output", required=False, default="parsed_notes.json")

args = parser.parse_args()

prompt = ""

if args.filename:
    with open(args.filename, "r",) as file:
        prompt = file.read()
else:
    print("Input bulleted patch notes, separated by line:")

    while True:
        try:
            line = input()
            prompt += line + "\n"
        except EOFError:
            break

print("Generating patchnotes...")

model = patch_note()
out = model.get_response(prompt)
json_out = json.loads(out)

tag = tagger()

json_out["title"] = tag.tag(json_out["title"],
                            json_out["version_request"]["increment"])

with open(args.output, "w") as file:
    json.dump(json_out, file, indent=4)

print(f"Saved the following to {args.output}:")
print(json.dumps(json_out, indent=4))
