from neo4j import GraphDatabase
import random

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)


def all_nodes_query(tx):
    return [record["ID(n)"] for record in tx.run("MATCH (n) RETURN ID(n);")]


def get_all_nodes():
    with driver.session() as session:
        return session.read_transaction(all_nodes_query)


def all_children_nodes_query(tx, nodeID):
    return [record["ID(m)"] for record in tx.run("MATCH (n) -[r]- (m) WHERE ID(n) = $nodeID RETURN ID(m);", nodeID=nodeID)]


def get_children_nodes(node):
    with driver.session() as session:
        return session.read_transaction(all_children_nodes_query, node)


def node_id_to_node_query(tx, i):
    return [record for record in tx.run("MATCH (n) WHERE ID(n) = $i RETURN n;", i=i)]


def node_id_to_node(id):
    with driver.session() as session:
        return session.read_transaction(node_id_to_node_query, id)


def pick_n_random_from_list(nodes, n):
    return random.choices(nodes, k=n)


def pick_random_from_list(children):
    return pick_n_random_from_list(children, 1)[0]


def make_path_from_node(node, remaining_length):
    if remaining_length == 0:
        return []
    else:
        children_nodes = get_children_nodes(node)
        # Island & non bidirectional graph traversing handling
        if children_nodes == []:
            return []
        new_node = pick_random_from_list(children_nodes)
        return [new_node] + make_path_from_node(new_node, remaining_length - 1)


def deepwalk(number_of_nodes, number_of_paths_per_node, path_lengths):
    all_nodes = get_all_nodes()
    nodes_to_walk_from = pick_n_random_from_list(all_nodes, number_of_nodes)
    walks = []
    for node in nodes_to_walk_from:
        for _ in range(number_of_paths_per_node):
            path = make_path_from_node(node, path_lengths)
            # For nice printing
            path = list(map(lambda n: node_id_to_node(n), path))
            walks.append(path)
    return walks


def main():
    nodes = deepwalk(2, 2, 3)

    # Nice printing
    for node in nodes:
        print("")
        for path in node:
            print(path)


main()
