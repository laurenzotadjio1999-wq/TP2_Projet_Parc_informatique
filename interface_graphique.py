# Importation des packages nécessaires
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel,QGridLayout
import gestion_donnees
import operations_CRUD

#import gestion_donnees
#import operations_CRUD


# Création de notre fenêtre
app = QApplication([])
fenetre = QWidget()
fenetre.setWindowTitle("TP2_POO_Laurenzo-Ricardeau")
fenetre.setGeometry(200, 200, 650, 500)

# grid layout
grid = QGridLayout()
fenetre.setLayout(grid)

# Création d’un message de bienvenue
message = "*********************************************************\n"
message += "*       GESTION DU PARC INFORMATIQUE – TP2 POO          ***\n"
message += "*********************************************************"
label_bienvenue = QLabel(message)
grid.addWidget(label_bienvenue, 0, 2, 1, 6)
label_bienvenue.setStyleSheet("font-family: Calibri; font-weight: bold;")

# Création du bouton "Créer Table"
btn1 = QPushButton(fenetre)
btn1.setText("Créer Table")
btn1.setGeometry(500, 100, 100, 30)
grid.addWidget(btn1, 1, 8)
btn1.clicked.connect(gestion_donnees.CreerTable)

# Création du bouton "Insérer"
btn2 = QPushButton(fenetre)
btn2.setText("INSÉRER")
btn2.setGeometry(500, 150, 100, 30)
grid.addWidget(btn2, 2, 8)
btn2.clicked.connect(lambda: operations_CRUD.InsererPoste(lineEditCodePoste, lineEditMarque, lineEditProcesseur, lineEditType, lineEditSE, qtab))

# Création des champs pour le bouton "Insérer"
labelCodePoste = QLabel("Code_Poste :")
labelMarque = QLabel("Marque:")
labelProcesseur = QLabel("Processeur:")
labelType = QLabel("Type (Laptop/Desktop):")
labelSE = QLabel("S.E:")

lineEditCodePoste = QLineEdit(fenetre)
lineEditCodePoste.setGeometry(150, 150, 100, 30)
grid.addWidget(labelCodePoste, 2, 0)
grid.addWidget(lineEditCodePoste, 2, 1)

lineEditMarque = QLineEdit(fenetre)
lineEditMarque.setGeometry(150, 150, 100, 30)
grid.addWidget(labelMarque, 2, 2)
grid.addWidget(lineEditMarque, 2, 3)

lineEditProcesseur = QLineEdit(fenetre)
lineEditProcesseur.setGeometry(350, 150, 100, 30)
grid.addWidget(labelProcesseur, 2, 4)
grid.addWidget(lineEditProcesseur, 2, 5)

lineEditType = QLineEdit(fenetre)
lineEditType.setGeometry(450, 150, 100, 30)
grid.addWidget(labelType, 3, 0)
grid.addWidget(lineEditType, 3, 1)

lineEditSE = QLineEdit(fenetre)
lineEditSE.setGeometry(450, 150, 100, 30)
grid.addWidget(labelSE, 3, 2)
grid.addWidget(lineEditSE, 3, 3)


# Création du bouton "Afficher Tout"
btn3 = QPushButton(fenetre)
btn3.setText("Afficher Tout")
btn3.setGeometry(500, 250, 100, 30)
grid.addWidget(btn3, 5, 8)
#btn3.clicked.connect()

# Création du bouton "Modifier"
btn4 = QPushButton(fenetre)
btn4.setText("MODIFIER")
btn4.setGeometry(500, 250, 100, 30)
grid.addWidget(btn4, 3, 8)
#btn4.clicked.connect()

# Création du QTable pour l’affichage des enregistrements
qtab = QTableWidget(fenetre)
qtab.setRowCount(8)
qtab.setColumnCount(5)
qtab.setMinimumHeight(200)
qtab.setMinimumWidth(450)
qtab.setHorizontalHeaderLabels(['Code Poste', 'Marque', 'Processeur', 'Type', 'Système d’exploitation'])
grid.addWidget(qtab, 7, 0, 2, 8)
#qtab.cellClicked.connect()

# Création du bouton "Supprimer"
labelSuppCode = QLabel("Code du poste :")
btn5 = QPushButton(fenetre)
btn5.setText("SUPPRIMER")
btn5.setGeometry(500, 200, 100, 30)
grid.addWidget(btn5, 4, 8)
#btn5.clicked.connect()
lineEditSuppCode = QLineEdit(fenetre)
lineEditSuppCode.setGeometry(350, 200, 100, 30)
grid.addWidget(labelSuppCode, 4, 6)
grid.addWidget(lineEditSuppCode, 4, 7)

# Affichage de la fenêtre et exécution de l’application
fenetre.show()
app.exec()
