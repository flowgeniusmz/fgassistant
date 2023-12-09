import json

def append_tool_schema_to_file(schema, file_name='tools_schema.json'):
    try:
        # Load the existing data from the file
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            # If file does not exist, create a new list to store schemas
            data = []

        # Append the new schema
        data.append(schema)

        # Write the updated data back to the file
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Schema for {schema['function']['name']} appended to {file_name}.")
    except Exception as e:
        print(f"Error while appending schema: {e}")
