import folium
import wikipedia as wiki
import re
import pandas as pd
import requests
import urllib.request
import json
import time
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url,timeout=90)
result = json.loads(response.read())
location = result ["iss_position"]
lat = location ["latitude"]
lon = location ["longitude"]
lat = float(lat)
lon = float (lon)

print ("\nLatitude: " + str(lat))
print ("\nLatitude: " + str(lon))

time.sleep(5)

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url,timeout=90)
result = json.loads(response.read())
people = result ['people']

astronauts = []
spacecraft = []
for p in people:
    astronauts.append(p['name'])
    spacecraft.append(p['craft'])

astro_page = []
for astronaut in astronauts:
    try:
        page = wiki.page(astronaut, auto_suggest=False)
        if 'astronaut' in page.summary.lower() or 'taikonaut' in page.summary.lower() or "cosmonaut" in page.summary.lower():
            astro_page.append(page.url)
            print(page.url)
        else:
            page = wiki.page(f"{astronaut} taikonaut")
            astro_page.append(page.url)
            print(page.url)
    except wiki.DisambiguationError as e:
        for option in e.options:
            if 'astronaut' in option.lower() or 'taikonaut' in option.lower():
                try:
                    page = wiki.page(option)
                    if 'astronaut' in page.summary.lower() or 'taikonaut' in page.summary.lower():
                        astro_page.append(page.url)
                        print(page.url)
                except wiki.DisambiguationError:
                    continue
    except wiki.PageError:
        print(f"Page not found for {astronaut}.")

img_links = []
img_src_list = []
dob_list = []
nationality_list = []
age_list = []
today = date.today()
for url in astro_page:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Extracting Astronauts images
    covers = soup.select("main#content table.biography tbody tr td.infobox-image span a.mw-file-description img")
    img_src_list.extend(img.get('src') for img in covers)

    # Extracting and Manipulating their birth dates
    infobox_table = soup.find('table', class_='infobox biography vcard')
    if infobox_table:
        next_sibling = infobox_table.find_next_sibling()
        while next_sibling and next_sibling.name != 'p':
            next_sibling = next_sibling.find_next_sibling()
        if next_sibling and next_sibling.name == 'p':
            paragraph_text = next_sibling.get_text(strip=True)
            year_match = re.search(r'\b(19|20)\d{2}\b', paragraph_text)
            if year_match:
                birth_year = int(year_match.group(0))
                age = today.year - birth_year
                dob_list.append(birth_year)
                age_list.append(age)
            else:
                dob_list.append("Year not found")
                age_list.append("Age not found")
        else:
            dob_list.append("No paragraph found immediately following the infobox table.")
            age_list.append("Age not found")
    else:
        dob_list.append("Infobox table not found.")
        age_list.append("Age not found")

    # Extract nationality
    shortdescription_div = soup.select("main#content div.shortdescription.nomobile.noexcerpt.noprint.searchaux")
    if shortdescription_div:
        for div in shortdescription_div:
            text = div.get_text(strip=True)
            nationality_match = re.match(r'\b\w+\b', text)
            nationality_list.append(nationality_match.group(0) if nationality_match else "Nationality not found")
    else:
        nationality_list.append("Info not found")

# Ensure all lists are the same length
max_length = max(len(img_src_list), len(dob_list), len(nationality_list), len(age_list))
img_src_list.extend([""] * (max_length - len(img_src_list)))
dob_list.extend([""] * (max_length - len(dob_list)))
nationality_list.extend([""] * (max_length - len(nationality_list)))
age_list.extend([""] * (max_length - len(age_list)))


