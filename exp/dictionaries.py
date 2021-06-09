# in this file I will make dictionaries of frequencies for each country being another's
# nearest neighbor.
# then I will graph the cases of the highest ones to get a visualization for what the most common
# nearest neighbors' cases actually look like, and maybe some intuition for why they are the nearest neighbors.

import json

BASE_PATH = '../COVID-19/csse_covid_19_data/'

with open("results/knn_dist_diff_global_deaths.json", "r") as read_file:
    neighbor_data = json.load(read_file)


neighbor_freq_dict = {}

# "Afghanistan": {
#         "minkowski": [
#             "Cambodia"
#         ],
#         "manhattan": [
#             "France"
#         ]
#     }

for country in neighbor_data:
    print(country)
    manhattan_nn = neighbor_data[country]['manhattan'][0]
    print(manhattan_nn)
    if manhattan_nn in neighbor_freq_dict:
        neighbor_freq_dict[manhattan_nn] += 1
    else:
        neighbor_freq_dict[manhattan_nn] = 1

with open('results/dict_knn_dist_diff_global_deaths.json', 'w') as f:
    json.dump(neighbor_freq_dict, f, indent=4)
