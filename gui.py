import tkinter as tk
from tkinter import messagebox

FILENAME = 'admission.txt'

# ---------- Add Admission ----------
def save_admission_window(entries, win):
    data = [entry.get().strip() for entry in entries]
    name, cnic = data[0], data[1]

    if not name or not cnic:
        messagebox.showerror("Error", "Name and CNIC are required.")
        return

    with open(FILENAME, 'a') as file:
        file.write(f'Name: {data[0]}\nCNIC: {data[1]}\nFather Name: {data[2]}\nAge: {data[3]}\nAddress: {data[4]}\nAcademic History: {data[5]}\n---\n')

    messagebox.showinfo("Success", "Admission added successfully!")
    win.destroy()

def open_add_admission():
    win = tk.Toplevel(root)
    win.title("Add New Admission")

    labels = ["Name", "CNIC", "Father's Name", "Age", "Address", "Academic History"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label + ":").grid(row=i, column=0, sticky='e', padx=5, pady=2)
        entry = tk.Entry(win, width=40)
        entry.grid(row=i, column=1, pady=2)
        entries.append(entry)

    tk.Button(win, text="Save Admission", command=lambda: save_admission_window(entries, win)).grid(row=len(labels), column=0, columnspan=2, pady=10)

# ---------- List Admissions ----------
def list_admissions():
    try:
        with open(FILENAME, 'r') as file:
            records = file.read().strip().split('---\n')
            result = "\n\n".join(records).strip()
            if result:
                show_text_window("All Admissions", result)
            else:
                messagebox.showinfo("No Records", "No admissions found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Admission file not found.")

# ---------- Search Admissions ----------
def search_admission():
    win = tk.Toplevel(root)
    win.title("Search Admission")

    def perform_search():
        query = search_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Required", "Please enter a value to search.")
            return
        try:
            with open(FILENAME, 'r') as file:
                records = file.read().strip().split('---\n')
                found = [r for r in records if query.lower() in r.lower()]
                result_text.config(state='normal')
                result_text.delete(1.0, tk.END)
                if found:
                    result_text.insert(tk.END, "\n\n".join(found))
                else:
                    result_text.insert(tk.END, "No matching records found.")
                result_text.config(state='disabled')
        except FileNotFoundError:
            messagebox.showerror("Error", "Admission file not found.")

    tk.Label(win, text="Search Admission", font=("Arial", 12, "bold")).pack(pady=10)

    frame = tk.Frame(win)
    frame.pack(pady=5)

    tk.Label(frame, text="Enter Name or CNIC:").grid(row=0, column=0, padx=5)
    search_entry = tk.Entry(frame, width=40)
    search_entry.grid(row=0, column=1, padx=5)

    tk.Button(win, text="Search", width=20, command=perform_search).pack(pady=10)

    result_text = tk.Text(win, wrap='word', width=70, height=20)
    result_text.pack(padx=10, pady=10)
    result_text.config(state='disabled')

# ---------- Utility Text Display ----------
def show_text_window(title, content):
    win = tk.Toplevel(root)
    win.title(title)
    text = tk.Text(win, wrap='word', width=70, height=25)
    text.insert(tk.END, content)
    text.config(state='disabled')
    text.pack(padx=10, pady=10)

# ---------- Main Window ----------
root = tk.Tk()
root.title("University Admission System")

tk.Label(root, text="Welcome to Forman Christian College", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="(A Chartered University)", font=("Arial", 10)).pack(pady=5)

tk.Button(root, text="Add Admission", width=25, command=open_add_admission).pack(pady=5)
tk.Button(root, text="List Admissions", width=25, command=list_admissions).pack(pady=5)
tk.Button(root, text="Search Admission", width=25, command=search_admission).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=20)

root.mainloop()
