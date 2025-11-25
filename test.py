import json
from patch_note import patch_note
import difflib
import sys


with open("tests.json") as file:
    tests = json.load(file)

#print(json.dumps(tests, indent=2))

model = patch_note()

for _, value in tests.items():

    out = model.get_response(value["input"])
    print(json.dumps(json.loads(out)))

    print(value["output"])

    #sys.stdout.writelines(difflib.unified_diff(out, value["output"]))

    #print(value["output"])
    #print(json.dumps(json.loads(value["output"]), indent=4))

    exit(1)
