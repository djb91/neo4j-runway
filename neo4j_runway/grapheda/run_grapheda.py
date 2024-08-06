# script to test Neo4jGraph Class

# import neo4jrunway functions 
from neo4j_runway.database import Neo4jGraph
from neo4j_runway.utils.read_env import read_environment
from neo4j_runway.utils.test_connection import test_database_connection

# import and read from .env file
import dotenv 
dotenv.load_dotenv()

# print("Connecting to:", read_environment("NEO4J_URI"))

# credentials = {"username": read_environment("NEO4J_USERNAME"),
#                 "password": read_environment("NEO4J_PASSWORD"),
#                 "uri": read_environment("NEO4J_URI")
#                 }

# response = test_database_connection(credentials=credentials)
# print(response)

from neo4j_runway.grapheda.grapheda import GraphEDA

# neo4j_graph = Neo4jGraph()

neo4j_graph = Neo4jGraph(
        username=read_environment("NEO4J_USERNAME"),
        password=read_environment("NEO4J_PASSWORD"),
        uri=read_environment("NEO4J_URI"),
    )

graph_eda = GraphEDA()
response = graph_eda.count_node_labels()
print(response)


