# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: italic 10pt \"Arial\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 21))
        self.menubar.setObjectName("menubar")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuTargets = QtWidgets.QMenu(self.menubar)
        self.menuTargets.setObjectName("menuTargets")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMake_csv = QtWidgets.QAction(MainWindow)
        self.actionMake_csv.setObjectName("actionMake_csv")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuData.addAction(self.actionMake_csv)
        self.menuData.addAction(self.actionRefresh)
        self.menuTargets.addAction(self.actionAdd)
        self.menuTargets.addAction(self.actionRemove)
        self.menuTargets.addAction(self.actionFind)
        self.menuInfo.addAction(self.actionInfo)
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuTargets.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refresh(self):
        self.listWidget.clear()

        if self.lineEdit.text() == "":
            QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "The directory entry should not be empty!\nPlease enter a valid directory address!");
            return

        address = QtCore.QDir(self.lineEdit.text())

        if (address.exists() == False):
            QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "There is no such directory!\nPlease enter a valid directory address!");
            return

        filters = []
        filters.append("*.txt")
        filters.append("*.docx")
        filters.append("*.doc")

        for item in address.entryList(filters, sort = QtCore.QDir.Name):
            listItem = QtWidgets.QListWidgetItem(item)
            if item.startswith("(c)"):
                listItem.setCheckState(2)
                listItem.setBackground(QtGui.QBrush(QtGui.QColor("lightgreen")))
            else:
                listItem.setCheckState(0)
                listItem.setBackground(QtGui.QBrush(QtGui.QColor("pink")))

            self.listWidget.addItem(listItem)

    def remove(self):
        self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem()))

    def add(self):
        if self.lineEdit.text() == "":
            QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "The target should not be empty!\nPlease enter a valid target name!");
            return

        item =  self.lineEdit.text()
        listItem = QtWidgets.QListWidgetItem(item)

        if item.startswith("(c)"):
            listItem.setCheckState(2)
            listItem.setBackground(QtGui.QBrush(QtGui.QColor("lightgreen")))
        else:
            listItem.setCheckState(0)
            listItem.setBackground(QtGui.QBrush(QtGui.QColor("pink")))

        self.listWidget.addItem(listItem)
        self.listWidget.sortItems(0)

    def find(self):
        if self.lineEdit.text() == "":
            QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "The target should not be empty!\nPlease enter a valid target name!");
            return

        ls = self.listWidget.findItems(self.lineEdit.text(), QtCore.Qt.MatchExactly)

        if ls.__len__() == 0:
                QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "The target name could not be found!\nPlease try again!");
                return

        QtWidgets.QMessageBox.information(self.listWidget, "Found!", "Match is found!\nThe target will be selected now!");

        for i in range(ls.__len__()):
            self.listWidget.setCurrentItem(ls[i])

    def make_csv(self):
        if self.listWidget.count() == 0:
            QtWidgets.QMessageBox.warning(self.listWidget, "Warning!", "There is no data to be written!\nPlease search for files in a valid directory!");
            return

        ls = []

        for i in range(self.listWidget.count()):
            d = {}

            item = self.listWidget.item(i)

            d["Name"] = item.text()

            if item.text().startswith("(c)"):
                d["Status"] = "Completed"
            else:
                d["Status"] = "Incomplete"

            ls.append(d)

        df = pandas.DataFrame(ls)
        df.to_csv("Data.csv")

    def info(self):
        text = "Welcome to Article Planner!\n\n"
        text += "This is a non-commercial application made with Bloggers/Webmasters in mind.\n\n"
        text += 'This application lets you manage all your articles.\n\n'
        text += 'Completed articles are "checked" and are shown with green background.\n'
        text += 'Incomplete articles are "unchecked" and are shown with red background.\n\n'
        text += "As a rule, the articles with names beginning with '(c)' are considered complete!\n\n"
        text += "Example: \n\t(c)ABC.txt - COMPLETE\n\tEFG.txt - INCOMPLETE\n\n"
        text += "You can also make a .csv file of the data shown in the view box\n"
        text += 'by going to Data > "Make \" .csv\"".\n'
        text += "The data is taken from the screen therefore the screen must not be empty.\n\n"
        text += "Only files with extensions .txt, .docx, .doc \nwill be shown the search results.\n\n"
        text += "Thank you for using my application!"

        QtWidgets.QMessageBox.information(self.listWidget, "Info", text);

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter directory address/ new target/ target to find: "))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_3.setText(_translate("MainWindow", "Find"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menuTargets.setTitle(_translate("MainWindow", "Targets"))
        self.actionMake_csv.setText(_translate("MainWindow", "Make \" .csv\""))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionInfo.setText(_translate("MainWindow", "Information"))
        self.pushButton_5.clicked.connect(self.refresh)
        self.pushButton.clicked.connect(self.refresh)
        self.pushButton_4.clicked.connect(self.remove)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.find)
        self.actionAdd.triggered.connect(self.add)
        self.actionFind.triggered.connect(self.find)
        self.actionRemove.triggered.connect(self.remove)
        self.actionRefresh.triggered.connect(self.refresh)
        self.actionMake_csv.triggered.connect(self.make_csv)
        self.actionInfo.triggered.connect(self.info)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
