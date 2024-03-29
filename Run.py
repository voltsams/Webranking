import tkinter as tk
from UI.gui import URLInputGUI


def main():
    # Créer une instance de l'interface graphique
    root = tk.Tk()
    app = URLInputGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
