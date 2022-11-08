# MODULE FOR CREATING DATABASE CONNECTIONS AND OPERATIONS
# =======================================================

# LIBRARIES AND MODULES
import sys # To boot the application
import psycopg2 # For database
import json # For converting connection settings to JSON format
import datetime # For handling date and time values
from decimal import Decimal # For handling decimal datatypes with extreme precision


# CLASS DEFINITIONS
class DatabaseOperation():
    """Creates a connection to postgreSQL database and executes SQL commands"""
    
    def __init__(self):
        self.errorCode
