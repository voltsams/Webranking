from tkinter import Tk, Label, Button
from fpdf import FPDF

class PDFGenerator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Générateur PDF")
        self.root.geometry("300x100")

        self.label = Label(self.root, text="Cliquez sur le bouton pour générer le PDF")
        self.label.pack()

        self.generate_button = Button(self.root, text="Générer PDF", command=self.generate_pdf)
        self.generate_button.pack()

        self.root.mainloop()

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Hello World", ln=True, align="C")
        pdf.output("example.pdf")

        self.label.config(text="PDF généré avec succès")

PDFGenerator()