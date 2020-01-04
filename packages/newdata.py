import pandas as pd

def import_newdata(url):
    gdp_data = pd.read_html('url')
    gdp_dataset = gdp_data[1]
    return gdp_dataset

def clean_data(gdp_dataset):
    gdp_dataset['GDP_BUSD'] = gdp_dataset['GDP 2018 (billions of $)']['Nominal']
    gdp_dataset['GDP_per_capita_USD'] = gdp_dataset['GDP per capita 2018 ($)']['Nominal']
    gdp_dataset['country'] = gdp_dataset['Country/Economy']['Country/Economy']
    columns = ['country', 'GDP_BUSD', 'GDP_per_capita_USD']
    gdp_dataset_cleaned = gdp_dataset[columns]
    gdp_dataset_cleaned.columns = gdp_dataset_cleaned.columns.droplevel(1)
    return gdp_dataset_cleaned



