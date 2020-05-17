import urllib.request
from bs4 import BeautifulSoup
import re
import requests


def get_list_of_cities():
    cities_in_poland = []
    cities_in_poland_link = "https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Poland"
    page = urllib.request.urlopen(cities_in_poland_link)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if cols != []:
            cities_in_poland.append(
                (cols[0].a['href'].split("/")[2], cols[0].a['title']))
    return cities_in_poland


def get_city_json(city_names):
    (city_name, city_title_name) = city_names
    r = requests.get("http://dbpedia.org/data/" + city_name + ".json")
    return (city_title_name, r.json()["http://dbpedia.org/resource/" + city_title_name.replace(" ", "_")])


