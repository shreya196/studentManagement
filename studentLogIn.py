from UI_Py.studentLogInUI import Ui_MainWindow as resgistrationForm
from PyQt5 import QtWidgets, QtSql
import sys
#import mysql.connector

#conn = mysql.connector.connect(user='root', password='123987', host='localhost', database='')
#mycursor = conn.cursor()



class StudentLogIn(resgistrationForm, QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.registerPushButton_2.clicked.connect(self.register)
		self.loginPushButton.clicked.connect(self.signin)

	def register(self):
		user = "root"
		passWord = "123987"
		dbName = "python"
		db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
		db.setUserName(user)
		db.setPassword(passWord)
		db.setDatabaseName(dbName)
		print("Registering Student")
		name = self.nameLineEdit.text()
		rollno = self.rollNoLineEdit_4.text()
		gender = self.genderComboBox.currentText()
		branch = self.branchComboBox_2.currentText()
		dob = self.dobDateEdit.text()
		contact = self.contactLineEdit_5.text()
		email = self.emailLineEdit_6.text()
		password = self.passwordLineEdit_7.text()
#		print(name,rollno,gender,branch,dob,contact,email,password)		
		if db.open():
			print("Connection Established")
			query = QtSql.QSqlQuerry()
			query.exec_("insert into ")
			print("student Registered")
		else:
			print("Database Connection Error")
			print("student not Registered..plz try again!!")


		self.nameLineEdit.clear()
		self.rollNoLineEdit_4.clear()
		self.genderComboBox.clear()
#		self.branchComboBox_2.clear()
#		self.dobDateEdit.clear()
		self.contactLineEdit_5.clear()
		self.emailLineEdit_6.clear()
		self.passwordLineEdit_7.clear()

#		mycursor.execute('use StudentManagement')
#		print(dob)
#		print(mycursor)
#		mycursor.execute('insert into Student values(%s, %s, %s, %s, %s, %s, %s, %s)', (name,rollno,gender,branch,dob,contact,email,password))
#		conn.commit()
#		print(mycursor)

	def signin(self):
		print("Signing In")
		sid = self.sidLineEdit_2.text()
		password = self.passwordLineEdit_3.text()
#		mycursor.execute('use StudentManagement')
#		mycursor.execute('select * from Student where (RollNo = %s AND Password = %s)',(sid, password) )
		
#		detail = mycursor.fetchall()
#		print(detail)
