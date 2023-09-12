import json
import os
import sys

from jsonschema import FormatChecker, Draft202012Validator
from schemas_declaration import schema_playstore


def validate_playstore(path_to_file: str):
    original_stdout = sys.stdout

    try:

        if not os.path.exists('validation_results'):
            os.mkdir('validation_results')

        f = open("validation_results/playstore_errors.txt", 'w')
        sys.stdout = f

        with open(path_to_file, 'r', encoding='utf-8') as pl:
            playstore_objects = [json.loads(line) for line in pl.readlines()]

        v = Draft202012Validator(
            schema_playstore, format_checker=FormatChecker())
        all_errors = []

        for _ in range(len(playstore_objects)):
            errors = sorted(v.iter_errors(
                playstore_objects[_]), key=lambda e: e.path)
            all_errors.append(errors)
        for _ in range(len(all_errors)):
            if all_errors[_]:
                print(f"Line {_ + 1}")
                for er_i, er in enumerate(all_errors[_]):
                    print(
                        f"\nError {er_i + 1}: {er.message}\nPath: {list(er.path)},")
                print('-' * 100)

        f.close()
        sys.stdout = original_stdout
        print(f"Validation of {path_to_file} completed.")

    except Exception as exp:
        sys.stdout = original_stdout
        print(f"Failed to validate {path_to_file}")
        print(exp)


if __name__ == '__main__':
    playstore_path = 'samples/playstore.jsonl'
    validate_playstore(playstore_path)
