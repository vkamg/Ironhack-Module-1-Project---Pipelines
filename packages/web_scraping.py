import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def import_countrydata(url1):
    df_country = pd.read_json(url1, orient='records')
    return df_country

def merge_countrydata(df_forbeslist, df_countrydata):
    df_forbeslist_country = pd.merge(df_forbeslist, df_countrydata, on='name')
    return df_forbeslist_country


def clean_countrydata(df_country):
    df_country['country'] = df_country['country_y']
    df_country['age'] = df_country['age_x']
    columns = ['name', 'worth_amount_(BUSD)', 'country', 'age', 'gender', 'company_sector', 'company_name']
    df_country_clean = df_country[columns]
    return df_country_clean


def table_gdp(url2):
    html_gdp = requests.get(url2).content
    soup_gdp = BeautifulSoup(html_gdp, 'lxml')
    rows_gdp = soup_gdp.find_all('tr')
    rows_parsed_gdp = [row.text for row in rows_gdp]
    return rows_parsed_gdp

def parser_gdp(row_text):
    row_text = row_text.replace('\n\n', '\n').strip('\n')
    row_text = re.sub('\[\d\]', '', row_text)
    return list(map(lambda x: x.strip(), row_text.split('\n')))

def dataframe_gdp(parsed_gdp):
    colnames_gdp = parsed_gdp[199]
    data_gdp = parsed_gdp[200:391]
    df_gdp = pd.DataFrame(data_gdp, columns=colnames_gdp)
    return df_gdp

def clean_df_gdp(df_gdp):
    df_gdp['country'] = df_gdp['Country/Territory'].apply(lambda x: re.sub("\[.*\].*", "", x))
    df_gdp['GDP_BUSD'] = df_gdp['GDP(US$million)'].apply(lambda x: int(re.sub(",|\(.*\).*", "", x)))
    columns = ['country', 'GDP_BUSD']
    df_gdp_clean = df_gdp[columns]
    return df_gdp_clean


def table_percapita(url3):
    html_percapita = requests.get(url3).content
    soup_percapita = BeautifulSoup(html_percapita, 'lxml')
    rows_percapita = soup_percapita.find_all('tr')
    rows_parsed_percapita = [row.text for row in rows_percapita]
    return rows_parsed_percapita


def parser_percapita(row_text):
    row_text = row_text.replace('\n\n', '\n').strip('\n')
    row_text = re.sub('\[\d\]', '', row_text)
    return list(map(lambda x: x.strip(), row_text.split('\n')))

def dataframe_percapita(parsed_percapita):
    colnames_percapita = parsed_percapita[197]
    data_percapita = parsed_percapita[198:386]
    df_percapita = pd.DataFrame(data_percapita, columns=colnames_percapita)
    return df_percapita

def clean_df_percapita(df_percapita):
    df_percapita['country'] = df_percapita['Country/Territory'].apply(lambda x: re.sub("\[.*\].*", "", x))
    df_percapita['GDP_per_capita_USD'] = df_percapita['US$'].apply(lambda x: int(re.sub(",|\(.*\).*", "", x)))
    columns = ['country', 'GDP_per_capita_USD']
    df_percapita_clean = df_percapita[columns]
    return df_percapita_clean

def merge_tables_gdp_percapia(df_gdp_clean, df_percapita_clean):
    df_mergegdp = pd.merge(df_gdp_clean, df_percapita_clean, on='country')
    return df_mergegdp

def merge_forbes_gdp(df_forbes, df_gdp):
    df_forbes_gdp = pd.merge(df_forbes, df_gdp, on='country')
    return df_forbes_gdp



def import_data(df_forbes, url_country, url_gdp, url_percapita):
    print("Merging Forbes list data with GDP data... ")
    country_table = import_countrydata(url_country)
    df_country = merge_countrydata(df_forbes, country_table)
    df_country_clean = clean_countrydata(df_country)
    soup1 = table_gdp(url_gdp)
    rows_parsed_gdp = parser_gdp(soup1)
    parsed_gdp = list(map(lambda x: parser_gdp(x), rows_parsed_gdp))
    df_gdp = dataframe_gdp(parsed_gdp)
    df_gdp_clean = clean_df_gdp(df_gdp)
    soup2 = table_percapita(url_percapita)
    rows_parsed_percapita = parser_percapita(soup2)
    parsed_percapita = list(map(lambda x: parser_percapita(x), rows_parsed_percapita))
    df_percapita = dataframe_percapita(parsed_percapita)
    df_percapita_clean = clean_df_percapita(df_percapita)
    df_mergegdp = merge_tables_gdp_percapia(df_gdp_clean, df_percapita_clean)
    df_forbes_gdp = merge_forbes_gdp(df_country_clean, df_mergegdp)
    return df_forbes_gdp



