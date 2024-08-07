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

# result = graph_eda.node_label_counts()
# print(type(result))
# print(result)
# print(graph_eda.result_cache["node_label_counts"])

# result = graph_eda.relationship_type_counts()
# print(type(result))
# print(result)

# graph_eda.multi_label_nodes()
# print(type(graph_eda.result_cache["multi_label_nodes"]))
# print(graph_eda.result_cache["multi_label_nodes"])

# result = graph_eda.count_disconnected_nodes()
# print(type(result))
# # print(result)
# print("disconnected node count:", result[0]['nodeCount'])

