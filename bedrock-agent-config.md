# 🤖 Bedrock Agent Configuration Guide

This file explains how to configure the **Amazon Bedrock Agent** and its **action group** to work with the `revenue_calculator.py` Lambda function.

---

## 🧱 1. Create a New Bedrock Agent

1. Go to [Amazon Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Navigate to **Agents** → Click **Create agent**
3. Provide:
   - **Agent name**: RevenueCalculatorAgent
   - **Description**: Calculates total revenue based on user input
   - **IAM Role**: Create or choose a role with Lambda invoke permission

---

## 🧩 2. Add an Action Group

Once the agent is created:

1. Under the agent, go to **Action groups**
2. Click **Add action group**
3. Set:
   - **Action group name**: `action-group-business`
   - **Lambda function**: Select your deployed Lambda (e.g., `revenue_calculator`)
4. Define parameters:

| Name       | Type     | Required | Description                        |
|------------|----------|----------|------------------------------------|
| quantity1  | integer  | ✅        | Quantity of the first product sold |
| price1     | number   | ✅        | Price of the first product         |
| quantity2  | integer  | ✅        | Quantity of the second product     |
| price2     | number   | ✅        | Price of the second product        |

---

## 🧠 3. Agent Instructions (System Prompt)

Paste the following into the **System prompt** field:

```text
You are a revenue calculation assistant. You will:
- Identify all product names, their quantities, and unit prices from the user’s input.
- Compute total revenue as (quantity × price) for each product.
- Provide a breakdown and final result in a clear format.
- Only use the parameters provided by the user, do not make assumptions.
