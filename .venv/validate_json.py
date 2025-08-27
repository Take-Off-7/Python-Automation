import json
from jsonschema import validate, ValidationError

with open("device-schema.json") as f:
    schema = json.load(f)

def validate_file(filename):
    with open(filename) as f:
        data = json.load(f)

    print(f"\nValidating {filename} ...")
    try:
        validate(instance=data, schema=schema)
        print(" JSON is valid")
    except ValidationError as e:
        print("Invalid JSON:", e.message)

validate_file("device.json")
validate_file("device-invalid.json")


