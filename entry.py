import tkinter as tk;

root=tk.Tk()
root.geometry("600x400")

name_var = tk.StringVar()

def submit():
	name = entry.get()
	print(name)
	entry.delete(0)

label = tk.Label(text="Name", font="Consolas")
label.pack()

entry = tk.Entry(textvariable=name_var, bg="black", fg="white", font="Consolas")
entry.pack()

button = tk.Button(text="Submit", bg="#0000FF", fg="#FFFFFF", command=submit)
button.pack()

root.mainloop()

	
