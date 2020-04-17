from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)

with open('bible.txt', 'r') as file:
    data = file.read().replace('\n', '').split(" ")
    data_size = len(data)

    with driver.session() as session:
        # Clear all nodes
        session.run("MATCH (n) DETACH DELETE n;")
        # Add words
        print("Loading words started.")
        i = 0.0
        for word in data:
            session.run("MERGE (w:WORD { word: '" + word + "'});")
            i = i + 1
            if i % 1000 == 0:
                print(str(100 * i / data_size) + " % words loaded")
        print("Loading words finished.")
        print(str(i) + "words were loaded.")

        zipped = zip(data[:-1], data[1:])
        i = 0.0
        print("Loading followers started.")
        for (pre, post) in zipped:
            session.run(
                "MATCH (w1:WORD {word:'" + pre + "'}), (w2:WORD {word:'"+ post +"'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;")
            i = i + 1
            if i % 1000 == 0:
                print(str(100 * i / data_size) + " % pairs loaded")
        print("Loading followers finished.")
        print(str(i) + "followers were loaded.")

print("Script finished.")
