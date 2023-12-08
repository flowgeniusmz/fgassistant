schema_generate_image = {
    "type": "function",
    "function": {
        "name": "generate_image",
        "description": "Generates an image using Dall-e 3 based on a provided text prompt.",
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The text prompt based on which the image is to be generated."
                },
                "size": {
                    "type": "string",
                    "enum": ["c", "f"],
                    "description": "The size of the generated image. Allowed values are 'c' and 'f'."
                }
            },
            "required": ["prompt"]
        }
    }
}

