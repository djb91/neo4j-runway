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

    Attributes
    ----------
    None
    """
    def __init__(self, neo4j_graph: Neo4jGraph) -> None:
        """
        Constructor for the GraphEDA class.

        Parameters
        ----------
        neo4j_graph : Neo4jGraph
            The Neo4jGraph object to perform the analysis on.

        """
        self.neo4j_graph = neo4j_graph
        self.result_cache = dict()  # cache results in raw format 
        logging.getLogger("neo4j").setLevel(logging.CRITICAL)
    

    ############################
    # DATA EXPLORATION FUNCTIONS
    ############################

    # count nodes by label
    def node_label_counts(self) -> List[Dict[str, Any]]:
        """
        Count the number of nodes for each unique label in the graph.
        Parameters:
            None
        Returns:
            list: A list of dictionaries, where each dictionary contains the unique node label 
            in the database as "label" along with the corresponding node count as "count".
        """

        query = """MATCH (n) 
                   WITH n, labels(n) AS node_labels
                   WITH node_labels[0] AS uniqueLabels
                   RETURN uniqueLabels AS label, COUNT(uniqueLabels) AS count
                   ORDER BY count DESC"""
        
        try:
            with self.neo4j_graph.driver.session() as session:
                response = session.run(query)
                response_list = [record.data() for record in response]
                self.result_cache["node_label_counts"] = response_list
                return response_list
            
        except Exception:
            self.neo4j_graph.driver.close()

    # identify multi-label nodes
    def multi_label_nodes(self) -> List[Dict[str, Any]]:
        """
        Identify nodes that have multiple labels in the graph.
        Parameters:
            None
        Returns:
            list: A list of dictionaries, where each dictionary contains the node id as "node_id" 
            and the list of labels for that node as "labels".
        """

        query = """MATCH (n) 
                   WITH n, labels(n) as node_labels
                   WHERE size(node_labels) > 1
                   WITH node_labels as labelCombinations
                   RETURN labelCombinations, count(labelCombinations) as nodeCount
                   ORDER BY nodeCount DESC"""
        
        try:
            with self.neo4j_graph.driver.session() as session:
                response = session.run(query)
                response_list = [record.data() for record in response]
                self.result_cache["multi_label_nodes"] = response_list
                return response_list
            
        except Exception:
            self.neo4j_graph.driver.close()

    # count relationships by type
    def relationship_type_counts(self) -> List[Dict[str, Any]]:
        """
        Count the number of relationships for each unique type in the graph.
        Parameters:
            None
        Returns:
            list: A list of dictionaries, where each dictionary contains the unique relationship type 
            in the database as "label" along with the corresponding count as "count".
        """

        query = """MATCH ()-[r]->()
                   WITH type(r) AS rel_type
                   RETURN rel_type as label, COUNT(rel_type) AS count
                   ORDER BY count DESC"""
        
        try:
            with self.neo4j_graph.driver.session() as session:
                response = session.run(query)
                response_list = [record.data() for record in response]
                self.result_cache["relationship_type_counts"] = response_list
                return response_list
            
        except Exception:
            self.neo4j_graph.driver.close()

    ############################
    # DATA QUALITY FUNCTIONS
    ############################

    # count disconnected nodes
    def count_disconnected_nodes(self) -> List[Dict[str, Any]]:
        """
        Count the number of disconnected nodes in the graph.
        Parameters:
        - None
        Returns:
        - the results as a list of dictionaries, where each dictionary 
        includes a node label and the count of disconnected nodes for that label
        - also appends the results to the result_cache dictionary
        """

        query = """MATCH (n) 
                   WHERE NOT (n)--()
                   WITH n, labels(n) as node_labels
                   WITH node_labels[0] as uniqueLabels
                   RETURN uniqueLabels, count(uniqueLabels) as count
                   ORDER BY count DESC"""
        
        try:
            with self.neo4j_graph.driver.session() as session:
                response = session.run(query=query)
                response_list = [record.data() for record in response]
                self.result_cache["disconnected_nodes"] = response_list
                return response_list
                
        except Exception:
            self.neo4j_graph.driver.close()


    # identify disconnected nodes
    def id_disconnected_nodes(self) -> List[Dict[str, Any]]:
        pass

    # count unlabeled nodes
    def count_unlabeled_nodes(self, as_df: bool = False): 
        pass 


    # explicit errors -- something didn't come over correctly
        
        # priority -- things in a graph created from the csv in this session
            # which things are wrong versus the designed graph
            # informative message to the user with pointers to exact issues 
            # optional -- pass the data to an LLM to interpret 
            # future -- have a method that will try to fix the issue  
        
        # future -- things in graph not created with runway
        
    
    # other possible issues