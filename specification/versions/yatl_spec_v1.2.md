# YATL Specification v1.2

This version introduces the concept of triggers to YATL, allowing workflows to be initiated by various events.

## New Features

### Triggers

YATL 1.2 introduces a new `triggers` section in the workflow definition. Triggers define how a workflow can be initiated. Multiple triggers can be defined for a single workflow.

#### Supported Trigger Types

1. HTTP Trigger
2. Webhook Trigger
3. Schedule Trigger
4. Cloud Event Trigger

### Trigger Context

Actions now have access to trigger-specific data through a new `trigger` object in the context. This allows workflows to use information from the triggering event in their execution.

## Backwards Compatibility

YATL 1.2 maintains backwards compatibility with version 1.0 and 1.1. Workflows without triggers will continue to function as before.

## Example

See the main specification file for a complete example of a YATL 1.2 workflow with a webhook trigger.

