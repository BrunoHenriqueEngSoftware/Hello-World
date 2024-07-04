import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x350")
root.configure(bg="lightblue")

message2 = tk.Label(root, text="Hellooo, World!", font=("Helvetica", 20, 'bold', ), bg="lightblue", fg="white")
message2.pack()

img = tk.PhotoImage(file="image.png")
img = img.subsample(10)  # Redimensiona a imagem 
label_img = tk.Label(image=img, bg="lightblue")
label_img.pack(pady=10)

message2 = tk.Label(root, text="Bruno Henrique Mendes Silva", font=("Helvetica", 8, 'bold'), bg="lightblue", fg="white")
message2.pack()
root.mainloop()
