"""
Download links from csv files in the sources folder
The csv files must contain an index column with the link in the first column of format:
"<A HREF = https://portal.phmsa.dot.gov/PDFGenerator/getPublicReport/OHMIR_5800-1?INCIDENTID=720164 target=""_blank"">I-2017090112</A> extract link

dependencies:
- pandas

"""

import os
from urllib.request import urlretrieve

import pandas as pd

# generate file paths
file_paths = os.listdir('sources')
file_paths = ['sources/' + file_path for file_path in file_paths]

# read csv files
df_list = [pd.read_csv(file_path, on_bad_lines="skip") for file_path in file_paths]

# loop through dataframes
for df in df_list:

    # set link column
    link_column = df.columns[0]

    # filter out rows with no link
    df = df[df[link_column].notnull()]

    # filter out rows with link with no `http` or `https`
    df = df[df.index.str.contains('http')]

    print(df.head())

    # loop through rows
    for index, row in df.iterrows():
        link_string = index

        # link_string has format  "<A HREF = https://portal.phmsa.dot.gov/PDFGenerator/getPublicReport/OHMIR_5800-1
        # ?INCIDENTID=720164 target=""_blank"">I-2017090112</A> extract link
        link = link_string.split('https')[1]  # split on https and take the second part
        link = link.split('target')[0]  # split on target and take the first part
        link = 'https' + link  # add https back to the link

        print("found link: ", link)

        # download file from link
        # place it in the folder output/<file_name>
        # name it <INCIDENTID>.pdf
        # if the file already exists, skip it

        # sve file using incident id
        incident_id = link.split('INCIDENTID=')[1]

        file_name = str(incident_id).strip() + '.pdf'
        file_path = 'output/' + file_name

        # create folder if it doesn't exist
        if not os.path.exists('output'):
            os.makedirs('output')

        if not os.path.exists(file_path):
            print("downloading file: ", file_name)
            with open(file_path, 'wb') as f:
                urlretrieve(link, file_path)
        else:
            print("file already exists: ", file_name)
