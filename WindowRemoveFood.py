import json
from sre_parse import State
import tkinter as tk
import tkinter.messagebox
import math
import customtkinter as ctk
from tkinter.messagebox import askyesno

class WindowRemoveFood(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.main_label = ctk.CTkLabel( master=self, 
                                        text="BUANG MAKANAN", 
                                        text_font=("Segoe UI Semibold", 40))
        self.main_label.grid(row=0, column = 1)

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(2, minsize=100)

        food_dict = self.read_food_from_db()
        food_dict = [key for key in food_dict.keys()]

        combobox = ctk.CTkOptionMenu(master=self,
                                       values=food_dict,
                                       command=self.optionmenu_callback,
                                       text_font=("Arial", 25),
                                       dropdown_text_font=("Arial", 25))
        
        combobox.grid(row=1, column=1, ipadx=50)
        
        self.submit_button = ctk.CTkButton(master=self, text="Buang", 
        width=200, height=60, text_font=("Arial", 25), 
        command=self.remove_food_from_db, fg_color="green")
        self.submit_button.grid(row=2, column=1, pady=10)

    def confirmation_dialog(self):
        answer = askyesno("Confirm makanan",
        "Betul ke nak buang" + self.food_to_remove)
        self.option_add('*Dialog.msg.font', 'Helvetica 20')
        return answer

    def optionmenu_callback(self, choice):
        self.food_to_remove = choice
    
    def read_food_from_db(self) :
        food_dict = {}
        with open("foods.json", "r") as file:
            food_dict = json.load(file)
        return food_dict

    def remove_food_from_db(self):
        food_dict = {}
        with open("foods.json", "r") as file:
            food_dict = json.load(file)

        print(self.food_to_remove)

        answer = self.confirmation_dialog()

        if not answer:
            return

        food_dict.pop(self.food_to_remove)

        with open("foods.json", "w") as file:
            file.write(str(food_dict).replace("'", '"'))