import os

import yaml


class ReadData:

    @classmethod
    def read_yml_data(cls, filename):
        data_list = []
        with open("../data" + os.sep + filename, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            data_list.append(data)
        return data_list
