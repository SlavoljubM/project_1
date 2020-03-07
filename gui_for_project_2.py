import tkinter as tk
import pandas as pd
import os


height = 300
width = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


def getCSV():
	df = pd.read_csv("result.csv")
	print(df)

def import_files():
	files = [file for file in os.listdir("./Accounts")]
	for file in files:
		print(file)



button_invoice = tk.Button(canvas, text="Invoice", command=import_files, bg="#9966ff")
button_invoice.place(relx=0.1, rely=0, relwidth=0.15, relheight=0.1)

button_result = tk.Button(canvas, text="Result", command=getCSV, bg="#9933ff")
button_result.place(relx=0.75, rely=0, relwidth=0.15, relheight=0.1)







root.mainloop()