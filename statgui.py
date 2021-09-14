# Copyright 2021 AtharvKolhar

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Cursor
from matplotlib.figure import Figure
from tkinter import *
matplotlib.use('TkAgg')


class StatGUI:
    def __init__(self, main_window, test_dataframe):
        self.main_window = main_window
        self.main_window.geometry("1000x500")
        self.test_dataframe = test_dataframe

        self.testcase_list = self.get_testcase_names()

        self.main_window.title("Test Status Graphical Tool (TeStGraphTo)")     # TeStGraphTo
        self.testcase_label = Label(self.main_window, text="Test Case Name: ")
        self.testcase_label.grid(column=1, row=5, columnspan=5)

        self.testcase = StringVar()
        self.testcase.set("None")

        self.testcase_name = OptionMenu(self.main_window, self.testcase, *self.testcase_list)
        self.testcase_name.grid(column=6, row=5, columnspan=10)

        self.plot_graph = Button(self.main_window, text="Plot the Graph", command=self.plot_the_scatter_plot)
        self.plot_graph.grid(column=6, row=25, columnspan=5)

        self.close_button = Button(self.main_window, text="Close", command=self.main_window.quit)
        self.close_button.grid(column=100, row=100, columnspan=5)

    def get_testcase_names(self):
        testcase_list = self.test_dataframe['Test Case Name'].tolist()

        return testcase_list

    def plot_the_scatter_plot(self):
        testcase_name = self.testcase.get()
        x = list(self.test_dataframe)[1:]
        ind = self.testcase_list.index(testcase_name)
        y = (self.test_dataframe.loc[ind]).tolist()[1:]

        fig = Figure(figsize=(8, 4))
        stat_graph = fig.add_subplot(111)
        stat_graph.scatter(x, y, color='blue')
        stat_graph.invert_yaxis()

        stat_graph.set_title(testcase_name, fontsize=16)
        stat_graph.set_ylabel("Status", fontsize=14)
        stat_graph.set_xlabel("Runs", fontsize=14)
        
        canvas = FigureCanvasTkAgg(fig, master=self.main_window)
        canvas.get_tk_widget().grid(column=6, row=50, columnspan=20)
        canvas.draw()

