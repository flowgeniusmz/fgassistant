
# JSON Schema Examples for Python Functions

These examples demonstrate how the OpenAI assistant can generate JSON schemas for various Python functions.

## Example 1: calculate_area Function

```json
{
    "type": "function",
    "function": {
        "name": "calculate_area",
        "description": "Calculates the area of a rectangle.",
        "parameters": {
            "type": "object",
            "properties": {
                "length": {
                    "type": "number",
                    "description": "The length of the rectangle."
                },
                "width": {
                    "type": "number",
                    "description": "The width of the rectangle."
                }
            },
            "required": ["length", "width"]
        }
    }
}
```

## Example 2: send_email Function

```json
{
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Sends an email to a specified recipient.",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient": {
                    "type": "string",
                    "description": "The email address of the recipient."
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email."
                },
                "body": {
                    "type": "string",
                    "description": "The body content of the email."
                }
            },
            "required": ["recipient", "subject", "body"]
        }
    }
}
```

## Example 3: convert_temperature Function

```json
{
    "type": "function",
    "function": {
        "name": "convert_temperature",
        "description": "Converts temperature from Celsius to Fahrenheit.",
        "parameters": {
            "type": "object",
            "properties": {
                "celsius": {
                    "type": "number",
                    "description": "Temperature in Celsius to be converted."
                }
            },
            "required": ["celsius"]
        }
    }
}
```

## Example 4: generate_report Function

```json
{
    "type": "function",
    "function": {
        "name": "generate_report",
        "description": "Generates a financial report for a given quarter.",
        "parameters": {
            "type": "object",
            "properties": {
                "quarter": {
                    "type": "string",
                    "description": "The quarter for which to generate the report."
                },
                "year": {
                    "type": "number",
                    "description": "The year of the report."
                }
            },
            "required": ["quarter", "year"]
        }
    }
}
```

## Example 5: find_user Function

```json
{
    "type": "function",
    "function": {
        "name": "find_user",
        "description": "Finds a user in the database by username.",
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "The username to search for."
                }
            },
            "required": ["username"]
        }
    }
}
```
