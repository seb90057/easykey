import csv
import json
import pandas as pd

class CsvFile:

    def __init__(self, path):
        self.path = path
        with open(path, errors='ignore') as csv_file:
            sniffer = csv.Sniffer()
            csv_file_lines = csv_file.readlines(100)
            csv_file_sample = '\n'.join(csv_file_lines)
            self.dialect = sniffer.sniff(csv_file_sample)
            self.has_header = sniffer.has_header(csv_file_sample)
            self.delimiter = self.dialect.delimiter
            self.quotechar = self.dialect.quotechar
            self.escapechar = self.dialect.escapechar

            if self.has_header:
                csv_file.seek(0)
                reader = csv.reader(csv_file, self.dialect)
                self.header = next(reader)
            else:
                self.header = None


    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


    def get_df(self):
        df = pd.read_csv(self.path, dialect=self.dialect, error_bad_lines=False)
        return df



if __name__ == '__main__':
    path = r'C:\Users\sebde\PycharmProjects\easykey\data\loan.csv'

    csv_file = CsvFile(path)

    # print(csv_file.__dict__)
    print(csv_file)

