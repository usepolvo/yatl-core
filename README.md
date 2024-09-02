# YATL Core

🦑 YATL (Yet Another Tentacle Language) is an innovative, octopus-themed markup language designed for defining and managing state machines and workflows. This repository contains the core specification and test suite for YATL.

## Current Version: 1.2

YATL 1.2 introduces exciting new features, including a trigger system for initiating workflows.

### New in YATL 1.2

- **Trigger System**: Define how workflows are initiated using HTTP, Webhook, Schedule, or Cloud Event triggers.
- **Enhanced Context**: Actions now have access to trigger-specific data.
- **Improved Task States**: Simplified state definitions for common tasks.

## Repository Structure

- `specification/`: Contains the YATL language specification
  - `yatl-spec.md`: The main specification file
  - `versions/`: Contains the YATL language spec versions
    - `yatl-spec-v1.0.md`: Original YATL 1.0 specification
    - `yatl-spec-v1.2.md`: Changelog for YATL 1.2
- `examples/`: Example YATL workflows
- `test-suite/`: Houses the YATL test cases and expected outcomes
- `docs/`: Additional documentation including contribution guidelines

## Getting Started

To get started with YATL, please refer to the [latest specification](specification/yatl-spec.md).

## Development Setup

To set up the development environment:

1. Ensure you have Python 3.9 or later and Make installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the root directory of the project in your terminal.
4. Run the setup command:
   ```
   make setup
   ```

This will create a virtual environment and install the necessary dependencies.

## Running Tests

To run the YATL tests on your local machine:

```
make test
```

## Other Make Commands

- `make clean`: Remove the virtual environment and cache files
- `make lint`: Run the linter
- `make docs`: Generate documentation (placeholder)
- `make help`: Show all available make commands

## Contributing

We welcome contributions! Please see our [contributing guidelines](docs/contributing.md) for more information.

## License

YATL is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to all the contributors who have helped shape YATL into what it is today. Your tentacles have reached far and wide!