import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os

def extract_emails():
    # Ask user to choose a .txt file
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=(("Text files", ".txt"), ("All files", ".*"))
    )
    
    if not file_path:
        return  # No file selected

    try:
        # Read the content of the file
        with open(file_path, 'r') as f:
            content = f.read()

        # Regex pattern to extract emails
        pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = sorted(set(re.findall(pattern, content)))

        if emails:
            # Save to new file in the same folder
            output_path = os.path.join(os.path.dirname(file_path), "emails_extracted.txt")
            with open(output_path, 'w') as f:
                for email in emails:
                    f.write(email + '\n')

            messagebox.showinfo("Success", f"{len(emails)} emails extracted and saved to:\n{output_path}")
        else:
            messagebox.showinfo("No Emails", "No email addresses found in the file.")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# Create the GUI
root = tk.Tk()
root.title("Email Extractor")
root.geometry("400x200")

label = tk.Label(root, text="📧 Extract Emails from Text File", font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Choose File and Extract", font=("Arial", 12), command=extract_emails)
btn.pack(pady=10)

root.mainloop()