import sqlite3

#création de notre base de données¸<PacrInfo.db> et de la table <postes>
def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("ParcInfo.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS postes(Code_poste TEXT,Marque TEXT,Processeur TEXT,Type TEXT,SE TEXT);")
    conn.commit()
