import argparse

def main(country, inform):
    data = create_dataset('../data/raw/veronicamg.db')
    data_cleaned = cleaning(data)
    data_imported = impor(data_cleaned,"https://restcountries.eu/rest/v2/name/")
    data_filtered= filtering(data_imported, year)
    path, path2, path3,path4 = analyze(data_filtered,year)
    file_to_send = pdf(path,path2,path3,path4, 'Helvetica',year,inform)
    emailing(file_to_send, year)





