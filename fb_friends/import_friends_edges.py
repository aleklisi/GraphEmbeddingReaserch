from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)

file1 = open('facebook/0.edges', 'r')
Lines = file1.readlines()

with driver.session() as session:
    # Clear all nodes
    session.run("MATCH (n) DETACH DELETE n;")
    # Add words

    nodes = []
    for line in Lines:
        [from_node, to_node] = line.strip().split(" ")
        if from_node not in nodes:
            nodes.append(from_node)
        if to_node not in nodes:
            nodes.append(to_node)

    print("Loading nodes started.")
    for node in nodes:
        session.run("MERGE (p:Person { name: '" + node + "'});")
    print("Loading nodes finished.")

    print("Loading relations started.")
    for line in Lines:
        [from_node, to_node] = line.strip().split(" ")
        result = session.run(
                "MATCH "
                "(p1:Person {name:'" + from_node + "'}), "
                "(p2:Person {name:'"+ to_node +"'}) "
                "MERGE (p1)-[r:IS_FRIEND]->(p2) "
                "ON CREATE SET r.weight = 1.0 "
                "ON MATCH SET r.weight = r.weight + 1;")
    print("Loading relations finished.")
