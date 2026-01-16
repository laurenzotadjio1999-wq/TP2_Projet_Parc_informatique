# Importation des packages nécessaires
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel,QGridLayout
import gestion_donnees
import operations_CRUD

# Création de notre fenêtre
app = QApplication([])
fenetre = QWidget()
fenetre.setWindowTitle("TP2_POO_Laurenzo-Ricardeau")
fenetre.setGeometry(200, 200, 650, 500)

# Création d’un message de bienvenue
message = "*********************************************************\n"
message += "*       GESTION DU PARC INFORMATIQUE – TP2 POO          ***\n"
message += "*********************************************************"
label_bienvenue = QLabel(message)
grid.addWidget(label_bienvenue, 0, 2, 1, 6)
label_bienvenue.setStyleSheet("font-family: Calibri; font-weight: bold;")




# Affichage de la fenêtre et exécution de l’application
fenetre.show()
app.exec()
