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
    
    ############################
    # DATA EXPLORATION FUNCTIONS
    ############################
    # count nodes by label
    def count_node_labels(self, as_df: bool = False):
        """
        Count the number of nodes for each unique label in the graph.
        Parameters:
            as_df (bool): If True, return the result as a pandas DataFrame. 
                          If False, return the result as a list of dictionaries.
        Returns:
            If as_df is True:
                pandas.DataFrame: A DataFrame containing the unique labels and their counts.
            If as_df is False:
                list: A list of dictionaries, where each dictionary contains the unique label and its count.
        """

        query = """MATCH (n) 
                   WITH n, labels(n) as node_labels
                   WITH node_labels[0] as uniqueLabels
                   RETURN uniqueLabels, count(uniqueLabels) as count
                   ORDER BY count DESC"""
        
        if as_df == True: # NOTE: Return as dataframe not working yet
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query=query, 
                                           driver_config={'result_transformer': 'neo4j.Result.to_df'})
                if response is not None:
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


    ############################
    # DATA QUALITY FUNCTIONS
    ############################

    # count disconnected nodes
    def count_disconnected_nodes(self, as_df: bool = False):
        """
        Count the number of disconnected nodes in the graph.
        Parameters:
        - as_df (bool): If True, return the result as a dataframe. Default is False.
        Returns:
        - If as_df is True, returns the result as a dataframe.
        - If as_df is False, returns a list of dictionaries, 
            where each dictionary represents a record in the response.
        """

        query = """MATCH (n) 
                   WHERE NOT (n)--()
                   RETURN COUNT(n) as nodeCount"""
        
        if as_df == True: # NOTE: Return as dataframe not working yet
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query=query, 
                                           driver_config={'result_transformer': 'neo4j.Result.to_df'})
                if response is not None:
                    return response
            except Exception:
                self.neo4j_graph.driver.close()
        
        else:
            try:
                with self.neo4j_graph.driver.session() as session:
                    response = session.run(query=query)
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