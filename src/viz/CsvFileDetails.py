from tkinter import *
from src.utils.file_utils.csv_utils import *
from src.viz.ScrollFrame import VerticalScrolledFrame

class CsvFileDetails(Frame):
    def __init__(self, mw, file_analysis):
        Frame.__init__(self, mw)
        self.root = mw
        self.master.title("CSV file details")

        # init next row to write in
        row = 0

        # grid header definition
        Label(self, text='file attribute').grid(row=row, column=0)
        Label(self, text='attribute value').grid(row=row, column=1)
        row += 1

        # define attributes to display
        attributes = ['path', 'delimiter', 'quotechar', 'escapechar', 'has_header']
        for attribute in attributes:
            Label(self, text=attribute).grid(row=row, column=0, sticky=W)
            Label(self, text=file_analysis.__dict__[attribute]).grid(row=row, column=1, sticky=W)
            row += 1



        # header
        Label(self, text='header').grid(row=row, column=0, sticky=W)

        header_frame = VerticalScrolledFrame(self)
        header_frame.grid(row=row, column=1, sticky=N+E+W+S)

        row_header = 0
        for header in file_analysis.__dict__['header']:
            Label(header_frame.interior, text=header).grid(row=row_header, column=0, sticky=W)
            row_header += 1

        self.pack()



if __name__ == "__main__":

    mw = Tk()

    path = r'C:\Users\sebde\PycharmProjects\easykey\data\loan.csv'
    file_analysis = CsvFile(path)
    filesGrid = CsvFileDetails(mw, file_analysis)
    filesGrid.mainloop()




