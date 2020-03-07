import tkinter as tk
import pandas as pd
import os


height = 500
width = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


frame = tk.Frame(root, bg="#99ccff")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)



def getCSV():
	df = pd.read_csv("result.csv")
	print(df)
	
def import_files():
	files = [file for file in os.listdir("./Accounts")]
	for file in files:
		print(file)
file_a = import_files()
file = tk.StringVar(file_a)
# csv = getCSV()
# csv1 = tk.StringVar(csv)


label_files = tk.Label(frame, bg="#9933ff",textvariable=file)
label_files.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=0.9)

label_result = tk.Label(frame, bg="#9966ff")
label_result.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.9)

button = tk.Button(frame, text="Result", command=getCSV, bg="gray")
button.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.05)





root.mainloop()