import pandas as pd








def import_newdata(url2):
    gdp_data = pd.read_html(url2)
    gdp_dataset = gdp_data[1]
    return gdp_dataset

def clean_gdp(gdp):
    if gdp != '-':
        return float(gdp)
    else:
        return None

def clean_data(gdp_dataset):
    gdp_dataset['GDP_BUSD'] = gdp_dataset['GDP 2018 (billions of $)']['Nominal'].apply(clean_gdp)
    gdp_dataset['GDP_per_capita_USD'] = gdp_dataset['GDP per capita 2018 ($)']['Nominal'].apply(clean_gdp)
    gdp_dataset['country'] = gdp_dataset['Country/Economy']['Country/Economy']
    columns = ['country', 'GDP_BUSD', 'GDP_per_capita_USD']
    gdp_dataset_cleaned = gdp_dataset[columns]
    gdp_dataset_cleaned.columns = gdp_dataset_cleaned.columns.droplevel(1)
    gdp_dataset_cleaned.dropna(subset=['GDP_BUSD'], inplace=True)
    return gdp_dataset_cleaned

def merge_newdata(df_forbeslist, gdp_dataset_cleaned):
    df_forbeslist_gdp = pd.merge(df_forbeslist, gdp_dataset_cleaned, on='country')
    return df_forbeslist_gdp


def import_data(df_forbes, url_new_data):
    print("Merging Forbes list data with GDP data... ")
    gdp_table = import_newdata(url_new_data)
    df_gdp_cleaned = clean_data(gdp_table)
    df_forbes_gdp = merge_newdata(df_forbes, df_gdp_cleaned)
    return df_forbes_gdp



