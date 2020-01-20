import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

def gdp_per_capita(dataframe, country):
    filter_country = dataframe['country'] == country
    gdp_percapita_array = dataframe[filter_country]['GDP_per_capita_USD'].unique()
    gdp_percapita = gdp_percapita_array[0]
    gdp_percapita_unique = dataframe['GDP_per_capita_USD'].unique()
    gdp_percapita_mean = round(gdp_percapita_unique.mean(), 1)
    list_gdp_percapita = [gdp_percapita, gdp_percapita_mean]
    return list_gdp_percapita

def plot_gdp_x(label, BUSD, country):
    plt.figure(figsize=(15,4))
    index = np.arange(len(label))
    plt.bar(index, BUSD)
    plt.ylabel('USD', fontsize=12)
    plt.xticks(index, label, fontsize=12, rotation=0)
    plt.title(f'{country} GDP per capita compared to Average GDP per capita (2018)', fontsize=16)
    plt.savefig(f'data/results/gdppercapita.png')
    return f'data/results/gdppercapita.png'

def gender_distribution(dataframe, country):
    filter_country = dataframe['country'] == country
    plt.figure(figsize=(10,4))
    dataframe[filter_country].groupby('gender')['name'].nunique().plot(kind='bar');
    plt.title(f'The richest people distribution by gender in {country} according to Forbes List (2018)', fontsize=14)
    plt.savefig(f'data/results/gender_distribution.png')
    return f'data/results/gender_distribution.png'

def age_distribution(dataframe, country):
    filter_country = dataframe['country'] == country
    plt.figure(figsize=(12,4))
    dataframe[filter_country]['age'].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.9);
    plt.title(f'The richest age distribution in {country} according to Forbes List (2018)', fontsize=14)
    plt.savefig(f'data/results/age_distribution.png')
    return f'data/results/age_distribution.png'

def sector_distribution(dataframe, country):
    filter_country = dataframe['country'] == country
    plt.figure(figsize=(14,6))
    dataframe[filter_country].groupby('company_sector')['name'].nunique().plot(kind='barh');
    plt.title(f'The richest people sector distribution in {country} according to Forbes List (2018)', fontsize=14)
    plt.savefig(f'data/results/sector_distribution.png')
    return f'data/results/sector_distribution.png'

def worth_amount(dataframe, country):
    filter_country = dataframe['country'] == country
    plt.figure(figsize=(14,4))
    dataframe[filter_country]['worth_amount_(BUSD)'].plot(kind='hist',bins=[0,20,40,60,80,100,120],rwidth=0.8);
    plt.title(f'Worth amount in {country} according to Forbes List (2018)', fontsize=14)
    plt.savefig(f'data/results/worth_amount.png')
    return f'data/results/worth_amount.png'

def richest_people(dataframe, country):
    filter_country = dataframe['country'] == country
    result = dataframe[filter_country].nlargest(5, 'worth_amount_(BUSD)')
    return result

def plot_richest_x(label, BUSD, country):
    plt.figure(figsize=(15,4))
    index = np.arange(len(label))
    plt.bar(index, BUSD)
    plt.ylabel('Billions of USD', fontsize=12)
    plt.xticks(index, label, fontsize=10, rotation=0)
    plt.title(f'The 5 richest people in {country} according to Forbes List (2018)', fontsize=20)
    plt.savefig(f'data/results/5richest.png')
    return f'data/results/5richest.png'

def create_pdf(country, plot1, plot2, plot3, plot4, plot5, plot6):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(3.0,1.0,'Forbes List and GDP report 2018')
    pdf.ln(6)
    images = [plot1, plot2, plot3, plot4, plot5, plot6]
    for image in images:
        pdf.image(image, w=pdf.w/1, h=pdf.h/3.5)
        pdf.ln(0.15)
    pdf.output(f'data/results/report_{country}.pdf')
    return "PDF successfully created. You can find the report in the results folder"

def analysis(dataframe, country):
    print("Generating plots and report...This may take a while")
    BUSD_gdp = gdp_per_capita(dataframe, country)
    label_gdp = [f'{country} GDP per capita', 'Average GDP per capita']
    gdp_percapita_plot = plot_gdp_x(label_gdp, BUSD_gdp, country)
    plot_gender = gender_distribution(dataframe,country)
    plot_age = age_distribution(dataframe,country)
    plot_sector = sector_distribution(dataframe,country)
    plot_worth = worth_amount(dataframe,country)
    richest = richest_people(dataframe, country)
    label_richest = richest['name']
    BUSD_richest = richest['worth_amount_(BUSD)']
    richest_people_plot = plot_richest_x(label_richest, BUSD_richest, country)
    create_pdf(country, gdp_percapita_plot, plot_gender, plot_age, plot_sector, plot_worth, richest_people_plot)
    print("PDF successfully created. You can find the report in the results folder")