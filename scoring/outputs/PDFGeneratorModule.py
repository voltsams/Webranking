from tkinter import Tk, Label, Button
from fpdf import FPDF


# Création de la classe PDFGenerator
class PDFGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Générateur PDF")
        self.root.geometry("300x100")

        self.label = Label(self.root, text="Cliquez sur le bouton pour générer le PDF")
        self.label.pack()

        self.generate_button = Button(self.root, text="Générer PDF", command=self.generate_pdf)
        self.generate_button.pack()

        self.root.mainloop()
    def header(self):
        self.set_font('Arial', 'B', 3)
        self.cell(0, 10, 'Audit de référencement d\'un site web', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def generate_pdf(self):
        # Création de l'objet PDF
        #pdf = PDFGenerator()
        self.add_page("landscape")

        # Définition des titres de colonnes
        column_titles = ["               ", "Liens entrants/sortants", "Temps de chargement", "Présence de la balise meta",
                         "Remplissage des balises <alt>", "Présence de H1", "Taille des images/vidéos",
                         "[Bonus] Présence de copié collé ?", "Pertinence des mots clés", "Fréquences des mots dans une page",
                         "[Bonus] Mobile friendly/accessibility", "Score"]

        # Largeurs des colonnes
        # col_width = 45

        # Ajout des titres de colonnes au tableau
        for title in column_titles:
            self.cell(len(title), 10, title, 1, 0, 'C')
        self.ln()

        # Ajout des données aux lignes du tableau
        for i in range(3):
            self.cell(15, 10, "Page {}".format(i + 1), 1, 0, 'C')
            for j in range(11):
                self.cell(len(column_titles[j+1]), 10, "", 1, 0, 'C')  # Cellules vides
            self.ln()

        # Sauvegarde du PDF
        self.output("audit_referencement.pdf")
        self.label.config(text="PDF généré avec succès")

PDFGenerator()