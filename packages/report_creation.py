import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF


def richest_people(dataframe, country):
    filter_country = dataframe['country'] == country
    result = dataframe[filter_country].nlargest(5, 'worth_amount_(BUSD)')
    return result

def plot1_bar_x(label, BUSD, country):
    plt.figure(figsize=(15,4))
    index = np.arange(len(label))
    plt.bar(index, BUSD)
    plt.ylabel('Billions of USD', fontsize=12)
    plt.xticks(index, label, fontsize=10, rotation=0)
    plt.title(f'The 5 richest people in {country} according to Forbes List (2018)', fontsize=20)
    plt.savefig(f'data/results/5richest.png')
    return f'data/results/5richest.png'

def country_gdp(dataframe, country):
    filter_country = dataframe['country'] == country
    gdp_country_array = dataframe[filter_country]['GDP_BUSD'].unique()
    gdp_country = gdp_country_array[0]
    gdp_unique = dataframe['GDP_BUSD'].unique()
    gdp_mean = round(gdp_unique.mean(), 1)
    list_country_gdp = [gdp_country, gdp_mean]
    return list_country_gdp

def plot2_bar_x(label, BUSD, country):
    plt.figure(figsize=(15,4))
    index = np.arange(len(label))
    plt.bar(index, BUSD)
    plt.ylabel('Billions of USD', fontsize=12)
    plt.xticks(index, label, fontsize=12, rotation=0)
    country = label[0]
    plt.title(f'{country} compared to Average GDP (2018)', fontsize=16)
    plt.savefig(f'data/results/gdpcountry.png')
    return f'data/results/gdpcountry.png'

def gdp_per_capita(dataframe, country):
    filter_country = dataframe['country'] == country
    gdp_percapita_array = dataframe[filter_country]['GDP_per_capita_USD'].unique()
    gdp_percapita = gdp_percapita_array[0]
    gdp_percapita_unique = dataframe['GDP_per_capita_USD'].unique()
    gdp_percapita_mean = round(gdp_percapita_unique.mean(), 1)
    list_gdp_percapita = [gdp_percapita, gdp_percapita_mean]
    return list_gdp_percapita

def plot3_bar_x(label, BUSD, country):
    plt.figure(figsize=(15,4))
    index = np.arange(len(label))
    plt.bar(index, BUSD)
    plt.ylabel('USD', fontsize=12)
    plt.xticks(index, label, fontsize=12, rotation=0)
    plt.title(f'{country} compared to Average GDP per capita (2018)', fontsize=16)
    plt.savefig(f'data/results/gdppercapita.png')
    return f'data/results/gdppercapita.png'

def create_pdf(plot1, plot2, plot3, country):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(3.0,1.0,'Forbes List and GDP report 2018')
    pdf.ln(6)
    images = [plot1, plot2, plot3]
    for image in images:
        pdf.image(image, w=pdf.w/1, h=pdf.h/3.5)
        pdf.ln(0.15)
    pdf.output(f'data/results/report_{country}.pdf')
    return "PDF successfully created. You can find the report in the results folder"



def analysis(dataframe, country):
    print("Generating plots and report...This may take a while")
    plot1 = richest_people(dataframe, country)
    label1 = plot1['name']
    BUSD1 = plot1['worth_amount_(BUSD)']
    richest_people_plot = plot1_bar_x(label1, BUSD1, country)
    BUSD2 = country_gdp(dataframe, country)
    label2 = [f'{country} GDP', 'Average GDP']
    gdp_country_plot = plot2_bar_x(label2, BUSD2, country)
    BUSD3 = gdp_per_capita(dataframe, country)
    label3 = [f'{country} GDP per capita', 'Average GDP per capita']
    gdp_percapita_plot = plot3_bar_x(label3, BUSD3, country)
    create_pdf(richest_people_plot, gdp_country_plot, gdp_percapita_plot, country)
    print("PDF successfully created. You can find the report in the results folder")