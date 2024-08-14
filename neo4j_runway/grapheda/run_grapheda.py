# script to test Neo4jGraph Class

import pandas as pd

# import neo4jrunway functions 
from neo4j_runway.database import Neo4jGraph
from neo4j_runway.utils.read_env import read_environment
from neo4j_runway.utils.test_connection import test_database_connection

# import and read from .env file
import dotenv 
dotenv.load_dotenv()

from neo4j_runway.grapheda.grapheda import GraphEDA


# instantiate Neo4jGraph
neo4j_graph = Neo4jGraph(
        username=read_environment("NEO4J_USERNAME"),
        password=read_environment("NEO4J_PASSWORD"),
        uri=read_environment("NEO4J_URI"),
    )


# instantiate GraphEDA class
graph_eda = GraphEDA(neo4j_graph=neo4j_graph)

############################
# DATABASE DETAILS 
############################

# result = graph_eda.neo4j_graph.database_version
# print(result)

# result = graph_eda.neo4j_graph.schema
# print(type(result))
# print(len(result))
# print(result.keys())
# print(result['Customer'])



# result = graph_eda.database_indexes()
# print(type(result))
# print(graph_eda.result_cache["database_indexes"])

# result = graph_eda.database_constraints()
# print(type(result))
# print(graph_eda.result_cache["database_constraints"])



############################
# DATA EXPLORATION FUNCTIONS
############################

result = graph_eda.neo4j_graph.schema
for key, value in result.items():
    if value["type"] == "node":
        print(key, value['count'])

# result = graph_eda.node_count()
# print(type(result))
# print(result)
# print("node count:", graph_eda.result_cache["node_count"])

result = graph_eda.node_label_counts()
# print(type(result))
# print(result)
# print(graph_eda.result_cache["node_label_counts"])
print('Database Node Label Counts:')
for item in graph_eda.result_cache["node_label_counts"]:
    print(item['label'], ":", item['count'])



# result = graph_eda.relationship_type_counts()
# print(type(result))
# print(result)

# graph_eda.multi_label_nodes()
# print(type(graph_eda.result_cache["multi_label_nodes"]))
# print(graph_eda.result_cache["multi_label_nodes"])

# graph_eda.node_properties()
# print(type(graph_eda.result_cache["node_properties"]))
# print(graph_eda.result_cache["node_properties"][0])

# graph_eda.relationship_properties()
# print(type(graph_eda.result_cache["relationship_properties"]))
# print(graph_eda.result_cache["relationship_properties"][0])

# result = graph_eda.count_disconnected_nodes()
# print(type(result))
# print(graph_eda.result_cache["disconnected_nodes"])

# result = graph_eda.disconnected_node_ids()
# print(type(result))
# print(graph_eda.result_cache["disconnected_node_ids"])