#!/usr/bin/python
from neo4j import GraphDatabase
import random
import sys

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)


def get_city_vector_query(tx, city_name):
    transaction_results = tx.run(
        "MATCH (n:City) --> (m) WHERE n.name = $city_name RETURN labels(m) AS labels, m.name as name;",
        city_name=city_name)
    result = {}
    for record in transaction_results:
        [key] = record["labels"]
        result[key] = record["name"]
    return result


def get_city_vector(city_name):
    with driver.session() as session:
        return session.read_transaction(get_city_vector_query, city_name)


def maybe_get(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    return None


class VectorCity:
    def __init__(self, name):
        city_params = get_city_vector(name)
        self.name = name
        self.voivodeship = maybe_get(city_params, 'Voivodeship')
        self.size = maybe_get(city_params, 'CitySize')
        self.elevation = maybe_get(city_params, 'Elevation')

    def __str__(self):
        return str((self.name, {
            "voivodeship": self.voivodeship,
            "size": self.size,
            "elevation": self.elevation
        }))

    def compare(self, city):
        return sum([
            self.name == city.name,
            self.voivodeship == city.voivodeship,
            self.size == city.size,
            self.elevation == city.elevation
        ]) / 4


def main(city_name_1, city_name_2):
    city1 = VectorCity(city_name_1)
    city2 = VectorCity(city_name_2)
    print(city1.compare(city2))


main(sys.argv[1], sys.argv[2])
