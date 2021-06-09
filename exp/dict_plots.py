import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import json
sys.path.insert(0, '..')

from utils import data
# I will create all my most frequent nearest neighbor trajectory graphs here


# recovery graph
# France, Benin, Australia, Burundi, Cameroon
BASE_PATH = '../COVID-19/csse_covid_19_data/'
trajectories = []
countries = ["Canada", "France", "United Kingdom", "Belize"]
colors = ["-y", "-r", "-b", "-c", "-g", "-m"]

confirmed = os.path.join(
    BASE_PATH, 
    'csse_covid_19_time_series',
    'time_series_covid19_confirmed_global.csv')
confirmed = data.load_csv_data(confirmed)

for val in countries:
    df = data.filter_by_attribute(
        confirmed, "Country/Region", val)
    cases, _ = data.get_cases_chronologically(df)
    trajectories.append(cases)

days = []
i = 0
while i < len(trajectories[0][0]):
    days.append(i)
    i += 1


plt.title('Global Confirmed Trajectories of Most Common M.NNs (KNN-D)')
plt.xlabel('Days since 1/22/2020')
plt.ylabel('Cumulative Confirmed Cases by Country')
j = 0
while j < len(trajectories):
    plt.plot(days, trajectories[j][0], colors[j], label=countries[j])
    j += 1
plt.legend(loc="upper left")
plt.savefig('global confirmed knn diff')

