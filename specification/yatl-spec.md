# YATL Specification v1.0

YATL (Yet Another Tentacle Language) is a markup language for defining state machines.

## Basic Structure

A YATL document consists of the following main sections:

1. `name`: The name of the state machine
2. `initial_state`: The starting state
3. `states`: A list of all possible states
4. `actions`: Defined actions that can be performed
5. `events`: Events that can trigger state transitions

## States

Each state is defined with:

- `type`: The type of state (e.g., "normal", "final")
- `on_enter`: Actions to perform when entering the state
- `on_exit`: Actions to perform when exiting the state
- `transitions`: Possible state changes based on events

## Example

```yaml
name: TrafficLight
initial_state: Red
states:
  Red:
    type: normal
    on_enter: [turnOnRed]
    on_exit: [turnOffRed]
    transitions:
      - event: TimerExpired
        target: Green
  # ... other states
```

For full syntax and more examples, please refer to the complete specification.
