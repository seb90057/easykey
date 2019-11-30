from tkinter import *
from src.utils.file_utils.csv_utils import *
from src.utils.tools.grouping import *


class FileKey(Frame):
    def __init__(self, mw, file_analysis):
        Frame.__init__(self, mw)
        self.root = mw
        self.master.title("CSV file keys")

        df = file_analysis.get_df()
        self.best_combinations = get_best_keys(search_key(df)[1])

        dist = self.best_combinations[0]
        combinations = self.best_combinations[1]

        print(combinations)

        row = 0
        col = 0
        # header
        Label(self, text='distance').grid(row=row, column=col, sticky=W)
        row += 1

        # fill result
        for combination in combinations:
            Label(self, text=dist).grid(row=row, column=col, sticky=W)
            col += 1
            for value in combination:
                Label(self, text=value).grid(row=row, column=col, sticky=W)
                col += 1
            col = 0
            row += 1


        self.pack()


if __name__ == "__main__":

    mw = Tk()

    path = r'C:\Users\sebde\PycharmProjects\easykey\data\loan.csv'
    file_analysis = CsvFile(path)
    filesGrid = FileKey(mw, file_analysis)
    filesGrid.mainloop()




