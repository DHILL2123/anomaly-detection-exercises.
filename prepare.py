import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from env import db,host,password,protocol,user
import os

######### Get Cohorts function #####################
def get_cohorts():
    '''
    Aquire function to pull cohorts data from mysql workbench
    The file is then saved as .csv on your machine.
    '''
    filename = "cohorts.csv"
    mysqlcon=f"{protocol}://{user}:{password}@{host}/curriculum_logs"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
    # read the SQL query into a dataframe
        df = pd.read_sql_query('''
                            select * from cohorts
                            ''', mysqlcon)  
    df.to_csv(filename)
    return df
############# Get Logs function ####################
def get_logs():
    '''
    Aquire function to pull logs data from mysql workbench 
    The file is then saved as .csv to your machine.
    '''
    filename = "logs.csv"
    mysqlcon=f"{protocol}://{user}:{password}@{host}/curriculum_logs"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
    # read the SQL query into a dataframe
        df = pd.read_sql_query('''
                            select * from logs
                            ''', mysqlcon)  
    df.to_csv(filename)
    return df