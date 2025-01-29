import os

from datetime import datetime, timedelta

file_name = "data.txt"
base_path = os.path.dirname(__file__)
file_path = os.path.join(
    os.path.dirname(os.path.dirname(base_path)),
    "eugene_okulik",
    "hw_13",
    file_name
)
dates = {}


def read_file(filename):
    with open(filename, "r") as data_file:
        for line in data_file.readlines():
            yield line


def make_date(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")


for data_line in read_file(file_path):
    num = data_line[0]
    new_date = data_line[3: 29]
    dates[num] = new_date

# 1. Print date but a week later.
print(make_date(dates["1"]) + timedelta(weeks=1))

# 2. Print what day of the week it will be
print(make_date(dates["2"]).strftime("%A"))

# 3. Print how many days ago was this date
print((datetime.now() - make_date(dates["3"])).days)
