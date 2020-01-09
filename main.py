import argparse

from packages.acquisition import create_dataset
from packages.cleaning import cleaning_dataset
from packages.newdata import import_data
from packages.report_creation import analysis


def main(country):
    data = create_dataset('/data/raw/veronicamg.db')
    data_cleaned = cleaning_dataset(data)
    data_imported = import_data(data_cleaned,'http://statisticstimes.com/economy/gdp-indicators-2018.php')
    analysis(data_imported, country)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This pipeline creates a report on the forbes list and its relationship to a country's gross domestic product")
    parser.add_argument('-c','--country', dest='country', default= None, type=str,required=True, help='Country selected to create the report')
    args = parser.parse_args()

    if isinstance(args.country, str):
        main(args.country)
    else:
        print('You have to specify the argument -c with the country for which you want the report information')







