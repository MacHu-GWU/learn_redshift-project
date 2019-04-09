# -*- coding: utf-8 -*-

import random
from rolex.generator import rnd_datetime_list_high_performance
from sfm.rnd import rand_hexstr


def create_fake_data():
    """
    - id:
    - name:
    - time:
    """
    n_names = 5
    name_pool = ["e%s - This is a long event name" % i for i in range(1, n_names + 1)]

    n = 1000
    id_list = [rand_hexstr(32) for _ in range(n)]
    name_list = [random.choice(name_pool) for _ in range(n)]
    time_list = rnd_datetime_list_high_performance(size=n, start="2018-01-01", end="2018-01-31 23:59:59")
    time_list.sort()

    data = [
        {"id": id, "name": name, "time": time}
        for id, name, time in zip(id_list, name_list, time_list)
    ]
    from pprint import pprint
    pprint(time_list)
    return data


if __name__ == "__main__":
    create_fake_data()