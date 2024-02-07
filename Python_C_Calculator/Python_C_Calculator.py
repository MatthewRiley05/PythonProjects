import customtkinter
import os
from PIL import Image, ImageTk
import ctypes

#C Library
lib = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), "calculator.dll"))

#Setup
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("system")

#App Frame
calculator = customtkinter.CTk()
calculator.geometry("400x600")
calculator.title("Calculator")
script_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(script_dir, "calculatorlogo.png")
icon = ImageTk.PhotoImage(Image.open(image_path))
calculator.iconbitmap()
calculator.iconphoto(False, icon)

#App Grid Configuration
calculator.grid_columnconfigure(0, weight=1)
calculator.grid_columnconfigure(1, weight=1)
calculator.grid_columnconfigure(2, weight=1)
calculator.grid_columnconfigure(3, weight=1)
calculator.grid_rowconfigure(0, weight=1)
calculator.grid_rowconfigure(1, weight=1)
calculator.grid_rowconfigure(2, weight=1)
calculator.grid_rowconfigure(3, weight=1)
calculator.grid_rowconfigure(4, weight=1)
calculator.grid_rowconfigure(5, weight=1)

#Output Panel
output = customtkinter.CTkEntry(calculator,
                                  font=("Product Sans", 30),
                                  text_color=("#000000", "#ffffff"),
                                  height=120,
                                  width=400,
                                  corner_radius=20,
                                  state="disabled")
output.grid(row=0, column=0, columnspan=4, padx=30, pady=(10, 0))

#Buttons
allClear = customtkinter.CTkButton(calculator,
                                   font=("Product Sans", 20),
                                   text_color=("#000000", "#ffffff"),
                                   fg_color="#71808e",
                                   hover_color="#4f5a63",
                                   text="AC",
                                   height=70,
                                   width=70,
                                   corner_radius=20,
                                   command=lambda: output.delete(0, 'end'))
allClear.grid(row=1, column=0, padx=(20, 0))

delete = customtkinter.CTkButton(calculator,
                                 font=("Product Sans", 20),
                                 text_color=("#000000", "#ffffff"),
                                 fg_color="#71808e",
                                 hover_color="#4f5a63",
                                 text="⌫",
                                 height=70,
                                 width=70, 
                                 corner_radius=20,
                                 command=lambda: output.delete('end'))
delete.grid(row=1, column=1)

divide = customtkinter.CTkButton(calculator,
                                 font=("Product Sans", 20),
                                 text_color=("#000000", "#ffffff"),
                                 text="÷",
                                 height=70,
                                 width=70,
                                 corner_radius=20)
divide.grid(row=1, column=2)

multiply = customtkinter.CTkButton(calculator,
                                   font=("Product Sans", 20),
                                   text_color=("#000000", "#ffffff"),
                                   text="×",
                                   height=70,
                                   width=70,
                                   corner_radius=20)
multiply.grid(row=1, column=3, padx=(0, 20))

subtract = customtkinter.CTkButton(calculator,
                                   font=("Product Sans", 20),
                                   text_color=("#000000", "#ffffff"),
                                   text="-",
                                   height=70,
                                   width=70,
                                   corner_radius=20)
subtract.grid(row=2, column=3, padx=(0, 20))

add = customtkinter.CTkButton(calculator,
                              font=("Product Sans", 20),
                              text_color=("#000000", "#ffffff"),
                              text="+",
                              height=70,
                              width=70,
                              corner_radius=20)
add.grid(row=3, column=3, padx=(0, 20))

equals = customtkinter.CTkButton(calculator,
                                 font=("Product Sans", 20),
                                 text_color=("#000000", "#ffffff"),
                                 text="=",
                                 height=170,
                                 width=70,
                                 corner_radius=20,
                                 command=lambda: output.insert('end', '='))
equals.grid(rowspan=5, column=3, padx=(0, 20), pady=(0, 10))

seven = customtkinter.CTkButton(calculator,
                                font=("Product Sans", 20),
                                text_color=("#000000", "#ffffff"),
                                fg_color="#71808e",
                                hover_color="#4f5a63",
                                text="7",
                                height=70,
                                width=70,
                                corner_radius=20)
seven.grid(row=2, column=0, padx=(20, 0))

eight = customtkinter.CTkButton(calculator,
                                font=("Product Sans", 20),
                                text_color=("#000000", "#ffffff"),
                                fg_color="#71808e",
                                hover_color="#4f5a63",
                                text="8",
                                height=70,
                                width=70,
                                corner_radius=20)
eight.grid(row=2, column=1)

nine = customtkinter.CTkButton(calculator,
                               font=("Product Sans", 20),
                               text_color=("#000000", "#ffffff"),
                               fg_color="#71808e",
                               hover_color="#4f5a63",
                               text="9",
                               height=70,
                               width=70,
                               corner_radius=20)
nine.grid(row=2, column=2)

four = customtkinter.CTkButton(calculator,
                               font=("Product Sans", 20),
                               text_color=("#000000", "#ffffff"),
                               fg_color="#71808e",
                               hover_color="#4f5a63",
                               text="4",
                               height=70,
                               width=70,
                               corner_radius=20)
four.grid(row=3, column=0, padx=(20, 0))

five = customtkinter.CTkButton(calculator,
                               font=("Product Sans", 20),
                               text_color=("#000000", "#ffffff"),
                               fg_color="#71808e",
                               hover_color="#4f5a63",
                               text="5",
                               height=70,
                               width=70,
                               corner_radius=20)
five.grid(row=3, column=1)

six = customtkinter.CTkButton(calculator,
                              font=("Product Sans", 20),
                              text_color=("#000000", "#ffffff"),
                              fg_color="#71808e",
                              hover_color="#4f5a63",
                              text="6",
                              height=70,
                              width=70,
                              corner_radius=20)
six.grid(row=3, column=2)

one = customtkinter.CTkButton(calculator,
                              font=("Product Sans", 20),
                              text_color=("#000000", "#ffffff"),
                              fg_color="#71808e",
                              hover_color="#4f5a63",
                              text="1",
                              height=70,
                              width=70,
                              corner_radius=20)
one.grid(row=4, column=0, padx=(20, 0))

two = customtkinter.CTkButton(calculator,
                              font=("Product Sans", 20),
                              text_color=("#000000", "#ffffff"),
                              fg_color="#71808e",
                              hover_color="#4f5a63",
                              text="2",
                              height=70,
                              width=70,
                              corner_radius=20)
two.grid(row=4, column=1)

three = customtkinter.CTkButton(calculator,
                                font=("Product Sans", 20),
                                text_color=("#000000", "#ffffff"),
                                fg_color="#71808e",
                                hover_color="#4f5a63",
                                text="3",
                                height=70,
                                width=70,
                                corner_radius=20)
three.grid(row=4, column=2)

zero = customtkinter.CTkButton(calculator,
                               font=("Product Sans", 20),
                               text_color=("#000000", "#ffffff"),
                               fg_color="#71808e",
                               hover_color="#4f5a63",
                               text="0",
                               height=70,
                               width=160,
                               corner_radius=20)
zero.grid(row=5, columnspan=2, padx=(20, 0), pady=(0, 10))

decimal = customtkinter.CTkButton(calculator,
                                  font=("Product Sans", 20),
                                  text_color=("#000000", "#ffffff"),
                                  fg_color="#71808e",
                                  hover_color="#4f5a63",
                                  text=".",
                                  height=70,
                                  width=70,
                                  corner_radius=20)
decimal.grid(row=5, column=2, pady=(0, 10))

#Output Expression
expression = ""

def add_to_expression(value):
    global expression
    expression += value
    output.config(state="normal")
    output.delete(0, 'end')
    output.insert(0, expression)
    output.config(state="disabled")

#Main Loop
calculator.mainloop()