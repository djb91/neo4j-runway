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

print("##########################################")
print("# Neo4j Exploratory Data Analysis Report")
print("##########################################")

############################
# DATABASE DETAILS 
############################

print("\n########## DATABASE DETAILS ##########")

graph_eda.database_version()

result = graph_eda.database_indexes()

print("\nNode Indexes:")
ctr = 0
for item in result:
    if item['entityType'] == 'NODE' and item['labelsOrTypes'] is not None:
        ctr += 1
        print(item['labelsOrTypes'], ":", item['properties'])
print("Node Indexes Count:", ctr)

print("\nRelationship Indexes:")
ctr = 0
for item in result:
    if item['entityType'] == 'RELATIONSHIP' and item['labelsOrTypes'] is not None:
        ctr += 1
        print(item['labelsOrTypes'], ":", item['properties'])
if ctr > 0:
    print("Relationship Indexe Count:", ctr)
else:
    print("No relationship indexes in database.")

print("\nDatabase Constraints:")
_ = graph_eda.database_constraints()
if len(graph_eda.result_cache["database_constraints"]) == 0:
    print("No constraints in database.")
else:
    print(pd.DataFrame(graph_eda.result_cache["database_constraints"])
          .loc[:, ['name', 'type', 'entityType', 'labelsOrTypes', 'properties']]
          .to_string(index=False)
          )


############################
# DATA EXPLORATION FUNCTIONS
############################

print("\n########## NODE DETAILS ##########")

_ = graph_eda.node_count()
print("\nTotal nodes in database:", graph_eda.result_cache["node_count"])

_ = graph_eda.node_label_counts()
print("\nNode counts by label:")
for item in graph_eda.result_cache["node_label_counts"]:
    print(item['label'], ":", item['count'])

print('\nMulti-Label Nodes:')
_ = graph_eda.multi_label_nodes()
if len(_) == 0:
    print("No multi-label nodes in graph")
else:
    print(graph_eda.result_cache["multi_label_nodes"])

print('\nNode Properties:')
_ = graph_eda.node_properties()
print(pd.DataFrame(graph_eda.result_cache["node_properties"])
      .sort_values(by='nodeLabels', ascending=True)
      .to_string(index=False))

print("\n########## RELATIONSHIP DETAILS ##########")

_ = graph_eda.relationship_count()
print("\nTotal relationships in database:", graph_eda.result_cache["relationship_count"])

print("\nRelationship counts by type:")
_ = graph_eda.relationship_type_counts()
for item in graph_eda.result_cache["relationship_type_counts"]:
    print(item['label'], ":", item['count'])

print("\nRelationship Properties:")
_ =  graph_eda.relationship_properties()
print(pd.DataFrame(graph_eda.result_cache["relationship_properties"])
      .dropna(subset=['propertyName'])
      .to_string(index=False))

############################
# DATA QUALITY FUNCTIONS
############################


print("\n########## DATA QUALITY ##########")

_ = graph_eda.unlabeled_node_count()
if graph_eda.result_cache["unlabeled_node_count"] == 0:
    print("\nAll nodes in database have labels.")
else:
    print("\nUnlabeled nodes in database:", graph_eda.result_cache["unlabeled_node_count"])


_ = graph_eda.count_disconnected_nodes()
print('\nCount of disconnected nodes by label:')
for item in graph_eda.result_cache["disconnected_nodes"]:
    print(item['nodeLabel'], ":", item['count'])

_ = graph_eda.disconnected_node_ids()
print('\nDisconnected node ids:')
print(pd.DataFrame(graph_eda.result_cache["disconnected_node_ids"])
      .to_string(index=False))
# for item in graph_eda.result_cache["disconnected_node_ids"]:
#     print(item['nodeLabel'], ":", item['node_id'])

print("\n########## GRAPH STATISTICS ##########")

_ = graph_eda.node_degree()

print("\nDistribution of Node Out-Degrees:")
print(pd.DataFrame(graph_eda.result_cache["node_degrees"])['outDegree']
      .describe(percentiles=[0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
      .round(2)
      )

print("\nNodes with Highest Out-Degrees:")
print(pd.DataFrame(graph_eda.result_cache["node_degrees"])
                   .sort_values(by='outDegree', ascending=False)
                   .head(5)
                   .to_string(index=False))

print("\nDistribution of Node In-Degrees:")
print(pd.DataFrame(graph_eda.result_cache["node_degrees"])['inDegree']
      .describe(percentiles=[0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
      .round(2)
      )

print("\nNodes with Highest In-Degrees:")
print(pd.DataFrame(graph_eda.result_cache["node_degrees"])
                   .sort_values(by='inDegree', ascending=False)
                   .head(5)
                   .to_string(index=False))
