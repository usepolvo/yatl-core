# Contributing to YATL Core

We welcome contributions to the YATL Core repository! Here are some guidelines to help you get started.

## Reporting Issues

- Use the GitHub issue tracker to report bugs or suggest enhancements.
- Before creating a new issue, please check if a similar issue already exists.

## Development Setup

1. Fork the repository and clone it to your local machine.
2. Ensure you have Python 3.9 or later and Make installed.
3. Set up the development environment:
   ```
   make setup
   ```

## Submitting Changes

1. Create a new branch for your feature or bug fix.
2. Make your changes, following the YATL specification and coding standards.
3. Write or update tests as necessary.
4. Run the tests locally to ensure your changes don't break existing functionality:
   ```
   make test
   ```
5. Run the linter to check for any code style issues:
   ```
   make lint
   ```
6. Update documentation to reflect your changes.
7. Submit a pull request with a clear description of your changes.

## Coding Standards

- Follow the existing code style and conventions used in the repository.
- Write clear, concise comments and documentation.

## Testing

- Add relevant test cases to the `test-suite/cases/` directory.
- Create corresponding expected outcomes in the `test-suite/expected-outcomes/` directory.
- Ensure all existing tests pass before submitting your changes.

## Documentation

If you've made changes that require documentation updates, please update the relevant files in the `docs/` directory. You can generate the documentation (when implemented) using:
```
make docs
```

Thank you for contributing to YATL Core!