from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

zapitanya_nadpus = QLabel("Якої форми Земля?")
square_btn = QRadioButton("квадратна")
tyt_btn = QRadioButton("кругла")
three_btn = QRadioButton("трикутна")
geode_btn = QRadioButton("геоїд")

main_line = QVBoxLayout()
main_line.addWidget(zapitanya_nadpus)


horizontal_line1 = QHBoxLayout()
horizontal_line2 = QHBoxLayout()
horizontal_line1.addWidget(square_btn)
horizontal_line1.addWidget(tyt_btn)
horizontal_line2.addWidget(three_btn)
horizontal_line2.addWidget(geode_btn)


main_line.addLayout(horizontal_line1)
main_line.addLayout(horizontal_line2)


window.setLayout(main_line)


window.setLayout(main_line)



zapitanya = QLabel("руб?")
fifas = QRadioButton("huh")

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline1.addWidget(fifas)


main_line.addLayout(hline1)
main_line.addLayout(hline2)

window.setLayout(main_line)
window.setLayout(main_line)


def win_btn():
    msg = QMessageBox()
    msg.setText("Ти переміг!")
    msg.exec()



geode_btn.clicked.connect(win_btn)
geode_btn.clicked.connect(win_btn)
window.show()
app.exec()
