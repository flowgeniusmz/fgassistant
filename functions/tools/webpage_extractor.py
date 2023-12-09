import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def dynamic_webpage_extractor(url):
    """
    Extracts and compiles different types of content from a webpage specified by the URL.

    Parameters:
    url (str): The URL of the webpage to be extracted.

    Returns:
    str: A compiled string of extracted content, including headers, paragraphs, table rows (if enabled), and links.
         If the webpage is not accessible or any other error occurs, it returns an error message with details.

    Notes:
    The function uses a configuration to determine the types of content to extract. By default, it extracts headers,
    paragraphs, and links, but not table rows. It processes the webpage using BeautifulSoup, extracts the specified 
    content types, and compiles them into a single string. In case of HTTP errors or exceptions, an appropriate 
    error message is returned.
    """

    config = {"headers": True, "paragraphs": True, "table_rows": False, "links": True}
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Received status code {response.status_code}"
        
        soup = BeautifulSoup(response.content, "html.parser")

        content = []

        # Process headers if specified
        if config.get("headers"):
            header_tags = soup.find_all(re.compile(r"^h\d$"))
            content.extend([tag.get_text().strip() for tag in header_tags])

        # Process paragraphs if specified
        if config.get("paragraphs"):
            paragraph_tags = soup.find_all("p")
            content.extend([tag.get_text().strip() for tag in paragraph_tags])

        # Process table rows if specified
        if config.get("table_rows"):
            tr_tags = soup.find_all("tr")
            content.extend([' '.join(td.get_text().strip() for td in tag.find_all('td')) for tag in tr_tags])

        # Process links if specified
        if config.get("links"):
            a_tags = soup.find_all('a')
            links = [urljoin(url, a_tag.get('href')) if a_tag.get('href') else 'No link found' for a_tag in a_tags]
            content.extend(links)

        return '\n'.join(content)

    except Exception as e:
        return f"Error scraping URL '{url}': {str(e)}"


