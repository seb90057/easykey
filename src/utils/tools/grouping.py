
import time
from src.utils.tools.utils import *

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


@timeit
def group_by_fields(data, fields):
    rownb = len(data.index)
    data_group_by = data.groupby(fields)

    df = pd.DataFrame(data_group_by.size().reset_index(name='temp')).drop('temp', 1)

    rownb_group_by = len(df.index)

    return rownb - rownb_group_by, df

# @timeit
def group_by(data_dict, last=[]):
    data = data_dict['data']
    fields = data_dict['fields']

    group_by_combination = get_combinations(fields, nb=len(fields)-1)

    for combination in group_by_combination:
        if combination:
            dist, data_tmp = group_by_fields(data, combination)
            result_data_dict = {'data': data_tmp, 'fields': combination, 'dist': dist}
            last.append(result_data_dict)
            group_by(result_data_dict, last=last)

    return last

@timeit
def group_by_all(data):
    group_by_dict = {'data': data, 'fields': data.columns, 'dist': 0}
    result = group_by(group_by_dict)

    return result


def clean_result(dict_list):
    data = []
    for dict in dict_list:
        data.append([dict['fields'], dict['dist']])

    df = pd.DataFrame(data, columns = ['fields', 'dist'])

    return df


def search_key(data):
    header = data.columns
    dist = len(header)
    combination_dict = {}

    for key_nb in range(1, len(header), 1):
        combinations = get_combinations(header, key_nb)

        if dist == 0:
            return dist, combination_dict

        for combination in combinations:
            combination_size = len(combination)
            current_dist, current_df = group_by_fields(data, combination)

            if current_dist in combination_dict.keys():
                if combination_size in combination_dict[current_dist].keys():
                    combination_dict[current_dist][combination_size]\
                        .append(combination)
                else:
                    combination_dict[current_dist][combination_size] = [combination]
            else:
                combination_dict[current_dist] = {}
                combination_dict[current_dist][combination_size] = [combination]

            if current_dist <= dist:
                dist = current_dist

    return dist, combination_dict


def get_best_keys(combination_dict):
    print('best keys combination : {}'.format(combination_dict.keys()))
    best_dist = min(combination_dict.keys())
    best_combination_size = min(combination_dict[best_dist].keys())
    best_combinations = combination_dict[best_dist][best_combination_size]

    return best_dist, best_combinations



if __name__ == '__main__':

    path = r'C:\Users\sebde\OneDrive\Documents\product_csv.csv'
    data = load_csv(path)
    dist, combination_dict = search_key(data)
    best_dist, best_keys = get_best_keys(combination_dict)

    print(best_dist)
    print(best_keys)
