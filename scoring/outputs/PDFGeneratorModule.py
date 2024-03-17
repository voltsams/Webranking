from tkinter import Tk, Label, Button
from fpdf import FPDF


# Création de la classe PDF
class PDFGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 3)
        self.cell(0, 10, 'Audit de référencement d\'un site web', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')


# Création de l'objet PDF
pdf = PDFGenerator()
pdf.add_page("landscape")

# Définition des titres de colonnes
column_titles = ["               ", "Liens entrants/sortants", "Temps de chargement", "Présence de la balise meta",
                 "Remplissage des balises <alt>", "Présence de H1", "Taille des images/vidéos",
                 "[Bonus] Présence de copié collé ?", "Pertinence des mots clés", "Fréquences des mots dans une page",
                 "[Bonus] Mobile friendly/accessibility", "Score"]

# Largeurs des colonnes
# col_width = 45

# Ajout des titres de colonnes au tableau
for title in column_titles:
    pdf.cell(len(title), 10, title, 1, 0, 'C')
pdf.ln()

# Ajout des données aux lignes du tableau
for i in range(3):
    pdf.cell(15, 10, "Page {}".format(i + 1), 1, 0, 'C')
    for j in range(11):
        pdf.cell(len(column_titles[j+1]), 10, "", 1, 0, 'C')  # Cellules vides
    pdf.ln()

# Sauvegarde du PDF
pdf.output("audit_referencement.pdf")
