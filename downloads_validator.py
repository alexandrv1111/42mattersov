import json
import sys
import os

from jsonschema import FormatChecker, Draft202012Validator
from schemas_declaration import schema_downloads


def validate_downloads(path_to_file: str):
    original_stdout = sys.stdout

    try:

        if not os.path.exists('validation_results'):
            os.mkdir('validation_results')

        with open(path_to_file, encoding='utf-8') as df:
            d = json.load(df)
        downloads_validator = Draft202012Validator(
            schema_downloads, format_checker=FormatChecker())
        errors = sorted(downloads_validator.iter_errors(d),
                        key=lambda e: e.path)

        f = open("validation_results/downloads_errors.txt", 'w')
        sys.stdout = f

        for error in errors:
            print(error.message, f"\nPath is {list(error.path)}")
            print('-' * 100)

        f.close()

        sys.stdout = original_stdout
        print(f"Validation of {path_to_file} completed.")

    except Exception as exp:
        sys.stdout = original_stdout
        print(f"Failed to validate {path_to_file}")
        print(exp)


if __name__ == '__main__':
    downloads_path = 'samples/downloads.json'
    validate_downloads(downloads_path)
