import db_importer


def get_total_area(city_with_json):
    (city, json_dict) = city_with_json
    return (city, float(json_dict.get("http://dbpedia.org/ontology/PopulatedPlace/areaTotal")[0]['value']))


def city_areas():
    return [
        ("very_small", lambda x: x < 100.0),
        ("small", lambda x: x >= 100.0 and x < 200),
        ("middle", lambda x: x >= 200.0 and x < 300),
        ("big", lambda x: x >= 300.0)
    ]


def add_area_sizes():
    for (size, _) in city_areas():
        query = "MERGE (cs:CitySize {name:'" + size + "'})"
        db_importer.run_query(query)


def pair_city_with_area(city_json):
    try:
        add_area_sizes()
        (city_name, area) = get_total_area(city_json)
        for (size_name, cond) in city_areas():
            if cond(area):
                query = "MATCH " + \
                    "(c:City {name:'" + city_name + "'}), " + \
                    "(cs:CitySize {name:'" + size_name + "'}) " + \
                    "MERGE (c)-[:Size]->(cs);"
                return db_importer.run_query(query)
    except:
        return 0
