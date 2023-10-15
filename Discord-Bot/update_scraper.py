from urllib.request import urlopen
import re
from pprint import pprint

desired_input = "+".join(input("Enter a manga/manhwa/novel: ").split(" "))


url = "https://www.mangaupdates.com/search.html?search="+desired_input

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# The problem with the method below, is that the wrong result is output if the user inputs the wrong name (or misspells the name)
search_results = re.search("<div class=\"col-6 py-1 py-md-0 text\">.*</div>", html, re.IGNORECASE)

# This method returns all results under the search, which you can further parse through (requires extra steps)
# search_results = re.findall("'https://www.mangaupdates.com/series/.*</a>", html, re.IGNORECASE)
desired_result = search_results.group()

print(desired_result)

# Getting manga/manhwa url from desired_result
# [starting index: ending index]
desired_url = desired_result[desired_result.find("href='")+len("href='"):desired_result.find("' alt")]

print(desired_url)

page = urlopen(desired_url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# For last update of the website
# search_results = re.search("<div class=\"sCat\"><b>Last Updated</b></div>\n.*\n</div>", html, re.IGNORECASE)
# latest_update = search_results.group()
# latest_update = latest_update[latest_update.find("<div class=\"sContent\" >")+len("<div class=\"sContent\" >"):latest_update.find("\n</div>")]



# For latest release of chapter
try:
    search_results = re.search("<div class=\"sContent\" >c.*\n</div>", html, re.IGNORECASE).group()
    latest_release = search_results[search_results.find("<span title = '")+len("<span title = '"):search_results.find("ago")+len("ago")]

    m_name = re.search("<title>.* - Baka-Updates Manga</title>", html, re.IGNORECASE).group()

    # Final Results
    m_name = m_name[m_name.find("<title>")+len("<title>"):m_name.find(" -")]
    # m_name = desired_result[desired_result.find("<i>")+len("<i>"):desired_result.find("</i>")]

    print(f"\n\n\n{m_name} was last updated {latest_release}!")

except AttributeError: 
    print("There haven't been any new releases as of yet!")
