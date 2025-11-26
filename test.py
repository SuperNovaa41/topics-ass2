import json
from patch_note import patch_note
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", required=False, default=False)
parser.add_argument("-i", "--iterations", required=False, default=1)

args = parser.parse_args()

with open("tests.json") as file:
    tests = json.load(file)

model = patch_note()


tests_ran = 0
total_tests = 15 * int(args.iterations)
tests_failed = 0
tests_passed = 0

for i in range(int(args.iterations)):
    for _, value in tests.items():

        out = model.get_response(value["input"])

        parsed_out = json.dumps(json.loads(out))

        if args.verbose:
            print(f"GENERATED: {parsed_out}")
            print(f"TEST: {value["output"]}")

        print(f"Test #{tests_ran}: ", end="")
        if parsed_out != value["output"]:
            print("FAIL!")
            tests_failed += 1
        else:
            print("PASS!")
            tests_passed += 1
        tests_ran += 1

        print(f"Tests passed: {tests_passed}/{total_tests}, Tests failed: {tests_failed}/{total_tests}")
print(f"Pass rate: {(tests_passed / total_tests) * 100}%")
