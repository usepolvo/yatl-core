# YATL Core

🦑 YATL (Yet Another Tentacle Language) is an innovative, octopus-themed markup language designed for defining and managing state machines. This repository contains the core specification and test suite for YATL.

## Repository Structure

- `specification/`: Contains the YATL language specification
- `test-suite/`: Houses the YATL test cases and expected outcomes
- `docs/`: Additional documentation including contribution guidelines

## Getting Started

To get started with YATL, please refer to the [specification](specification/yatl-spec.md).

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
