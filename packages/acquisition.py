import pandas as pd
from sqlalchemy import create_engine

def create_engine_db(sqlitedb_path):
    engine = create_engine(f'sqlite://{sqlitedb_path}')
    return engine


def read_business_info(engine):
    df_business_info = pd.read_sql_query("select * from business_info", engine)
    return df_business_info

def read_personal_info(engine):
    df_personal_info = pd.read_sql_query("select * from personal_info", engine)
    return df_personal_info

def read_rank_info(engine):
    df_rank_info = pd.read_sql_query("select * from rank_info", engine)
    return df_rank_info

def merge_tables(df_business_info, df_personal_info, df_rank_info):
    df_business_personal = pd.merge(df_business_info, df_personal_info, on='Unnamed: 0')
    df_merged = pd.merge(df_business_personal, df_rank_info, on='Unnamed: 0')
    return df_merged

def create_dataset(sqlitedb_path):
    print("Charging dataset...")
    engine_generated = create_engine_db(sqlitedb_path)
    df_business = read_business_info(engine_generated)
    df_personal = read_personal_info(engine_generated)
    df_rank = read_rank_info(engine_generated)
    df_merged = merge_tables(df_business, df_personal, df_rank)
    return df_merged