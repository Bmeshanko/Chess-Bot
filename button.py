import tkinter as tk;
def main():
	window = tk.Tk()

	label = tk.Label(
		text="Hello",
		fg="white",
		bg="black",
		width=20,
		height=10)
	label.pack()

	button = tk.Button(
		text="Click",
		width=20,
		height=10,
		bg="blue",
		fg="black")
	button.pack();


	window.mainloop()

if __name__ == "__main__":
	main()
	
