import sqlite3
from PyQt6.QtWidgets import QTableWidgetItem
import gestion_donnees

#Créatiuon de la fonction Insérer
def InsererPoste(lineEditCodePoste, lineEditMarque, lineEditProcesseur, lineEditType, lineEditSE, qtab):
    print("Insertion dans la table postes")
    conn = sqlite3.connect("ParcInfo.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "INSERT INTO postes (Code_poste, Marque, Processeur, Type, SE) VALUES (?, ?, ?, ?, ?)",
        (lineEditCodePoste.text(),lineEditMarque.text(),lineEditProcesseur.text(),lineEditType.text(),lineEditSE.text())
    )
    conn.commit()
    AfficherTout(qtab)


# Création de la fonction AfficherTout
def AfficherTout(qtab):
    print("Affichage de tous les postes")
    conn = sqlite3.connect("ParcInfo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM postes")
    resultat = cursor.fetchall()
    conn.close()
    # QTable
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(5)
    qtab.setGeometry(50, 250, 450, 200)
    qtab.setHorizontalHeaderLabels(['Code Poste', 'Marque', 'Processeur', 'Type', 'S.E'])

    for i in range(len(resultat)):
        for j in range(5):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))


# Fonction pour supprimer un poste selon son Code_poste
def SupprimerPoste(lineEditSuppCode, qtab):
    print("Suppression du poste :", lineEditSuppCode.text())
    conn = sqlite3.connect("ParcInfo.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("DELETE FROM postes WHERE Code_poste = ?", (lineEditSuppCode.text(),))
    conn.commit()
    conn.close()
    # Rafraîchir l’affichage
    AfficherTout(qtab)