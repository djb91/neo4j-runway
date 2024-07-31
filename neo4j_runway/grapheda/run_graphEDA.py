from grapheda import GraphEDA
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run GraphEDA')
parser.add_argument('--uri', required=True, help='Neo4j URI')
parser.add_argument('--username', required=True, help='Neo4j Username')
parser.add_argument('--password', required=True, help='Neo4j Password')
parser.add_argument('--database', required=True, help='Neo4j Database')
args = parser.parse_args()

# Initialize the GraphEDA object with your credentials
graph_eda = GraphEDA(
    username=args.username,
    password=args.password,
    uri=args.uri,
    database=args.database
)

# Call the connect_to_neo4j function
graph_eda.connect_to_neo4j()

# Confirm the connection to the Neo4j database
try:
    graph_eda.confirm_neo4j_connection()
    print("Connection to Neo4j confirmed")
except Exception as e:
    print(f"Failed to confirm connection: {e}")

# Close the connection to Neo4j 
graph_eda.close()

