# Importiert Qt-spezifische Konstanten wie z. B. für Ausrichtung
from PyQt6.QtCore import Qt

# Importiert notwendige Qt-Widgets wie Labels, Layouts, Eingabefelder usw.
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QRadioButton, QCheckBox, QButtonGroup


# Erstellt ein benutzerdefiniertes zentrales Widget (GUI-Komponente)
class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)  # Initialisiert die Elternklasse QWidget

        # ---------- LABELS ----------

        # Erstellt ein Label für die Artikelanzahl und richtet es rechtsbündig aus
        lable_anzahl = QLabel("Anzahl an Artikeln pro Stück:")
        lable_anzahl.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Label für Benutzername, ebenfalls rechtsbündig
        lable_username = QLabel("Benutzername:")
        lable_username.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Label für Kennzeichen
        lable_kennzeichen = QLabel("Kennzeichen:")
        lable_kennzeichen.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Label für Alter
        lable_age = QLabel("Alter:")
        lable_age.setAlignment(Qt.AlignmentFlag.AlignRight)

        # (Optionales Label für Passwort – aktuell auskommentiert)
        # lable_passwort = QLabel("Passwort:")
        # lable_passwort.setAlignment(Qt.AlignmentFlag.AlignRight)

        # ---------- LINE EDITS MIT EINGABEMASKEN ----------

        # Eingabe für KFZ-Kennzeichen mit komplexer Eingabemaske (z. B. "B:AB 1234 C")
        lineedit_kennzeichen = QLineEdit()
        lineedit_kennzeichen.setInputMask(">A!aa:>aA! 0009 >a!;_")

        # Eingabe für Artikelanzahl – erwartet 2 Ziffern und 1 Buchstabe (z. B. "25A")
        lineedit_anzahl = QLineEdit()
        lineedit_anzahl.setInputMask("00D;_")

        # Eingabe für Benutzername mit strukturierter Maske
        lineedit_username = QLineEdit()
        lineedit_username.setInputMask(">A!A>A!AAaaa0;_")

        # Eingabe für Alter – hier als Geburtsdatum im Format TT.MM.JJJJ
        lineedit_age = QLineEdit()
        lineedit_age.setInputMask("99.99.9999;_")

        # (Optionales Passwortfeld – auskommentiert)
        # lineedit_passwort = QLineEdit()
        # lineedit_passwort.setEchoMode(QLineEdit.EchoMode.Password)

        # ---------- RADIO BUTTONS ----------

        # Zwei RadioButtons, vermutlich für eine Auswahloption
        radio_button = QRadioButton("Anzahl")
        radio_button2 = QRadioButton("Anzahl2")

        # ---------- CHECKBOXEN ----------

        # Zwei Checkboxes – evtl. für zusätzliche Optionen
        check_box = QCheckBox("Anzahl")
        check_box2 = QCheckBox("Anzahl2")

        # ---------- LAYOUT (GRID) ----------

        layout = QGridLayout()  # Erstellt ein Gitterlayout (Tabellenraster)

        # Platzierung der Labels in Spalte 1, Zeilen 1–4
        layout.addWidget(lable_anzahl, 1, 1)
        layout.addWidget(lable_username, 2, 1)
        layout.addWidget(lable_kennzeichen, 3, 1)
        layout.addWidget(lable_age, 4, 1)

        # Platzierung der Eingabefelder in Spalte 2, Zeilen 1–4
        layout.addWidget(lineedit_anzahl, 1, 2)
        layout.addWidget(lineedit_username, 2, 2)
        layout.addWidget(lineedit_kennzeichen, 3, 2)
        layout.addWidget(lineedit_age, 4, 2)

        # Platzierung der Radiobuttons in Zeile 5, Spalten 1 und 2
        layout.addWidget(radio_button, 5, 1)
        layout.addWidget(radio_button2, 5, 2)

        # Platzierung der Checkboxes in Zeile 6, Spalten 1 und 2
        layout.addWidget(check_box, 6, 1)
        layout.addWidget(check_box2, 6, 2)

        # Setzt das definierte Layout als Layout des Widgets
        self.setLayout(layout)
