import json
from sre_parse import State
import tkinter as tk
import tkinter.messagebox
import math
import customtkinter as ctk
import WindowMenuSelect
import WindowAddNewFood
import WindowRemoveFood

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Cafe System")
        #self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.main_label = ctk.CTkLabel( master=self, 
                                        text_color="black", 
                                        text="CAFE SYSTEM", 
                                        text_font=("Segoe UI Semibold", 40))
        self.main_label.grid(row=0, column = 1)
        self.configure(fg_color="white")

        self.rowconfigure(0, minsize=100)
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=120)

        button_1 = ctk.CTkButton(master=self, fg_color="green", text="Bayar", width=200, height=60, text_font=("Arial", 25), command=WindowMenuSelect.Window_CustomerBayar)
        button_1.grid(row=1, column = 1, pady=10, sticky="ew")

        button_2 = ctk.CTkButton(master=self,text_color="black", fg_color="yellow", text="Tambah makanan", 
                                width=200, height=60, text_font=("Arial", 25), 
                                command=WindowAddNewFood.Window_TambahMakanan)
        button_2.grid(row=2, column = 1, sticky="ew")

        button_3 = ctk.CTkButton(master=self, fg_color="red", text="Buang makanan", 
                                width=200, height=60, text_font=("Arial", 25), 
                                command=WindowRemoveFood.WindowRemoveFood)
        button_3.grid(row=3, column = 1, pady=10, sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()