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

    for key in ["name", "description", "version", "initial_state"]:
        if yatl_data.get(key) != expected_outcome.get(key):
            errors.append(f"{key.capitalize()} mismatch: expected {expected_outcome.get(key)}, got {yatl_data.get(key)}")

    if "triggers" in expected_outcome:
        if "triggers" not in yatl_data:
            errors.append("Triggers section missing in YATL data")
        else:
            for expected_trigger in expected_outcome["triggers"]:
                if not any(t["type"] == expected_trigger["type"] and t.get("cron") == expected_trigger.get("cron") for t in yatl_data["triggers"]):
                    errors.append(f"Trigger not found: {expected_trigger}")

    for expected_state in expected_outcome["states"]:
        if expected_state["name"] not in yatl_data["states"]:
            errors.append(f"State not found: {expected_state['name']}")
        else:
            yatl_state = yatl_data["states"][expected_state["name"]]
            if yatl_state.get("type") != expected_state.get("type"):
                errors.append(f"State type mismatch for {expected_state['name']}: expected {expected_state.get('type')}, got {yatl_state.get('type')}")
            if yatl_state.get("action") != expected_state.get("action"):
                errors.append(f"State action mismatch for {expected_state['name']}: expected {expected_state.get('action')}, got {yatl_state.get('action')}")
            if yatl_state.get("next") != expected_state.get("next"):
                errors.append(f"State next mismatch for {expected_state['name']}: expected {expected_state.get('next')}, got {yatl_state.get('next')}")

    for expected_action in expected_outcome["actions"]:
        if expected_action["name"] not in yatl_data["actions"]:
            errors.append(f"Action not found: {expected_action['name']}")
        else:
            yatl_action = yatl_data["actions"][expected_action["name"]]
            if yatl_action.get("description") != expected_action.get("description"):
                errors.append(f"Action description mismatch for {expected_action['name']}")
            if yatl_action.get("language") != expected_action.get("language"):
                errors.append(f"Action language mismatch for {expected_action['name']}")

    yatl_variables = set(yatl_data["variables"].keys())
    expected_variables = set(v["name"] for v in expected_outcome["variables"])
    if yatl_variables != expected_variables:
        errors.append(f"Variables mismatch: expected {expected_variables}, got {yatl_variables}")

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