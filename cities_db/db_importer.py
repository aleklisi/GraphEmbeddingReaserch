from neo4j import GraphDatabase

def add_city(city_names):
    (city_name, _) = city_names
    query = "MERGE (c:City {name:'" + city_name + "'})"
    return run_query(query)

def run_query(query_str):
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri)
    with driver.session() as session:
        return session.run(query_str)
