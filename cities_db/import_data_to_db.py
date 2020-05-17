import data_crowler
import db_importer

import voivodeship
import areaTotal
import elevation

cities = data_crowler.get_list_of_cities()[:5]
dbpedia_cities_jsons = list(map(lambda s: data_crowler.get_city_json(s), cities))

# Import cities
list(map(lambda c: db_importer.add_city(c), dbpedia_cities_jsons))

# Pair cities with respective voivodeships
list(map(lambda s: voivodeship.pair_city_with_voivodeship(s), dbpedia_cities_jsons))

# Pair cities with their areas
list(map(lambda s: areaTotal.pair_city_with_area(s), dbpedia_cities_jsons))

# Pair cities with their elevations
list(map(lambda s: elevation.pair_city_with_elevations(s), dbpedia_cities_jsons))
