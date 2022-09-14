import json
from sre_parse import State
import tkinter as tk
import tkinter.messagebox
import math
import customtkinter as ctk
import WindowMenuSelect
import WindowAddNewFood

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Window_CheckOut(ctk.CTkToplevel):
    def __init__(self, text, total_bayaran):
        super().__init__() 

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=100)
        middle_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        self.total_bayaran = total_bayaran

        middle_frame.grid(row=0, column=1, sticky="ns", padx=20, pady=10)
        tajuk = ctk.CTkLabel(master=middle_frame, text="CHECKOUT", text_font=("Arial", 25))
        tajuk.grid(row=0, column=0, sticky="ew")

        self.receipt = tkinter.Text(master=middle_frame, highlightthickness=0, font=("Consolas", 27), height=5, width=40)
        self.receipt.grid(row=1, column=0, sticky="nsew", pady=15)
        self.receipt.insert(tkinter.END, text)

        self.frame_tengah = ctk.CTkFrame(self, fg_color=self.master.fg_color)
        self.frame_tengah.columnconfigure(0, weight=1)
        self.frame_tengah.columnconfigure(1, weight=1)
        self.frame_tengah.grid(row=2,column=1, sticky="nsew", pady=10)

        self.labelBayaran = ctk.CTkLabel(master=self.frame_tengah, text="Paid: RM 0", text_font=("Arial", 25))
        self.labelBayaran.grid(row=0, column=1)

        self.totalBayaran = ctk.CTkLabel(master=self.frame_tengah, text=f"Total: {total_bayaran}", text_font=("Arial", 25))
        self.totalBayaran.grid(row=0, column=0, sticky="w")

        self.labelPaymentMethod = ctk.CTkLabel(master=self.frame_tengah, text="Payment method : Select One", text_font=("Arial", 25))
        self.labelPaymentMethod.grid(row=1, column=0, sticky="w")

        self.labelBaki = ctk.CTkLabel(master=self.frame_tengah, text="Baki: RM 0", text_font=("Arial", 25))
        self.labelBaki.grid(row=1, column=1)

        self.bottom_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        button_1 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "light blue",
                                            text="Cash", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="black",
                                            command=self.cash_event
                                            )
        button_2 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "yellow",
                                            text="Debit", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="black")
        button_3 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "brown",
                                            text="HUTANG(555)", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="white")

        self.bottom_frame.grid(row=3, column=1)
        button_1.grid(row=0, column=0)         
        button_2.grid(row=0, column=1)                                         
        button_3.grid(row=0, column=2)

    def cash_event(self):
            dialog = ctk.CTkInputDialog(master=None, text="Type in a number:", title="Berapa ringgit")
            self.set_label_bayaran(dialog.get_input())
    
    def set_label_bayaran(self, bayaran):
        self.labelBayaran.configure(text=f"Paid: RM {float(bayaran):.2f}")
        baki = str(int(bayaran) - float(self.total_bayaran[3:]))
        baki = float(baki)
        self.labelBaki.configure(text=f"Baki: RM {baki:.2f}") 
        self.labelPaymentMethod.configure(text="Payment method: Cash")

class App(ctk.CTk):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Cafe System")
        #self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.main_label = ctk.CTkLabel(master=self, text="CAFE SYSTEM", text_font=("Arial", 25))
        self.main_label.grid(row=0, column = 1)

        self.rowconfigure(0, minsize=100)
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=120)

        button_1 = ctk.CTkButton(master=self, text="Bayar", width=200, height=60, text_font=("Arial", 25), command=WindowMenuSelect.Window_CustomerBayar)
        button_1.grid(row=1, column = 1, pady=10, sticky="ew")

        button_2 = ctk.CTkButton(master=self, text="Tambah makanan", 
                                width=200, height=60, text_font=("Arial", 25), 
                                command=WindowAddNewFood.Window_TambahMakanan)
        button_2.grid(row=2, column = 1)

if __name__ == "__main__":
    app = App()
    app.mainloop()