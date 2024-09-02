# YATL Specification v1.2

YATL (Yet Another Tentacle Language) is a markup language for defining state machines and workflows.

## Table of Contents

1. [Basic Structure](#basic-structure)
2. [Triggers](#triggers)
3. [States](#states)
4. [Actions](#actions)
5. [Variables](#variables)
6. [Conditions](#conditions)
7. [Example](#example)

## Basic Structure

A YATL file consists of the following main sections:

```yaml
name: <StateMachineName>
description: <Optional description>
version: <Optional version string>
triggers:
  # Trigger definitions
initial_state: <InitialStateName>

states:
  # State definitions

actions:
  # Action definitions

variables:
  # Variable definitions
```

## Triggers

Triggers define how a workflow can be initiated. Multiple triggers can be defined for a single workflow.

### HTTP Trigger

```yaml
triggers:
  - type: http
    path: /api/workflow
    method: POST
    auth: 
      type: api_key
      header: X-API-Key
```

### Webhook Trigger

```yaml
triggers:
  - type: webhook
    event: new_order
    source: ecommerce_system
    auth:
      type: hmac
      secret_env: WEBHOOK_SECRET
```

### Schedule Trigger

```yaml
triggers:
  - type: schedule
    cron: "0 0 * * *"  # Run daily at midnight
```

### Cloud Event Trigger

```yaml
triggers:
  - type: cloud_event
    type: com.example.object.created
    source: storage.googleapis.com
```

## States

States are defined under the states section. Each state has a unique name and properties based on its type.

### Task State

```yaml
StateName:
  type: task
  action: <actionName>
  next: <nextStateName>
```

### Choice State

```yaml
StateName:
  type: choice
  choices:
    - condition: <condition>
      next: <nextStateName>
  default: <defaultStateName>
```

### Loop State

```yaml
StateName:
  type: loop
  collection: <collectionVariable>
  iterator: <iteratorName>
  body:
    <stateMachineDefinition>
  next: <nextStateName>
```

### Parallel State

```yaml
StateName:
  type: parallel
  branches:
    - <stateMachineDefinition>
  next: <nextStateName>
```

### End State

```yaml
StateName:
  type: end
  result: <resultData>
```

### Fail State

```yaml
StateName:
  type: fail
  error: <errorType>
  cause: <errorDescription>
```

## Actions

Actions are defined in the actions section. Each action can include executable code:

```yaml
actions:
  actionName:
    description: "Description of the action"
    language: <programmingLanguage>
    code: |
      # Code block
      # Can reference variables using context['variableName']
      # Trigger data available via context['trigger']
```

## Variables

Variables are declared in the variables section:

```yaml
variables:
  variableName: <dataType>
```

Variables can be referenced in states and actions using the context dictionary: `context['variableName']`

## Conditions

Conditions are used in choice states to determine the next state:

```yaml
condition:
  variable: <variableName>
  operator: <operatorType>
  value: <comparisonValue>
```

Supported operators include:

- `equals`
- `not_equals`
- `greater_than`
- `less_than`
- `contains`

## Example

Here's an example of a YATL 1.2 workflow for processing orders:

```yaml
name: OrderProcessingWorkflow
description: "Process new orders from the e-commerce system"
version: "1.2"
triggers:
  - type: webhook
    event: new_order
    source: ecommerce_system
    auth:
      type: hmac
      secret_env: WEBHOOK_SECRET
initial_state: ProcessNewOrder

states:
  ProcessNewOrder:
    type: task
    action: parseOrderData
    next: ValidateOrder

  ValidateOrder:
    type: task
    action: validateOrder
    next: ProcessPayment

  ProcessPayment:
    type: task
    action: processPayment
    next: CheckPaymentStatus

  CheckPaymentStatus:
    type: choice
    choices:
      - condition:
          variable: paymentStatus
          operator: equals
          value: SUCCESS
        next: FulfillOrder
      - condition:
          variable: paymentStatus
          operator: equals
          value: FAILED
        next: CancelOrder
    default: HandlePaymentError

  FulfillOrder:
    type: task
    action: fulfillOrder
    next: NotifyCustomer

  CancelOrder:
    type: task
    action: cancelOrder
    next: NotifyCustomer

  HandlePaymentError:
    type: task
    action: handlePaymentError
    next: NotifyCustomer

  NotifyCustomer:
    type: task
    action: sendNotification
    next: End

  End:
    type: end

actions:
  parseOrderData:
    description: "Parse the incoming webhook data"
    language: python
    code: |
      order = context['trigger']['data']
      context['order_id'] = order['id']
      context['items'] = order['items']
      context['total_amount'] = order['total_amount']
      print(f"Received order {context['order_id']}")

  validateOrder:
    description: "Validate the order"
    language: python
    code: |
      context['is_valid'] = context['total_amount'] > 0 and len(context['items']) > 0
      print(f"Order {context['order_id']} validity: {context['is_valid']}")

  processPayment:
    description: "Process payment for the order"
    language: python
    code: |
      # This would typically involve calling a payment gateway API
      context['paymentStatus'] = 'SUCCESS'  # Simulating successful payment
      print(f"Payment processed for order {context['order_id']}: {context['paymentStatus']}")

  fulfillOrder:
    description: "Fulfill the order"
    language: python
    code: |
      # This would typically involve calling a fulfillment system API
      print(f"Fulfilling order {context['order_id']}")

  cancelOrder:
    description: "Cancel the order"
    language: python
    code: |
      print(f"Cancelling order {context['order_id']}")

  handlePaymentError:
    description: "Handle payment processing errors"
    language: python
    code: |
      print(f"Payment error for order {context['order_id']}")

  sendNotification:
    description: "Send notification to the customer"
    language: python
    code: |
      status = "processed" if context['paymentStatus'] == 'SUCCESS' else "cancelled"
      print(f"Sending notification for order {context['order_id']}: Order {status}")

variables:
  order_id: string
  items: list
  total_amount: number
  is_valid: boolean
  paymentStatus: string
```

This example demonstrates various features of YATL 1.2, including the new trigger system, task states, choice states, actions with code, and variable usage. The workflow is triggered by a webhook, processes an order, handles payment, and notifies the customer of the outcome.