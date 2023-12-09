
# JSON Schema Template for Python Functions

This template is designed for generating JSON schemas for various Python functions.

```json
{
    "type": "function",
    "function": {
        "name": "<function_name>",
        "description": "<function_description>",
        "parameters": {
            "type": "object",
            "properties": {
                "<parameter_name>": {
                    "type": "<data_type>",
                    "description": "<parameter_description>"
                }
                // Add other parameters here
            },
            "required": ["<required_parameter_name>"]
        }
    }
}
```
