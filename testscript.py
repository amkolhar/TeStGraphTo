# Copyright 2021 AtharvKolhar

import os
import statgui
import teststat
from tkinter import *


class TestScript:
    def __init__(self):
        self.test_stat_obj = teststat.TestStat()
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.test_result_dir = self.dir_path + '/test_result_dir/'
        self.test_files = self.create_test_file_list()
        self.test_df = self.create_test_df()

        self.my_window = Tk()
        statgui.StatGUI(self.my_window, self.test_df)
        self.my_window.mainloop()

    def create_test_file_list(self):
        filenames = os.listdir(self.test_result_dir)
        return [filename for filename in filenames if filename.endswith('.csv')]

    def create_test_df(self):
        test_df_list = []
        for t_file in self.test_files:
            test_df = self.test_stat_obj.create_dataframe('%s/%s' % (self.test_result_dir, t_file))
            test_df_list.append(test_df)

        test_df = self.test_stat_obj.merge_dataframes(test_df_list)
        return test_df


if __name__ == '__main__':
    TestScript()
