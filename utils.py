import os
import json
import pandas as pd
import logging
from copy import deepcopy

from config import config as cfg

def get_employees_data():
    employees = pd.read_csv(os.path.join(cfg['app_data_dir'], f'employees.csv'))

    return employees

def get_svi_data():
    df_SVI_2020 = pd.read_csv('/Users/jamesswank/Python_Projects/Situational_Awareness/appData/Colorado_SVI_2020.csv')
    df_SVI_2020['YEAR'] = 2020

    return df_SVI_2020

# def get_