import customtkinter
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys
import main

# Setup
default_appearance_mode = "system"
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
customtkinter.set_appearance_mode(default_appearance_mode)
customtkinter.set_default_color_theme("blue")

def start():
    # Create the main window
    app = customtkinter.CTk()
    app.title("Terrain Generator")
    app.geometry("1000x600")
    
    # Import icon
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    icon = ImageTk.PhotoImage(Image.open(resource_path("logo.png")))
    app.iconbitmap()
    app.iconphoto(False, icon)

    # Create grid layout
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(8, weight=1)

    # Create a FigureCanvasTkAgg object and add it to the window
    canvas = FigureCanvasTkAgg(main.generateDiamondSquare())
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0, rowspan=9)

    # Functions
    def updateFigure():
        if generationOption.get() == 'Diamond Square':
            fig = main.generateDiamondSquare()
            canvas.figure = fig
            canvas.draw()
        elif generationOption.get() == 'Perlin':
            fig = main.generatePerlin()
            canvas.figure = fig
            canvas.draw()
        elif generationOption.get() == 'OpenSimplex':
            fig = main.generateOpenSimplex()
            canvas.figure = fig
            canvas.draw()

    def sizeSliderUpdate(val):
        main.size = int(sizeSlider.get())
        sizeLabel.configure(text=f'Size: {main.size}')
        
    def scaleSliderUpdate(val):
        main.scale = int(scaleSlider.get()) / 10
        scaleLabel.configure(text=f'Scale: {main.scale}')
        
    def mixSliderUpdate(val):
        main.mix = int(mixSlider.get()) / 10
        mixLabel.configure(text=f'Mix: {main.mix}')

    # Widgets
    title = customtkinter.CTkLabel(app,
                                    text='Ygdrassil',
                                    font=('Product Sans', 50, 'bold'))
    title.grid(column=1 ,row=0, padx=(0, 0), pady=(30, 0))

    generationOption_var = customtkinter.StringVar(value='Diamond Square')
    generationOption = customtkinter.CTkSegmentedButton(app, values=['Diamond Square', 'Perlin', 'OpenSimplex'],
                                                        font=('Product Sans', 15, 'bold'),
                                                        variable=generationOption_var)

    generationOption.grid(column=1, row=1, padx=(0, 0), pady=(30, 0))

    sizeLabel = customtkinter.CTkLabel(app,
                                    text='Size: 100',
                                    font=('Product Sans', 20, 'bold'))
    sizeLabel.grid(column=1 ,row=2, padx=(0, 0), pady=(30, 0))

    sizeSlider = customtkinter.CTkSlider(app,
                                    width=300,
                                    from_=50,
                                    to=1000,
                                    number_of_steps=19,
                                    command=sizeSliderUpdate,
                                    )
    sizeSlider.grid(column=1, row=3, padx=(0, 0), pady=(20, 0))
    sizeSlider.set(100)

    scaleLabel = customtkinter.CTkLabel(app,
                                        text='Scale: 1',
                                        font=('Product Sans', 20, 'bold'))
    scaleLabel.grid(column=1, row=4, padx=(0, 0), pady=(50, 0))

    scaleSlider = customtkinter.CTkSlider(app,
                                    width=300,
                                    from_=1,
                                    to=50,
                                    number_of_steps=10,
                                    command=scaleSliderUpdate,
                                    )
    scaleSlider.grid(column=1, row=5, padx=(0, 0), pady=(20, 0))
    scaleSlider.set(10)

    mixLabel = customtkinter.CTkLabel(app,
                                        text='Mix: 0.3',
                                        font=('Product Sans', 20, 'bold'))
    mixLabel.grid(column=1, row=6, padx=(0, 0), pady=(50, 0))

    mixSlider = customtkinter.CTkSlider(app,
                                    width=300,
                                    from_=1,
                                    to=5,
                                    number_of_steps=4,
                                    command=mixSliderUpdate,
                                    )
    mixSlider.grid(column=1, row=7, padx=(0, 0), pady=(20, 0))
    mixSlider.set(3)

    generate = customtkinter.CTkButton(app,
                                    text='Generate',
                                    font=('Product Sans', 20, 'bold'),
                                    corner_radius=10,
                                    width=150,
                                    height=50,
                                    command=updateFigure)
    generate.grid(column=1, row=8, padx=(0, 0), pady=(0, 0))

    # Main loop
    app.mainloop()

# Program start
if __name__ == "__main__":
    start()