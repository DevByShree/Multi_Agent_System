from langchain.tools import tool   # Create AI tools
import requests                    # Make API/web requests
from bs4 import BeautifulSoup      # Parse website HTML
from tavily import TavilyClient    # AI web search tool
import os                          # Access system variables
from dotenv import load_dotenv     # Load .env file

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
# this tool for search  info 
@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information."""

    results = tavily.search(query=query, max_results=3)

    out = []
    
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content'][:300]}\n"
        )

    return "\n-----\n".join(out)

# this tool is for extract the information 
@tool
def scrape_url(url:str)-> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:2000]
    except Exception as e:
        return f"Cloud not scrape URL: {str(e)}"






