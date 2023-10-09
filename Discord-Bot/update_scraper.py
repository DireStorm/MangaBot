from urllib.request import urlopen
import re
from pprint import pprint

desired_input = "+".join(input("Enter a manga/manhwa/novel: ").split(" "))


url = "https://www.mangaupdates.com/search.html?search="+desired_input

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# The problem with the method below, is that the wrong result is output if the user inputs the wrong name
search_results = re.search("<div class=\"col-6 py-1 py-md-0 text\">.*</div>", html, re.IGNORECASE)

# This method returns all results under the search, which you can further parse through (requires extra steps)
# search_results = re.findall("'https://www.mangaupdates.com/series/.*</a>", html, re.IGNORECASE)
desired_result = search_results.group()

print(pprint(desired_result))