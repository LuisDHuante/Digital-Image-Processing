import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertir a Escala de Grises")

        self.image = None
        self.gray_image = None

        # Botón para abrir la imagen
        self.open_button = tk.Button(root, text="Abrir", command=self.open_image)
        self.open_button.pack()

        # Botón para convertir a escala de grises
        self.convert_button = tk.Button(root, text="Convertir a Grises", command=self.convert_to_gray, state=tk.DISABLED)
        self.convert_button.pack()

        # Botón para guardar la imagen en escala de grises
        self.save_button = tk.Button(root, text="Guardar", command=self.save_gray_image, state=tk.DISABLED)
        self.save_button.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.show_image(self.image)
            self.convert_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.DISABLED)

    def convert_to_gray(self):
        if self.image:
            self.gray_image = self.image.convert("L")
            self.show_image(self.gray_image)
            self.save_button.config(state=tk.NORMAL)

    def save_gray_image(self):
        if self.gray_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
            if file_path:
                self.gray_image.save(file_path)

    def show_image(self, img):
        img = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=img)
        label.image = img
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
