import json
from sre_parse import State
import tkinter as tk
import tkinter.messagebox
import math
import customtkinter as ctk

class Window_CustomerBayar(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()    

        self.total_harga = 0
        self.makanan_dict = self.retrieve_food_from_db()
        self.customer_food = ""
        self.senarai_makanan_dict = dict()

        self.create_center_frame().grid(row=0, column=1, sticky="ns", padx=20, pady=10)
        self.create_bottom_frame().grid(row=1, column=1, sticky="ns", padx=20, pady=10)
        
    def create_bottom_frame(self):
        bottom_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        button_clear = ctk.CTkButton(  master=bottom_frame, 
                                            fg_color = "green",
                                            text="Clear All", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            command = self.clearAll)            

        button_clear.grid(row=0, column = 0)
        pay_button = ctk.CTkButton(  master=bottom_frame, 
                                            fg_color = "green",
                                            text="Pay", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            command = self.open_pay_window)  
        pay_button.grid(row=0, column = 1)
        return bottom_frame

    def create_center_frame(self):
        # ----------- MAIN FRAME -------------
        main_middle_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        main_middle_frame.rowconfigure(0, weight=1)
        main_middle_frame.rowconfigure(1, weight=1)
        main_middle_frame.columnconfigure(0, minsize=500)

        # ----------- TOP HALF OF MAIN FRAME -------------
        top_middle_frame = ctk.CTkFrame(master=main_middle_frame, fg_color=self.fg_color)
        top_middle_frame.grid(row=0, column=0, sticky="nsew")
        top_middle_frame.columnconfigure(0, weight=1)
        main_label = ctk.CTkLabel(master=top_middle_frame, text="Customer Bayar", text_font=("Consolas", 25))
        main_label.grid(row=0, column=0, sticky="ew")

        # Total Price Entry
        self.entry_total_price = ctk.CTkEntry(top_middle_frame, placeholder_text="Total Harga", text_font=("Arial", 30))
        self.entry_total_price.grid(row=1, column=0, sticky="ew")
        
        # List Of Food TextArea with scrollbar
        self.text_field_total_price = tkinter.Text(master=top_middle_frame, highlightthickness=0, font=("Consolas", 27), height=5, width=12)
        self.text_field_total_price.grid(row=2, column=0, sticky="nsew", pady=15)
        ctk_textbox_scrollbar = ctk.CTkScrollbar(master=top_middle_frame, command=self.text_field_total_price.yview, fg_color=self.fg_color, scrollbar_color="yellow")
        ctk_textbox_scrollbar.grid(row=2, column=0, sticky="sen")
        self.text_field_total_price.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        # ----------- BOTTOM HALF OF MAIN FRAME -------------
        bottom_middle_frame = ctk.CTkFrame(master=main_middle_frame, fg_color=self.fg_color)
        bottom_middle_frame.grid(row=1, column=0)
        self.makanan_customer_dict = dict()
        self.total_harga = 0

        buttons_per_row = 2

        for index, food in enumerate(self.makanan_dict):
            harga = self.makanan_dict[food]
            row = math.floor(index/buttons_per_row)
            col = index%buttons_per_row*2
            button_food_name = ctk.CTkButton(master=bottom_middle_frame, 
                                             command= lambda harga=harga, food=food: self.add_customer_food(harga, food), 
                                             text=food, text_font=("Terminal", 25))
            button_food_name.grid(row=row, column=col, sticky="ew", padx=10, pady=10, ipady=10)
            button_minus = ctk.CTkButton(master=bottom_middle_frame, text_font=("Arial", 20), text="-", fg_color="red", width=10, height=0,
            command = lambda food=food, harga=harga: self.remove_customer_food(food, harga))
            button_minus.grid(row=row, column=col+1)

        return main_middle_frame

    def remove_customer_food(self, nama_makanan, harga_makanan):
        if nama_makanan not in self.makanan_customer_dict:
            return

        self.total_harga -= round(harga_makanan, 2)
        self.update_customer_food_dict(nama_makanan, "minus")
        self.update_customer_food_display()

    def add_customer_food(self, harga_makanan, nama_makanan):
        self.total_harga += round(harga_makanan, 2) 
        self.update_customer_food_dict(nama_makanan, "add")
        self.update_customer_food_display()
    
    def update_customer_food_display(self):
        senarai_makanan_cantik = ""
        for food in self.makanan_customer_dict:
            bil = self.makanan_customer_dict[food]
            current_harga = round(self.makanan_dict[food]*bil, 2)
            senarai_makanan_cantik += f"{food:<20} x{bil:>2} (RM {current_harga:.2f})\n"
        self.text_field_total_price.delete("1.0", tkinter.END)
        self.text_field_total_price.insert(tkinter.END, senarai_makanan_cantik)
        self.entry_total_price.delete(0, tkinter.END)
        self.entry_total_price.insert(0, f"RM {self.total_harga:.2f}")

    def update_customer_food_dict(self, nama_makanan, operation):
        if operation == "add":
            if nama_makanan in self.makanan_customer_dict:
                self.makanan_customer_dict[nama_makanan] += 1
            else :
                self.makanan_customer_dict[nama_makanan] = 1
        elif operation == "minus":
            if self.makanan_customer_dict[nama_makanan] == 1:
                self.makanan_customer_dict.pop(nama_makanan)
            else :
                self.makanan_customer_dict[nama_makanan] -= 1

    def retrieve_food_from_db(self):
        with open("foods.json", "r") as file:
            return json.load(file)    

    def clearAll(self) :
        self.total_harga = 0
        self.entry_total_price.delete(0, tkinter.END)
        self.text_field_total_price.delete("1.0", tkinter.END)
        self.makanan_customer_dict.clear()
    
    def open_pay_window(self):
        window = Window_CheckOut(self.text_field_total_price.get("1.0",'end-1c'), 
        self.entry_total_price.get())