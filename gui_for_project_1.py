import tkinter as tk

height = 500
width = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


frame = tk.Frame(root, bg="#99ccff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


button = tk.Button(frame, text="Result", bg="gray")
button.pack()

label_files = tk.Label(frame, bg="#9933ff")
label_files.pack(side ="right")

label_result = tk.Label(frame, bg="#9966ff")
label_result.pack(side ="left")





root.mainloop()