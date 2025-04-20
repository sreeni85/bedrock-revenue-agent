# 💰 Bedrock Revenue Calculator Agent

This project showcases how to build an AI assistant using **Amazon Bedrock Agents** with a **Lambda function** to compute sales revenue based on natural language input.

---

## 📌 Use Case

A user can say:

> "I sold 2 laptops at $20 each and 3 mice at $10 each. What is my total revenue?"

And the agent will respond with:

> "Your total revenue is $70. This is how I calculated it:
> - 2 laptops at $20 each: $40
> - 3 mice at $10 each: $30
> - Total revenue: $70"

---

## 🧠 What’s Inside

- ✅ Amazon Bedrock Agent with parameterized action group
- ✅ Lambda function for revenue calculation
- ✅ JSON-compatible Bedrock response format
- ✅ Full test payload for validation

---

## 📁 Folder Structure

```bash
bedrock-revenue-agent/
├── lambda/
│   └── revenue_calculator.py
├── test-event.json
├── bedrock-agent-config.md
├── README.md
├── assets/
│   └── screenshot.png (optional)
