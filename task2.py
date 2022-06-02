"""
Created on 2022-06-02
@author: chy
"""

import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./task2_data.csv"
NEEDED_PRODUCT = "pink morsel"

with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # write three fields
    header = ["Sales", "Date", "Region"]
    writer.writerow(header)

    # iterate all csv file in data directory
    file_list = os.listdir(DATA_DIRECTORY)
    # sort csv file in directory
    file_list.sort()

    for file in file_list:

        # change csv file path
        domain = os.path.abspath(DATA_DIRECTORY)
        path = os.path.join(domain, file)
        # print(path)

        # open csv file
        with open(path, "r") as input_file:
            reader = csv.reader(input_file)

            # read from second row
            next(reader)
            for row in reader:
                product = row[0]
                raw_price = row[1]
                quantity = row[2]
                date = row[3]
                region = row[4]

                if product == NEEDED_PRODUCT:
                    # remove $
                    price = float(raw_price[1:])
                    sale = price * int(quantity)

                    output_row = [sale, date, region]
                    writer.writerow(output_row)

            input_file.close()

    output_file.close()
