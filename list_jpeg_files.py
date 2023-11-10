import os
import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas

def list_and_export_to_pdf():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if folder_path:
        try:
            image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
            if image_files:
                pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save PDF As")
                if pdf_path:
                    create_pdf(image_files, pdf_path)
            else:
                show_message("No image files (JPEG or PNG) found in the selected folder.")
        except Exception as e:
            show_message(f"An error occurred: {str(e)}")

def create_pdf(image_files, pdf_path):
    pdf = canvas.Canvas(pdf_path)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(72, 800, "List of Image Files:")
    y_position = 780

    for image_file in image_files:
        pdf.drawString(72, y_position, image_file)
        y_position -= 15

    pdf.save()
    show_message(f"PDF file created at: {pdf_path}")

def show_message(message):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, message)
    result_text.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("List and Export to PDF")

# Create and configure widgets
label = tk.Label(app, text="Click the button to select a folder, list image files (JPEG or PNG), and export to PDF.")
label.pack(pady=10)

export_button = tk.Button(app, text="Export to PDF", command=list_and_export_to_pdf)
export_button.pack(pady=10)

result_text = tk.Text(app, height=10, width=40, state=tk.DISABLED)
result_text.pack(pady=10)

# Run the application
app.mainloop()
