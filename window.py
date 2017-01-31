import sys
from PyQt5 import QtGui, QtWidgets
def window(text):
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	b = QtWidgets.QLabel(w)
	b.setText(text)
	w.setGeometry(400,400,200,50)
	b.move(50,20)
	w.setWindowTitle("PyQt")
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	window(text)