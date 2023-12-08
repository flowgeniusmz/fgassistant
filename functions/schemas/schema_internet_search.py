import streamlit as st


schema_internet_search = {
    "name": "internet_search",
    "description": "Conducts an internet search based on a query and a specified search type.",
    "parameters": {
        "type": "object",
        "properties": {
            "varQuery": {
                "type": "string",
                "description": "The query string for the internet search."
            },
            "varType": {
                "type": "string",
                "description": "The type of the search. Can be either 'basic' or 'advanced'. Defaults to 'basic'.",
                "enum": ["basic", "advanced"],
                "default": "basic"
            }
        },
        "required": ["varQuery"]
    }
}

