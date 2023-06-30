from cProfile import label
import os
os.system("cls")

import tkinter

main_window = tkinter.Tk()

def tekan_aku():
    label2 = tkinter.Label(main_window, text="Aku sudah ditekan ^_^")
    label2.pack ()

label = tkinter.Label(main_window, text="Hallo saya adalah \nGUI sederhana dengan \nmenggunakan python")
tombol = tkinter.Button(main_window, text="Tekan aku",command = tekan_aku)

label.pack ()
tombol.pack ()

main_window.mainloop()



