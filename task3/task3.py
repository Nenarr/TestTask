import json
import sys

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)


def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)


    with open(report_path, 'w') as report_file:
        json.dump(tests_data, report_file, indent=4)


if __name__ == "__main__":
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)