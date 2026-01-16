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

def Remplir_auto(qtab, lineEditCodePoste, lineEditMarque, lineEditProcesseur, lineEditType, lineEditSE, row, column):
    # Récupérer les valeurs de la ligne sélectionnée
    Codeposte = qtab.item(row, 0).text()
    Marque = qtab.item(row, 1).text()
    Processeur = qtab.item(row, 2).text()
    Type = qtab.item(row, 3).text()
    SE = qtab.item(row, 4).text()
    # Remplir les champs correspondants dans le formulaire
    lineEditCodePoste.setText(Codeposte)
    lineEditMarque.setText(Marque)
    lineEditProcesseur.setText(Processeur)
    lineEditType.setText(Type)
    lineEditSE.setText(SE)
    #Mettre en évidence la ligne sélectionnée (effet visuel)
    qtab.selectRow(row)


# Fonction pour modifier les informations d’un poste
def ModifierPoste(lineEditCodePoste, lineEditMarque, lineEditProcesseur, lineEditType, lineEditSE, qtab):
    CodePoste= lineEditCodePoste.text().strip()
    Marque = lineEditMarque.text().strip()
    Processeur = lineEditProcesseur.text().strip()
    Type = lineEditType.text().strip()
    SE = lineEditSE.text().strip()

    print("Modification du poste :", CodePoste)
    conn = sqlite3.connect("ParcInfo.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("UPDATE postes SET Marque=?, Processeur=?, Type=?, SE=? WHERE Code_poste = ?;", (CodePoste,Marque, Processeur, Type, SE))
    conn.commit()
    conn.close()
    # Rafraîchir l’affichage
    AfficherTout(qtab)