import tkinter as tk
import pandas as pd
import os


height = 700
width = 1200

if __name__ == "__main__":

	root = tk.Tk()

	canvas = tk.Canvas(root, height=height, width=width)
	canvas.pack()


	frame = tk.Frame(root, bg="#99ccff")
	frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

	def format_csv(df):
		return str(df)

	def format_files(file):
		return str(file)
		
		
	def getCSV():
		df = pd.read_csv("result.csv")
		label_result["text"] = format_csv(df)
		button.configure(state="disabled")
		
	def import_files():
		files = [file for file in os.listdir("./Accounts")]
		for file in files:
			label_files["text"] += format_files(file)
			button1.configure(state="disabled")

			

			
	label_files = tk.Message(frame, bg="#9933ff", justify="left")
	label_files.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=0.9)

	label_result = tk.Label(frame, bg="#9966ff", justify="left")
	label_result.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.9)

	button = tk.Button(frame, text="Result", command=lambda: getCSV(), bg="gray")
	button.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.05)

	button1 = tk.Button(frame, text="Invoice", command=lambda: import_files(), bg="gray")
	button1.place(relx=0.4, rely=0, relwidth=0.1, relheight=0.05)






	root.mainloop()