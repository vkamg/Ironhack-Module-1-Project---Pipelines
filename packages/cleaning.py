import pandas as pd
import re

def clean_sourcecolumn(s):
    return s.split('  ==> ')


def create_columns(df_merged):
    df_merged['Source'] = df_merged['Source'].apply(clean_sourcecolumn)
    df_merged['company_name'] = df_merged['Source'].apply(lambda x: x[1:])
    df_merged['company_name'] = df_merged['company_name'].apply(lambda x: x[0])
    df_merged['company_sector'] = df_merged['Source'].apply(lambda x: x[:1])
    df_merged['company_sector'] = df_merged['company_sector'].apply(lambda x: x[0])
    df_merged.drop(columns=['Source'], inplace=True)
    return df_merged


def clean_worthcolumn(df_merged):
    df_merged['worth'] = df_merged['worth'].apply(lambda x: x.split(' '))
    df_merged['worth_unit'] = df_merged['worth'].apply(lambda x: x[1:])
    df_merged['worth_unit'] = df_merged['worth_unit'].apply(lambda x: x[0])
    df_merged["worth_amount_(BUSD)"] = df_merged['worth'].apply(lambda x: x[:1])
    df_merged["worth_amount_(BUSD)"] = df_merged["worth_amount_(BUSD)"].apply(lambda x: x[0])
    df_merged["worth_amount_(BUSD)"] = df_merged["worth_amount_(BUSD)"].astype(float)
    df_merged.drop(columns=['worth_unit', 'worth'], inplace=True)
    return df_merged


def change_age(age):
    if age == None:
        return None
    elif re.search('years old', age) is not None:
        num = re.sub('[a-zA-Z ]', '', age)
        return int(num)
    else:
        year = int(age)
        age_2018 = 2018 - year
        return int(age_2018)


def clean_age(df_merged):
    df_merged['age'] = df_merged['age'].apply(change_age)
    return df_merged


def country_clean(country):
    if country is None:
        return None
    elif re.search('USA', country) is not None:
        return 'United States'
    elif re.search('China', country) is not None:
        return 'China'
    elif re.search('UK', country) is not None:
        return 'United Kingdom'
    elif re.search('UAE', country) is not None:
        return 'United Arab Emirates'
    elif re.search('None', country) is not None:
        return None
    else:
        return country


def clean_countrycolumn(df_merged):
    df_merged['country'] = df_merged['country'].apply(country_clean)
    return df_merged


def drop_nullvalues(df_merged):
    df_merged.dropna(subset=['country'], inplace=True)
    return df_merged


def capitalize(name):
    return name.title()


def clean_namecolumn(df_merged):
    df_merged['name'] = df_merged['name'].apply(capitalize)
    df_merged['lastName'] = df_merged['lastName'].apply(capitalize)
    return df_merged


def df_columns(df_merged):
    columns = ['name', 'worth_amount_(BUSD)', 'country', 'company_sector', 'company_name', 'age']
    df_cleaned = df_merged[columns]
    return df_cleaned


def sort_values(df_cleaned):
    df_cleaned = df_cleaned.sort_values(by='worth_amount_(BUSD)', ascending=False)
    return df_cleaned

def resetindex(df_cleaned):
    df_cleaned.reset_index(drop=True, inplace=True)
    return df_cleaned

def save_to_parquet(df_cleaned):
    df_cleaned.to_parquet(f'../data/processed/cleaned_data.parquet')
    return df_cleaned

def cleaning_dataset(df_merged):
    print("Cleaning the dataset... This may take a while")
    df_merged1 = create_columns(df_merged)
    df_merged2 = clean_worthcolumn(df_merged1)
    df_merged3 = clean_age(df_merged2)
    df_merged4 = clean_countrycolumn(df_merged3)
    df_merged5 = drop_nullvalues(df_merged4)
    df_merged6 = clean_namecolumn(df_merged5)
    df_merged7 = df_columns(df_merged6)
    df_merged8 = sort_values(df_merged7)
    df_cleaned = resetindex(df_merged8)
    return df_cleaned