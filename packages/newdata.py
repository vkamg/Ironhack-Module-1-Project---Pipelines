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
    columns = ['name', 'worth_amount_(BUSD)', 'country', 'company_sector', 'company_name', 'age']
    df_country_clean = df_country[columns]
    return df_country_clean


def import_gdpdata(url2):
    gdp_data = pd.read_html(url2)
    gdp_dataset = gdp_data[1]
    return gdp_dataset

def clean_gdp(gdp):
    if gdp != '-':
        return float(gdp)
    else:
        return None

def clean_datagdp(gdp_dataset):
    gdp_dataset['GDP_BUSD'] = gdp_dataset['GDP 2018 (billions of $)']['Nominal'].apply(clean_gdp)
    gdp_dataset['GDP_per_capita_USD'] = gdp_dataset['GDP per capita 2018 ($)']['Nominal'].apply(clean_gdp)
    gdp_dataset['country'] = gdp_dataset['Country/Economy']['Country/Economy']
    columns = ['country', 'GDP_BUSD', 'GDP_per_capita_USD']
    gdp_dataset_cleaned = gdp_dataset[columns]
    gdp_dataset_cleaned.columns = gdp_dataset_cleaned.columns.droplevel(1)
    gdp_dataset_cleaned.dropna(subset=['GDP_BUSD'], inplace=True)
    return gdp_dataset_cleaned

def merge_gdpdata(df_forbeslist, gdp_dataset_cleaned):
    df_forbeslist_gdp = pd.merge(df_forbeslist, gdp_dataset_cleaned, on='country')
    return df_forbeslist_gdp


def import_data(df_forbes, url_country, url_gdp):
    print("Merging Forbes list data with GDP data... ")
    country_table = import_countrydata(url_country)
    df_country = merge_countrydata(df_forbes, country_table)
    df_country_clean = clean_countrydata(df_country)
    gdp_table = import_gdpdata(url_gdp)
    df_gdp_cleaned = clean_datagdp(gdp_table)
    df_forbes_gdp = merge_gdpdata(df_country_clean, df_gdp_cleaned)
    return df_forbes_gdp



