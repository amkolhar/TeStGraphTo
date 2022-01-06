# Copyright 2021 AtharvKolhar

import pandas as pd
from ruamel.yaml import YAML


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

yaml = YAML()


class TestStat:
    def __init__(self):
        self.config = self.read_yaml_config()

    def read_yaml_config(self):
        with open('./data/config.yaml', 'r') as config:
            data = yaml.load(config)
        return data

    def create_dataframe(self, test_file):
        """

        :param test_file: .csv file
        :return: pandas dataframe
        """

        test_run_name = test_file.split('/')[-1].split('.')[0].replace('test_results_', "")

        # Create a Pandas Dataframe
        test_dataframe = pd.read_csv(test_file)

        # Select the columns using the config file
        test_dataframe = test_dataframe[self.config['columns']]

        # Rename the the test_result column to the run name
        test_dataframe = test_dataframe.rename(columns={"Test Result": test_run_name})

        # Sort the Column = Test Case Name
        test_dataframe = test_dataframe.sort_values(by=['Test Case Name'])

        # print(test_dataframe)
        return test_dataframe

    @staticmethod
    def merge_dataframes(list_of_dfs):
        if len(list_of_dfs) < 2:
            return -1

        org_df = list_of_dfs[0]

        for df_n in range(1, len(list_of_dfs)):
            org_df = pd.merge(org_df, list_of_dfs[df_n],
                              on=['Test Case Name'],
                              suffixes=('_0', '_%s' % df_n),
                              how='outer')

        return org_df


if __name__ == '__main__':
    test_stat_obj = TestStat()

