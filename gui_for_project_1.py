import tkinter as tk
import pandas as pd


height = 500
width = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


frame = tk.Frame(root, bg="#99ccff")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

def getCSV():
	global df
	df = pd.read_csv("result.csv")
	print(df)
		


label_files = tk.Label(frame, bg="#9933ff")
label_files.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=0.9)

label_result = tk.Label(frame, bg="#9966ff")
label_result.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.9)

button = tk.Button(frame, text="Result", command=getCSV, bg="gray")
button.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.05)





root.mainloop()