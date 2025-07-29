import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
# 2. Concurrency and Parallelism

# Practice Task : 1 | Create a program that scrapes multiple websites concurrently using asyncio.
urls = [
    "https://quotes.toscrape.com",
    "https://books.toscrape.com",
    "https://news.ycombinator.com",
    "https://example.com"
]

# Async function to fetch HTML content
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            html = await response.text()
            return url, html
    except Exception as e:
        return url, f"Error: {e}"

# Function to extract and print title from HTML
def get_title(url, html):
    if html.startswith("Error"):
        print(f"Failed to fetch {url} - {html}")
        return

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title found"
    print(f"Fetched {url} - Title: {title}")

# Main async function to coordinate all tasks
async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for url, html in responses:
            get_title(url, html)

    print(f"\nCompleted in {time.time() - start_time:.2f} seconds")

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())