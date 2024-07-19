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

class GraphEDA:
    """
    The GraphEDA module performs Graph Exploratory data analysis on the created Neo4j graph database.
    """

    def __init__(
        self,
        username: Union[str, None] = None,
        password: Union[str, None] = None,
        uri: Union[str, None] = None,
        database: Union[str, None] = None,
    ):

     """
     The GraphEDA module performs Graph Exploratory data analysis on the created Neo4j graph database.

    Parameters
    ----------
    username : Union[str, None], optional
        The username used to connect to Neo4j, by default None
    password : Union[str, None], optional
        The password used to connect to Neo4j, by default None
    uri : Union[str, None], optional
        The uri of the Neo4j instance, by default None
    database : Union[str, None], optional
        The database within the Neo4j instance to load the data, by default None
        """