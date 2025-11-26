import json
from patch_note import patch_note
import difflib
import sys


with open("tests.json") as file:
    tests = json.load(file)

#print(json.dumps(tests, indent=2))

model = patch_note()


tests_ran = 0

total_tests = 15*5

tests_failed = 0
tests_passed = 0

for i in range(5):
    for _, value in tests.items():

        out = model.get_response(value["input"])
        parsed_out = json.dumps(json.loads(out))

        print(f"GENERATED: {parsed_out}")
        print(f"TEST: {value["output"]}")

        if parsed_out != value["output"]:
            print("FAIL!")
            tests_failed += 1
        else:
            print("PASS!")
            tests_passed += 1
        tests_ran += 1

        print(f"Tests passed: {tests_passed}/{total_tests}, Tests failed: {tests_failed}/{total_tests}")

