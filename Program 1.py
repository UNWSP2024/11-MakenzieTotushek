# Author: Makenzie Totushek
# Date: 4/15/2026
# Title: GUI Display
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My Favorite Saying")

        self.label1 = tkinter.Label(self.main_window,text = 'So do not fear, for I am with you;')
        self.label2 = tkinter.Label(self.main_window,text = 'do not be dismayed, for I am your God.')
        self.label3 = tkinter.Label(self.main_window,text = 'I will strengthen you and help you;')
        self.label4 = tkinter.Label(self.main_window,text = 'I will uphold you with my righteous right hand.')
        self.label5 = tkinter.Label(self.main_window,text = 'Isaiah 41:10')

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()