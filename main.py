import tkinter as tk

from screens import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()#tova e samata vizializaciq na prozoreca
    window.geometry('700x700')#razmerite
    window.title('My GUI Shop')#tova e kakvo da pishe vmesto tk
    render_main_screen(window)
    window.mainloop()#staratira
