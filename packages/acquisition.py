import pandas as pd
from sqlalchemy import create_engine

def create_engine_db(sqlitedb_path):
    print('Creating engine...')
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    return engine


def read_tables(engine):
    print('Reading tables from database...')
    df_business_info = pd.read_sql_query("select * from business_info", engine)
    df_personal_info = pd.read_sql_query("select * from personal_info", engine)
    df_rank_info = pd.read_sql_query("select * from rank_info", engine)
    return df_business_info, df_personal_info, df_rank_info


def merge_tables(df_business_info, df_personal_info, df_rank_info):
    df_business_personal = pd.merge(df_business_info, df_personal_info, on='Unnamed: 0')
    df_merged = pd.merge(df_business_personal, df_rank_info, on='Unnamed: 0')
    return df_merged