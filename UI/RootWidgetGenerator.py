import tkinter as tk


class Tableau(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Création du tableau
        self.table = tk.Frame(self.parent)
        self.table.pack(expand=True, fill=tk.BOTH)

        # Création des en-têtes
        headers = ['Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 5']
        for col, header in enumerate(headers):
            lbl_header = tk.Label(self.table, text=header, borderwidth=1, relief='solid')
            lbl_header.grid(row=0, column=col, sticky='nsew')

        # Remplissage de quelques données
        data = [
            ['Donnée 1', 'Donnée 2', 'Donnée 3', 'Donnée 4', 'Donnée 5'],
            ['Donnée 6', 'Donnée 7', 'Donnée 8', 'Donnée 9', 'Donnée 10']
        ]
        for row, row_data in enumerate(data, start=1):
            for col, cell_data in enumerate(row_data):
                lbl_data = tk.Label(self.table, text=cell_data, borderwidth=1, relief='solid')
                lbl_data.grid(row=row, column=col, sticky='nsew')

        # Configuration des poids des lignes et des colonnes pour le redimensionnement
        self.table.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.table.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tableau avec 5 colonnes")
    tableau = Tableau(root)
    tableau.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
