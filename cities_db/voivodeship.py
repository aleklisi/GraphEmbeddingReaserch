import db_importer


def get_voivodeship(city_with_json):
    (city, json_dict) = city_with_json
    for v in json_dict.get("http://dbpedia.org/ontology/isPartOf"):
        if "Voivodeship" in v.get('value'):
            return (city, v.get('value').split("/")[-1])


def add_voivodeship(city_with_voivodeship):
    (_, voivodeship) = city_with_voivodeship
    query = "MERGE (v:Voivodeship {name:'" + voivodeship + "'})"
    return db_importer.run_query(query)


def assign_city_to_voivodeship(city_with_voivodeship):
    (city_name, voivodeship) = city_with_voivodeship
    query = "MATCH " + \
        "(c:City {name:'" + city_name + "'}), " + \
        "(v:Voivodeship {name:'" + voivodeship + "'}) " + \
        "MERGE (c)-[:IsPartOf]->(v);"
    return db_importer.run_query(query)


def pair_city_with_voivodeship(city_json):
    try:
        city_with_voivodeship = get_voivodeship(city_json)
        add_voivodeship(city_with_voivodeship)
        return assign_city_to_voivodeship(city_with_voivodeship)
    except:
        return 0
