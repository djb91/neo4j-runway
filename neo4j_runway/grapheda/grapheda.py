"""
The GraphEDA module performs Graph Exploratory data analysis
on the LLM-created Neo4j graph database. 

The purpose of GraphEDA is to understand the characteristics 
of the data in graph form (nodes, relationships, and properties). 
It also helps identify errors and outliers in the data. 
"""

import pandas as pd
import os
from typing import Dict, List, Any, Union
from neo4j_runway.database.neo4j import Neo4jGraph
import logging
import neo4j 

class GraphEDA:
    """
    The GraphEDA module performs Graph Exploratory data analysis on the created Neo4j graph database.
    """
    def __init__(self, neo4j_graph: Neo4jGraph):
        self.neo4j_graph = neo4j_graph
        self.result_cache = dict()  # cache results in raw format 
        logging.getLogger("neo4j").setLevel(logging.CRITICAL)
    
    # DATA EXPLORATION FUNCTIONS
    # count nodes by label
    def count_node_labels(self, as_df: bool = False):
        query = """MATCH (n) 
                   WITH n, labels(n) as node_labels
                   WITH node_labels[0] as uniqueLabels
                   RETURN uniqueLabels, count(uniqueLabels) as count
                   ORDER BY count DESC"""
        if as_df == True:
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query, 
                                           result_transformer_= neo4j.Result.to_df)
                    return response
            except Exception:
                self.neo4j_graph.driver.close()
        
        else:
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query)
                    return [record.data() for record in response]
                
            except Exception:
                self.neo4j_graph.driver.close()


    # DATA QUALITY FUNCTIONS
    def count_disconnected_nodes(self, as_df: bool = False):
        query = """MATCH (n) 
                   WHERE NOT (n)--()
                   RETURN COUNT(n) as nodeCount"""
        
        if as_df == True:
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query, 
                                           result_transformer_= neo4j.Result.to_df)
                    return response
            except Exception:
                self.neo4j_graph.driver.close()
        
        else:
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query)
                    return [record.data() for record in response]
                
            except Exception:
                self.neo4j_graph.driver.close()


    # explicit errors -- something didn't come over correctly
        
        # priority -- things in a graph created from the csv in this session
            # which things are wrong versus the designed graph
            # informative message to the user with pointers to exact issues 
            # optional -- pass the data to an LLM to interpret 
            # future -- have a method that will try to fix the issue  
        
        # future -- things in graph not created with runway
        
    
    # other possible issues