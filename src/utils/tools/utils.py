import pandas as pd
import itertools
import time
import random
import csv

SAMPLE_ROW_NUMBER = 10000

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f s' % \
                  (method.__name__, (te - ts)))
        return result
    return timed

#
# # @timeit
# def load_csv(path, sep=None):
#     if sep is None:
#         sep = sniff_csv(path)
#
#     data = pd.read_csv(path, sep=sep)
#     return data
#
#
# # @timeit
# def load_csv_sample(path, sep=None, sample_row_nb=SAMPLE_ROW_NUMBER):
#     if sep is None:
#         sep = sniff_csv(path)
#
#     line_nb = sum(1 for line in open(path, encoding='utf8')) - 1
#
#     if line_nb <= sample_row_nb:
#         return load_csv(path, sep=sep)
#     else:
#         skip = sorted(random.sample(range(1, line_nb + 1),
#                                     line_nb - sample_row_nb))
#         data = pd.read_csv(path, skiprows=skip, sep=sep)
#
#         return data
#
#
# def sniff_csv(path):
#     with open(path) as csv_file:
#         dialect = csv.Sniffer().sniff(csv_file.read(1024))
#
#     delimiter = dialect.delimiter
#
#     return delimiter
#
#
# def load_multiple_csv(path_list, sep=None, sample_row_nb=SAMPLE_ROW_NUMBER):
#     file_nb = len(path_list)
#     sample_row_nb_by_file = int(sample_row_nb/file_nb) + 1
#
#     data_list = []
#     header = None
#
#     for path in path_list:
#         if sep is None:
#             sep = sniff_csv(path)
#         data = load_csv_sample(path, sep=sep, sample_row_nb=sample_row_nb_by_file)
#         if header is None:
#             header = data.columns
#
#         if compare_list(header, data.columns):
#             data_list.append(data)
#         else:
#             raise Exception
#
#     result = pd.DataFrame()
#     result = result.append(data_list, ignore_index=True)
#
#     return result.drop_duplicates()
#
#
# def compare_list(list_1, list_2):
#     list_1_size = len(list_1)
#     list_2_size = len(list_2)
#     if list_1_size != list_2_size:
#         return False
#
#     for i_1, elt_1 in enumerate(list_1):
#         if elt_1 != list_2[i_1]:
#             return False
#
#     return True
#
#
# # @timeit
# def get_header(data):
#     return list(data.columns)
#
#
# # @timeit
# def row_number(data):
#     return len(data.index)
#
#
# # @timeit
# def group_by_number(data, group_list):
#     gb = group_by(data, group_list)
#     return len(gb)
#
#
# # @timeit
# def group_by(data, group_list):
#     return data.groupby(group_list)
#
#
# @timeit
def get_combinations(header, nb):
    return list(itertools.combinations(header, nb))
#
# @timeit
# def get_all_combinations(headers):
#     combinations_dict = {}
#
#     for i, header in enumerate(headers):
#         combinations_dict[i+1] = []
#         combinations_dict[i + 1].append(get_combinations(headers, i+1))
#
#     return combinations_dict
#
#
# @timeit
# def compute_combination_result(data, nb):
#     header = get_header(data)
#     combination_list = get_combinations(header, nb)
#     data_size = row_number(data)
#     result = {}
#     result['combination'] = []
#     result['row_nb'] = []
#     result['dist'] = []
#     result['combination_len'] = []
#
#     for c in combination_list:
#         gb_nb = group_by_number(data, list(c))
#         result['combination'].append(c)
#         result['row_nb'].append(gb_nb)
#         result['dist'].append(data_size-gb_nb)
#         result['combination_len'].append(len(c))
#
#     return pd.DataFrame(data=result)
#
#
# @timeit
# def compute_all_combination_result(data):
#     header = get_header(data)
#     df_list = []
#     for i in range(len(header)):
#         df_list.append(compute_combination_result(data, i+1))
#
#     return pd.concat(df_list)
#
#
# @timeit
# def estimate_optimum(data):
#     combination = None
#     dist = None
#     combination_len = None
#
#     header_nb = len(get_header(data))
#     for nb in range(header_nb):
#         stat = compute_combination_result(data, nb+1)
#         for index, row in stat.iterrows():
#             row_combination = row['combination']
#             row_dist = row['dist']
#             row_combination_len = row['combination_len']
#
#             if not combination:
#                 combination = row_combination
#                 dist = row_dist
#                 combination_len = row_combination_len
#             else:
#                 if dist == row_dist:
#                     if combination_len > row_combination_len:
#                         dist = row_dist
#                         combination_len = row_combination_len
#                         combination = row_combination
#                 elif dist > row_dist:
#                     dist = row_dist
#                     combination_len = row_combination_len
#                     combination = row_combination
#             if dist == 0:
#                 return combination, dist
#         return combination, dist


#
# if __name__ == '__main__':
#     path = r'C:\Users\sebde\PycharmProjects\easykey\data\test_multiple_key.csv'
#     path_list = [r'C:\Users\sebde\PycharmProjects\easykey\data\test_multiple_key.csv',
#                  r'C:\Users\sebde\PycharmProjects\easykey\data\test_multiple_key_2.csv']
#
#     # data = load_csv_sample(path, sep=';')
#     # data = load_csv_sample(path, sep=';', sample_row_nb=5)
#
#     data = load_multiple_csv(path_list, sep=';', sample_row_nb=2)
#     print(data)
