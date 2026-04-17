# Author: Makenzie Totushek
# Date: 4/17/2026
# Title: Show Info

import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window, text='Show Info', command=self.do_somthing)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()

    def do_somthing(self):
        tkinter.messagebox.showinfo('My Info', info)


info = ('Name: Makenzie Totushek\nAddress: 1234 74th St Seattle, Washington')

if __name__ == "__main__":
    my_gui = MyGUI()