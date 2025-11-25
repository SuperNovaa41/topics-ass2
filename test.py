import json
from patch_note import patch_note

with open("tests.json") as file:
    tests = json.load(file)

#print(json.dumps(tests, indent=2))

model = patch_note()

for _, value in tests.items():

    out = model.get_response(value["input"])

    print(out)
    
    #print(value["output"])
    #print(json.dumps(json.loads(value["output"]), indent=4))

    exit(1)
