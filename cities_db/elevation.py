import db_importer

def get_elevaton(city_json):
    (city, json_dict) = city_json
    return (city, float(json_dict.get("http://dbpedia.org/ontology/elevation")[0]['value']))

def elevations():
    return [
        ("sea", lambda x: x < 20),
        ("lowland", lambda x: x < 300),
        ("upland", lambda x: x < 500),
        ("mountains", lambda x: x >= 500)
    ]

def add_elevation_sizes():
    for (size, _) in elevations():
        query = "MERGE (e:Elevation {name:'" + size + "'})"
        db_importer.run_query(query)

def pair_city_with_elevations(city_json):
    try:
        add_elevation_sizes()
        (city_name, elevation) = get_elevaton(city_json)
        for (size_name, cond) in elevations():
            if cond(elevation):
                query = "MATCH " + \
                    "(c:City {name:'" + city_name + "'}), " + \
                    "(e:Elevation {name:'" + size_name + "'}) " + \
                    "MERGE (c)-[:Elevation]->(e);"
                return db_importer.run_query(query)
    except:
        return 0
