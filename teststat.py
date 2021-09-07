# Copyright 2021 AtharvKolhar

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class TestStat:
    def __init__(self):
        pass

    def create_dataframe(self, test_file):
        """

        :param test_file: .csv file
        :return: pandas dataframe
        """

        # Create a Pandas Dataframe
        test_dataframe = pd.read_csv(test_file)

        # Remove the Columns = ['% Rate', 'Test Suite']
        test_dataframe = test_dataframe.drop(columns=['% Rate', 'Test Suite'])

        # Sort the Column = Test Case Name
        test_dataframe = test_dataframe.sort_values(by=['Test Case Name'])

        # print(test_dataframe)
        return test_dataframe

    def merge_dataframes(self, list_of_dfs):
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

