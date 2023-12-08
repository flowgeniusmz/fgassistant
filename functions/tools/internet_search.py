import time
from tavily import TavilyClient
import streamlit as st

# MAIN FUNCTION
def internet_search(varQuery, varType: str = 'basic'):
    """
    Conducts an internet search based on a query and a specified search type.

    Parameters:
    varQuery (str): The query string for the internet search.
    varType (str, optional): The type of the search. Can be either 'basic' or 'advanced'.
                             Defaults to 'basic'.

    Raises:
    ValueError: If varType is not 'basic' or 'advanced'.

    Returns:
    The result of the internet search. (This part should be customized based on what your function actually returns)
    """
    client_tavily = TavilyClient(api_key=st.secrets.tavily.api_key)
    search_result = client_tavily.get_search_context(
        query=varQuery,
        search_depth=varType,
        max_tokens=4000,
        max_results=5
    )
    return search_result



#https://gist.github.com/assafelovic/579822cd42d52d80db1e1c1ff82ffffd

#https://app.tavily.com/playground
