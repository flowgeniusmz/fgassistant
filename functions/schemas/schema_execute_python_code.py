schema_execute_python_code = {
    "name": "execute_python_code",
    "description": "Executes a given string of Python code in a temporary file and returns the output.",
    "parameters": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The string containing the Python code to be executed."
            }
        },
        "required": ["code"]
    }
}
