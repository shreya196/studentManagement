from UI_Py.homePageUI import Ui_Form as logInForm
from studentLogIn import StudentLogIn
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class HomePage(logInForm, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		print("hello")
		self.studentPushButton_4.clicked.connect(self.open)

	def open(self):
		print("Student Button Clicked")
		print("Opening Student Registration Page")
		self.ui = StudentLogIn()
		self.ui.show()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = HomePage()
	sys.exit(app.exec_())