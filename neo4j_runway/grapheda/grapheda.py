"""
The GraphEDA module performs Graph Exploratory data analysis
on the LLM-created Neo4j graph database. 

The purpose of GraphEDA is to understand the characteristics 
of the data in graph form (nodes, relationships, and properties). 
It also helps identify errors and outliers in the data. 
"""

# import pandas as pd

import os
from typing import Dict, List, Any, Union

from neo4j import GraphDatabase

class GraphEDA:
    """
    The GraphEDA module performs Graph Exploratory data analysis on the created Neo4j graph database.
    """

    # will need to pass in data from constructing the graph 
    def __init__(self, neo4j_graph: Neo4jGraph):
        self.neo4j_graph = neo4j_graph
        self.result_cache = dict() 
    # explicit errors -- something didn't come over correctly
        
        # priority -- things in a graph created from the csv in this session
            # which things are wrong versus the designed graph
            # informative message to the user with pointers to exact issues 
            # optional -- pass the data to an LLM to interpret 
            # future -- have a method that will try to fix the issue  
        
        # future -- things in graph not created with runway 
        
        
    # graph summary statistics
    # other possible issues

