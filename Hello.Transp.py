import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x350")
root.configure(bg="lightblue")

root.attributes('-alpha', 1)
style = ttk.Style()
style.theme_use('clam')
style.configure('Transparent.TFrame', background='lightblue')
root.wm_attributes("-transparentcolor", 'lightblue')

frame = ttk.Frame(root, style='Transparent.TFrame')
frame.place(relwidth=1, relheight=1)

message2 = tk.Label(frame, text="Hellooo, World!", font=("Helvetica", 20, 'bold'), bg="white", fg="black")
message2.pack()

img = tk.PhotoImage(file="image.png")
img = img.subsample(10)
label_img = tk.Label(frame, image=img, bg="lightblue")
label_img.pack(pady=10)

root.mainloop()
