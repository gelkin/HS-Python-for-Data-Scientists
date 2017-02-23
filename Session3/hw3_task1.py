# task 1
# Create a data structure, which stores retention time of different aminoacids.
# Retention times can be acquired using peak detection algorithms, which you have
# implemented during todays Session and filename annotation.
# You should be aware of the following:
# * False peak detection due to to background noise and presence of supplementary chemical compounds,
# * Retention time shifts.
# * Any other artifacts, which can be present in the data and complicate automatic processing.
from collections import namedtuple

Record = namedtuple("Record", ['time', 'values'])

filename = "./LS_MS_Data_CSV/4T1_MRM_TABL_M3_C13LR_LYS.csv"


def read_file(filename):
    header = []
    content = []
    with open(filename, 'r') as file:
        header = file.readline().split(',')[1:]
        for line in map(lambda s: s.strip('\n'), file.readlines()):
            parts = line.split(',')
            record = Record(parts[0], parts[1:])
            content.append(record)
    return header, content


def get_plotting_data(header, content):
    """ Makes plotting data time-value for each elements. """
    plotting_data = []
    for i in range(len(header)):
        times = []
        values_on_time = []
        for time, values in content:
            values_sum = sum(map(float, values))
            times.append(time)
            values_on_time.append(float(values[i]) / values_sum)
        plotting_data.append((times, values_on_time))
    return plotting_data


def make_variance(plotting_data):
    """ Make mapping time - variance of values of different elements. """
    from statistics import variance

    times, _ = plotting_data[0]
    variance_at_time = []
    for i in range(len(times)):
        vals = []
        for j in range(len(plotting_data)):
            vals.append(plotting_data[j][1][i])
        variance_at_time.append(variance(vals))
    return times, variance_at_time


def calc_diff(start, end, values):
    """ Calculate difference between values on interval [start, end) """

    diff = 0
    for i in range(start, end - 1):
        diff += abs(values[i + 1] - values[i])
    return diff


def get_peak_intervals(times, variance_at_time):
    eps = 0.05
    num = 20
    intervals = []
    start = -1
    for i in range(len(times) - num):
        print(calc_diff(i, i + num, variance_at_time))
        if calc_diff(i, i + num, variance_at_time) < eps:
            if start == -1:
                start = i
        elif start != -1:
            intervals.append((times[start], times[i + num]))
            start = -1
    if start != -1:
        intervals.append((times[start], times[-1]))
    return intervals


# header, content = read_file(filename)
# to_plot_analysed = get_plotting_data(header, content)
# times, res_values = make_variance(to_plot_analysed)
# intervals = get_peak_intervals(times, res_values)
# print(intervals)

class RetentionTime:
    # intervals - contain time bounds of peaks

    def __init__(self, filename):
        header, content = read_file(filename)
        plotting_data = get_plotting_data(header, content)
        times, res_values = make_variance(plotting_data)
        self.intervals = get_peak_intervals(times, res_values)
