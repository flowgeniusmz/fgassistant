

def execute_function_call(message):
    function_name = message["function_call"]["name"]
    if function_name == "translate":
        query = json.loads(message["function_call"]["arguments"])["text"]
        results = translate(query)
    elif function_name == "get_current_weather":
        location = json.loads(message["function_call"]["arguments"])["location"]
        results = get_weather(location)
    else:
        results = "Function not found"
    return results
