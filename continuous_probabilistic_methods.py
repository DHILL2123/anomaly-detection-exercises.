import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


################################## Get upper and lower fence for outliers #####################################################
def get_lower_and_upper_bounds(df, col, k=1.5):
    '''
    get_fences takes in a dataframe and a string literal
    df, a pandas dataframe
    k, an integer representing the fence for our method
    col, a string literal represening a column name
    returns the lower and upper fences of a series
    '''
    col = ['Temperature','Rainfall','Flyers','Price','Sales']
    q1 = df[col].quantile(.25)
    q3 = df[col].quantile(.75)
    iqr = q3 - q1
    lower_fence = q1 - iqr*k
    upper_fence = q3 + iqr*k
    
    return lower_fence, upper_fence
################################# Get outliers outside of lower and upper fence ################################################
def lower_and_upper_outliers(df,cols,k=1.5):
    '''
    Takes in a dataframe and list of numeric cols, and k=1.5 as parameters
    the lower and upper outliers for each column are returned 
    '''
    my_fences = {}
    cols = ['Temperature','Rainfall','Flyers','Price','Sales']
    for col in cols:
        my_fences[col] = get_lower_and_upper_bounds(df,col,k=k)
        print(f'For feature {col}')
        print(df[
        (df[col] < my_fences[col][0]) \
        | (df[col] > my_fences[col][1])])
        print('========================')