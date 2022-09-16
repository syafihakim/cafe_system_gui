import json
from sre_parse import State
import tkinter as tk
import tkinter.messagebox
import math
import customtkinter as ctk

class Window_TambahMakanan(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.main_label = ctk.CTkLabel( master=self, 
                                        text="TAMBAH MAKANAN", 
                                        text_font=("Segoe UI Semibold", 40))
        self.main_label.grid(row=0, column = 1)

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(2, minsize=100)

        entry_food_name = ctk.CTkEntry(self, placeholder_text="Nama Makanan", text_font=("Arial", 30))
        entry_food_name.grid(row=1, column=1, sticky="ew", pady=10, ipady=10)
        entry_food_price = ctk.CTkEntry(self, placeholder_text="Harga", text_font=("Arial", 30))
        entry_food_price.grid(row=2, column=1, sticky="ew", pady=10, ipady=10)
        
        self.submit_button = ctk.CTkButton(master=self, text="Tambah", 
        width=200, height=60, text_font=("Arial", 25), command=lambda :self.add_food_to_db(entry_food_name.get(), entry_food_price.get()), fg_color="green")
        self.submit_button.grid(row=3, column=1, pady=10)
    
    def add_food_to_db(self, food_name, food_price):
        food_dict = {}
        with open("foods.json", "r") as file:
            food_dict = json.load(file)

        food_dict[food_name] = int(food_price)

        with open("foods.json", "w") as file:
            file.write(str(food_dict).replace("'", '"'))