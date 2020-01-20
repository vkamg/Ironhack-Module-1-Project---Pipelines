# Ironhack-Module-1-Project---Pipelines
First Ironhack Project 

## Overview

*The goal of this project is to create a pipeline to analyze the data provided on the forbes 2018 list.*

**Learning objective:** Create a Pipeline and get some hands on experience on working with web scraping through Python: getting, transforming and exporting data.

## Results

**Input**

- A country -- The argparse method has been used to enter variables from the console.
  - Example: python main.py -c "Spain"

**Output**

- A PDF with the following plots:

  1. GDP per capita of the selected country compared to the world average GDP per capita.
  2. The gender distribution of the richest people in the selected country.
  3. The age distribution of the richest people in the selected country.
  4. The distribution by sector of the richest people in the selected country.
  5. The distribution by worth amount of the richest people in the selected country.
  6. The Top 5 richest people in the selected country.
  
## Data applied
  
  1. Database provided in class with data from the 2018 Forbes List.
  2. The GDP per capita data for each country obtained through web scraping         (https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita)

## Procedure

  **1. Acquisition:** Import data from the database and web scraping.
  
  **2. Wrangling:** Data cleaning - Change the data type of the numeric columns (from object to integer or float),      Standardize the data format of each column (ex. gender: F, Female; or age: 27 years old, 1991), etc.
  
  **3.Analysis and Reporting:** Analyse the data and create the plots and PDF with the analised data.
