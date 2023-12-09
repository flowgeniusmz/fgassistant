import json


    # Function to append a new tool function and its metadata
def append_new_tool_function_and_metadata(function_name: str, function_code: str, metadata: dict, tool_meta_description: str):
    try:
        # Logic to append new function code to dynamic_functions.py
        with open('assistant_manager/functions/dynamic/dynamic_functions.py', 'a') as file:
            file.write(f'\n\n{function_code}')

        
        # Add the tool_meta_description to the metadata dict
        metadata['tool_meta_description'] = tool_meta_description

        # Logic to append new metadata to functions_metadata.json
        with open('assistant_manager/functions/dynamic/functions_metadata.json', 'r+') as file:
            existing_metadata = json.load(file)
            # Lets run a check to see if the read metadata is hiding in a dict wrapped around our dict
            
            existing_metadata[function_name] = metadata
            file.seek(0)  # Reset file position to the beginning.
            json.dump(existing_metadata, file, indent=4)
    except Exception as e:
        print(f"An error occurred while appending the new function: {e}")
        return False
    return True  # Indication that the function and metadata have been successfully appended
