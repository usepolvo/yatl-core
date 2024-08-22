import json
import os
import sys

import yaml


def load_yatl(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def load_expected_outcome(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def validate_yatl(yatl_data, expected_outcome):
    errors = []

    if yatl_data["name"] != expected_outcome["name"]:
        errors.append(f"Name mismatch: expected {expected_outcome['name']}, got {yatl_data['name']}")

    if yatl_data["initial_state"] != expected_outcome["initial_state"]:
        errors.append(
            f"Initial state mismatch: expected {expected_outcome['initial_state']}, got {yatl_data['initial_state']}"
        )

    for transition in expected_outcome["transitions"]:
        from_state = yatl_data["states"][transition["from"]]
        if not any(
            t["event"] == transition["event"] and t["target"] == transition["to"] for t in from_state["transitions"]
        ):
            errors.append(f"Transition not found: {transition}")

    return errors


def run_tests():
    test_cases_dir = "test-suite/cases"
    expected_outcomes_dir = "test-suite/expected-outcomes"
    results = []

    for filename in os.listdir(test_cases_dir):
        if filename.endswith(".yatl"):
            yatl_path = os.path.join(test_cases_dir, filename)
            outcome_path = os.path.join(expected_outcomes_dir, filename.replace(".yatl", "_outcome.json"))

            yatl_data = load_yatl(yatl_path)
            expected_outcome = load_expected_outcome(outcome_path)

            errors = validate_yatl(yatl_data, expected_outcome)

            results.append({"test_case": filename, "passed": len(errors) == 0, "errors": errors})

    return results


if __name__ == "__main__":
    results = run_tests()

    # Print results
    for result in results:
        print(f"Test case: {result['test_case']}")
        print(f"Passed: {'Yes' if result['passed'] else 'No'}")
        if not result["passed"]:
            for error in result["errors"]:
                print(f"  - {error}")
        print()

    # Generate report file
    os.makedirs("test-results", exist_ok=True)
    with open("test-results/report.json", "w") as f:
        json.dump(results, f, indent=2)

    # Exit with non-zero status if any test failed
    if any(not result["passed"] for result in results):
        sys.exit(1)
