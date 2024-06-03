import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100
    bmi = weight / (height ** 2)
    bmi_result_label.config(text=f"BMI: {bmi:.2f}")

    # Store data
    with open("bmi_data.txt", "a") as file:
        file.write(f"{weight},{height},{bmi}\n")

    # Display message box with BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal Weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    messagebox.showinfo("BMI Category", f"Your BMI Category: {category}")
def view_history():
    weights = []
    heights = []
    bmis = []

    # Read data from file
    with open("bmi_data.txt", "r") as file:
        for line in file:
            weight, height, bmi = line.strip().split(",")
            weights.append(float(weight))
            heights.append(float(height) * 100)
            bmis.append(float(bmi))

    # Plot BMI trend
    plt.plot(bmis)
    plt.xlabel('Entries')
    plt.ylabel('BMI')
    plt.title('BMI Trend')
    plt.show()
root = tk.Tk()
root.title("BMI Calculator")

# Add labels and entry fields
weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5)

weight_entry = ttk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = ttk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0, padx=5, pady=5)

height_entry = ttk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

bmi_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
bmi_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

bmi_result_label = ttk.Label(root, text="")
bmi_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

history_button = ttk.Button(root, text="View History", command=view_history)
history_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
