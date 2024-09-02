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

[Rest of the content remains the same as in the previous specification, including States, Actions, Variables, and Conditions sections]

## Example

Here's an updated example of a YATL workflow for processing orders, now including a webhook trigger:

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
          variable: $.paymentStatus
          operator: equals
          value: SUCCESS
        next: FulfillOrder
      - condition:
          variable: $.paymentStatus
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

  validateOrder:
    description: "Validate the order"
    language: python
    code: |
      context['is_valid'] = context['total_amount'] > 0 and len(context['items']) > 0

  processPayment:
    description: "Process payment for the order"
    language: python
    code: |
      # Payment processing logic here
      context['paymentStatus'] = 'SUCCESS'

  fulfillOrder:
    description: "Fulfill the order"
    language: python
    code: |
      # Order fulfillment logic here
      print(f"Fulfilling order {context['order_id']}")

  cancelOrder:
    description: "Cancel the order"
    language: python
    code: |
      # Order cancellation logic here
      print(f"Cancelling order {context['order_id']}")

  handlePaymentError:
    description: "Handle payment processing errors"
    language: python
    code: |
      # Error handling logic here
      print(f"Payment error for order {context['order_id']}")

  sendNotification:
    description: "Send notification to the customer"
    language: python
    code: |
      # Notification logic here
      print(f"Sending notification for order {context['order_id']}")

variables:
  order_id: string
  items: list
  total_amount: number
  is_valid: boolean
  paymentStatus: string
```

This example demonstrates the new trigger feature along with the existing YATL concepts.