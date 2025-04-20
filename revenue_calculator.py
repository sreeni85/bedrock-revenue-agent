import logging
from typing import Dict, Any

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for calculating revenue based on input from Amazon Bedrock Agent.
    """

    try:
        # Convert parameter list to a dictionary { name: value }
        param_list = event.get("parameters", [])
        params = {param["name"]: int(param["value"]) for param in param_list}

        # Extract parameters
        quantity1 = params["quantity1"]
        quantity2 = params["quantity2"]
        price1 = params["price1"]
        price2 = params["price2"]

        # Revenue calculations
        product1_total = quantity1 * price1
        product2_total = quantity2 * price2
        total = product1_total + product2_total

        # Final message
        message = (
            f"Your total revenue is ${total}. This is how I calculated it:\n"
            f"- {quantity1} laptops at ${price1} each: ${product
