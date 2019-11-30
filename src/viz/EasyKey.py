from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from src.viz.CsvFileDetails import CsvFileDetails
from src.viz.FileKey import FileKey
from src.utils.file_utils.csv_utils import *


class FilesGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.files_grid = Frame()

        self.files_grid.master.title("Files")
        self.files_grid.master.rowconfigure(5, weight=1)
        self.files_grid.master.columnconfigure(5, weight=1)
        self.files_grid.grid(sticky=W+E+N+S)

        self.file_path_list = []
        self.file_path_checkbox_list = []

        self.files_grid.pack()


        # functionalities
        self.validation = Frame()
        self.button_file_search = Button(self.validation, text="Select File", command=self.load_file,
                                         width=10)
        self.button_file_search.pack()

        self.validation.pack()

        self.result_grid = Frame()
        self.result_grid.pack()


    def load_file(self):
        fname = askopenfilename(filetypes=(("CSV files", "*.csv"),
                                           ("All files", "*.*"),
                                           ))
        if fname:
            try:
                self.add_file(fname)
            except:
                showerror("Open Source File", "Failed to read file_utils\n'%s'" % fname)
            return


    def get_file_details(self, file_analysis):
        root = Tk()
        filesGrid = CsvFileDetails(root, file_analysis)
        filesGrid.mainloop()


    def get_file_key(self, file_analysis):
        root = Tk()
        filesGrid = FileKey(root, file_analysis)
        filesGrid.mainloop()




    def add_file(self, file_path):

        file_analysis = CsvFile(file_path)

        new_file_path = Label(self.files_grid, text=file_path)
        var = IntVar()
        new_checkbox = Checkbutton(self.files_grid, variable=var)
        new_checkbox.select()
        self.file_path_list.append(new_file_path)
        self.file_path_checkbox_list.append(var)
        new_row = len(self.file_path_list) - 1

        new_button_details = Button(self.files_grid, text="Details",
                                          command=lambda: self.get_file_details(file_analysis),
                                          width=10)

        new_button_keys = Button(self.files_grid, text="Compute Key",
                                    command=lambda: self.get_file_key(
                                        file_analysis),
                                    width=10)

        new_file_path.grid(row=new_row, column=0, sticky=W)
        new_checkbox.grid(row=new_row, column=1, sticky=W)
        new_button_details.grid(row=new_row, column=2, sticky=W)
        new_button_keys.grid(row=new_row, column=3, sticky=W)



if __name__ == "__main__":
    filesGrid = FilesGrid()

    filesGrid.mainloop()
