import customtkinter
import os
import pyjokes


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def generateJoke():
    if segmented_button.get() == 'Normal':
        joke = pyjokes.get_joke('en', 'neutral')
        output.configure(state='normal')
        output.delete('1.0', 'end')
        output.insert('1.0', joke)
        output.configure(state='disabled')
    elif segmented_button.get() == 'Chuck Norris Mode':
        joke = pyjokes.get_joke('en', 'chuck')
        output.configure(state='normal')
        output.delete('1.0', 'end')
        output.insert('1.0', joke)
        output.configure(state='disabled')

app = customtkinter.CTk()
app.geometry("720x480")
app.title('Joke Generator')

customtkinter.CTkLabel(app, text="Humor.exe", font=("Product Sans", 70)).pack(pady=50)

segmented_button = customtkinter.CTkSegmentedButton(app, values=['Normal', 'Chuck Norris Mode'],
                                                     width=170, height=30,
                                                     font=("Product Sans", 15, 'bold'),
                                                     )

segmented_button.pack(pady=(0, 20))
segmented_button.set('Normal')

output = customtkinter.CTkTextbox(app, width=600, height=100, wrap='word', state='disabled', font=("Product Sans", 20))
output.pack(pady=(0, 20))

button = customtkinter.CTkButton(app, text='Generate', width=140, height=50, corner_radius=10, font=("Product Sans", 20, 'bold'), command=generateJoke)
button.pack(pady=20)

app.mainloop()