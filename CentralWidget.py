from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QRadioButton, QCheckBox, QButtonGroup


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        lable_anzahl = QLabel("Anzahl an Artikeln pro Stück:")
        lable_anzahl.setAlignment(Qt.AlignmentFlag.AlignRight)
        lable_username = QLabel("Benutzername:")
        lable_username.setAlignment(Qt.AlignmentFlag.AlignRight)
        lable_kennzeichen = QLabel("Kennzeichen:")
        lable_kennzeichen.setAlignment(Qt.AlignmentFlag.AlignRight)
        lable_age = QLabel("Alter:")
        lable_age.setAlignment(Qt.AlignmentFlag.AlignRight)

        # lable_passwort = QLabel("Passwort:")
        # lable_passwort.setAlignment(Qt.AlignmentFlag.AlignRight)

        lineedit_kennzeichen = QLineEdit()
        lineedit_kennzeichen.setInputMask(">A!aa:>aA! 0009 >a!;_")
        lineedit_anzahl = QLineEdit()
        lineedit_anzahl.setInputMask("00D;_")
        lineedit_username = QLineEdit()
        lineedit_username.setInputMask(">A!A>A!AAaaa0;_")
        lineedit_age = QLineEdit()
        lineedit_age.setInputMask("99.99.9999;_")
        # lineedit_passwort = QLineEdit()
        # lineedit_passwort.setEchoMode(QLineEdit.EchoMode.Password)

        radio_button = QRadioButton("Anzahl")
        radio_button2 = QRadioButton("Anzahl2")

        check_box = QCheckBox("Anzahl")
        check_box2 = QCheckBox("Anzahl2")

        layout = QGridLayout()
        layout.addWidget(lable_anzahl, 1, 1)
        layout.addWidget(lable_username, 2, 1)
        layout.addWidget(lable_kennzeichen, 3, 1)
        layout.addWidget(lable_age, 4, 1)
        layout.addWidget(lineedit_anzahl, 1, 2)
        layout.addWidget(lineedit_username, 2, 2)
        layout.addWidget(lineedit_kennzeichen, 3, 2)
        layout.addWidget(lineedit_age, 4, 2)
        layout.addWidget(radio_button, 5, 1)
        layout.addWidget(radio_button2, 5, 2)
        layout.addWidget(check_box, 6, 1)
        layout.addWidget(check_box2, 6, 2)

        self.setLayout(layout)