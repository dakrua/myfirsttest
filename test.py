#import sys
#from PyQt5.QtWidgets import *

#app = QApplication(sys.argv)

#dlgMain = QWidget()
#dlgMain = QDialog()
#dlgMain = QMainWindow()
#dlgMain.setWindowTitle('myWin')
#dlgMain.show()

#app.exec_()
#sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('new')
        self.resize(300, 200)

        self.ledText = QLineEdit('Default Text', self)
        self.ledText.move(100,50)

        self.btnUpdate = QPushButton('Update',self)
        self.btnUpdate.move(100,80)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)

    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
