# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JP\Documents\GitHub\hirviporukka\multiPageMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.summaryPage = QtWidgets.QWidget()
        self.summaryPage.setObjectName("summaryPage")
        self.meatSharedTableWidget = QtWidgets.QTableWidget(self.summaryPage)
        self.meatSharedTableWidget.setGeometry(QtCore.QRect(10, 50, 301, 192))
        self.meatSharedTableWidget.setStyleSheet("")
        self.meatSharedTableWidget.setObjectName("meatSharedTableWidget")
        self.meatSharedTableWidget.setColumnCount(0)
        self.meatSharedTableWidget.setRowCount(0)
        self.groupSummaryTableWidget = QtWidgets.QTableWidget(self.summaryPage)
        self.groupSummaryTableWidget.setGeometry(QtCore.QRect(10, 290, 301, 192))
        self.groupSummaryTableWidget.setObjectName("groupSummaryTableWidget")
        self.groupSummaryTableWidget.setColumnCount(0)
        self.groupSummaryTableWidget.setRowCount(0)
        self.sharedMeatLabel = QtWidgets.QLabel(self.summaryPage)
        self.sharedMeatLabel.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.sharedMeatLabel.setObjectName("sharedMeatLabel")
        self.groupSummaryLabel = QtWidgets.QLabel(self.summaryPage)
        self.groupSummaryLabel.setGeometry(QtCore.QRect(10, 270, 151, 16))
        self.groupSummaryLabel.setObjectName("groupSummaryLabel")
        self.summaryRefreshPushButton = QtWidgets.QPushButton(self.summaryPage)
        self.summaryRefreshPushButton.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.summaryRefreshPushButton.setObjectName("summaryRefreshPushButton")
        self.summarySuggestGroupBox = QtWidgets.QGroupBox(self.summaryPage)
        self.summarySuggestGroupBox.setGeometry(QtCore.QRect(330, 40, 251, 441))
        self.summarySuggestGroupBox.setObjectName("summarySuggestGroupBox")
        self.tabWidget.addTab(self.summaryPage, "")
        self.killPage = QtWidgets.QWidget()
        self.killPage.setObjectName("killPage")
        self.shotByComboBox = QtWidgets.QComboBox(self.killPage)
        self.shotByComboBox.setGeometry(QtCore.QRect(10, 40, 191, 22))
        self.shotByComboBox.setObjectName("shotByComboBox")
        self.shotByLabel = QtWidgets.QLabel(self.killPage)
        self.shotByLabel.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.shotByLabel.setObjectName("shotByLabel")
        self.shotDateEdit = QtWidgets.QDateEdit(self.killPage)
        self.shotDateEdit.setGeometry(QtCore.QRect(220, 40, 121, 22))
        self.shotDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.shotDateEdit.setCalendarPopup(True)
        self.shotDateEdit.setDate(QtCore.QDate(2022, 11, 15))
        self.shotDateEdit.setObjectName("shotDateEdit")
        self.shotDateLabel = QtWidgets.QLabel(self.killPage)
        self.shotDateLabel.setGeometry(QtCore.QRect(220, 20, 101, 16))
        self.shotDateLabel.setObjectName("shotDateLabel")
        self.animalComboBox = QtWidgets.QComboBox(self.killPage)
        self.animalComboBox.setGeometry(QtCore.QRect(10, 90, 191, 22))
        self.animalComboBox.setObjectName("animalComboBox")
        self.ageGroupComboBox = QtWidgets.QComboBox(self.killPage)
        self.ageGroupComboBox.setGeometry(QtCore.QRect(220, 90, 121, 22))
        self.ageGroupComboBox.setObjectName("ageGroupComboBox")
        self.genderComboBox = QtWidgets.QComboBox(self.killPage)
        self.genderComboBox.setGeometry(QtCore.QRect(360, 90, 121, 22))
        self.genderComboBox.setObjectName("genderComboBox")
        self.animalLabel = QtWidgets.QLabel(self.killPage)
        self.animalLabel.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.animalLabel.setObjectName("animalLabel")
        self.ageGroupLabel = QtWidgets.QLabel(self.killPage)
        self.ageGroupLabel.setGeometry(QtCore.QRect(220, 70, 61, 16))
        self.ageGroupLabel.setObjectName("ageGroupLabel")
        self.genderLabel = QtWidgets.QLabel(self.killPage)
        self.genderLabel.setGeometry(QtCore.QRect(360, 70, 61, 16))
        self.genderLabel.setObjectName("genderLabel")
        self.usageComboBox = QtWidgets.QComboBox(self.killPage)
        self.usageComboBox.setGeometry(QtCore.QRect(90, 140, 111, 22))
        self.usageComboBox.setObjectName("usageComboBox")
        self.weightLineEdit = QtWidgets.QLineEdit(self.killPage)
        self.weightLineEdit.setGeometry(QtCore.QRect(10, 140, 61, 20))
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.weightLabel = QtWidgets.QLabel(self.killPage)
        self.weightLabel.setGeometry(QtCore.QRect(10, 120, 47, 13))
        self.weightLabel.setObjectName("weightLabel")
        self.usageLabel = QtWidgets.QLabel(self.killPage)
        self.usageLabel.setGeometry(QtCore.QRect(90, 120, 47, 13))
        self.usageLabel.setObjectName("usageLabel")
        self.additionalInfoTextEdit = QtWidgets.QPlainTextEdit(self.killPage)
        self.additionalInfoTextEdit.setGeometry(QtCore.QRect(220, 140, 361, 71))
        self.additionalInfoTextEdit.setToolTipDuration(10000)
        self.additionalInfoTextEdit.setObjectName("additionalInfoTextEdit")
        self.additionalInfoLabel = QtWidgets.QLabel(self.killPage)
        self.additionalInfoLabel.setGeometry(QtCore.QRect(220, 120, 51, 16))
        self.additionalInfoLabel.setObjectName("additionalInfoLabel")
        self.killsKillsTableWidget = QtWidgets.QTableWidget(self.killPage)
        self.killsKillsTableWidget.setGeometry(QtCore.QRect(10, 280, 571, 192))
        self.killsKillsTableWidget.setObjectName("killsKillsTableWidget")
        self.killsKillsTableWidget.setColumnCount(0)
        self.killsKillsTableWidget.setRowCount(0)
        self.killsTableLabel = QtWidgets.QLabel(self.killPage)
        self.killsTableLabel.setGeometry(QtCore.QRect(10, 260, 47, 13))
        self.killsTableLabel.setObjectName("killsTableLabel")
        self.saveShotPushButton = QtWidgets.QPushButton(self.killPage)
        self.saveShotPushButton.setGeometry(QtCore.QRect(510, 220, 75, 23))
        self.saveShotPushButton.setObjectName("saveShotPushButton")
        self.locationLineEdit = QtWidgets.QLineEdit(self.killPage)
        self.locationLineEdit.setGeometry(QtCore.QRect(360, 40, 221, 20))
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.locationLabel = QtWidgets.QLabel(self.killPage)
        self.locationLabel.setGeometry(QtCore.QRect(360, 20, 101, 16))
        self.locationLabel.setObjectName("locationLabel")
        self.tabWidget.addTab(self.killPage, "")
        self.sharePage = QtWidgets.QWidget()
        self.sharePage.setObjectName("sharePage")
        self.shareKillsTableWidget = QtWidgets.QTableWidget(self.sharePage)
        self.shareKillsTableWidget.setGeometry(QtCore.QRect(10, 30, 571, 192))
        self.shareKillsTableWidget.setObjectName("shareKillsTableWidget")
        self.shareKillsTableWidget.setColumnCount(0)
        self.shareKillsTableWidget.setRowCount(0)
        self.shareKillsLabel = QtWidgets.QLabel(self.sharePage)
        self.shareKillsLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.shareKillsLabel.setObjectName("shareKillsLabel")
        self.shareDateEdit = QtWidgets.QDateEdit(self.sharePage)
        self.shareDateEdit.setGeometry(QtCore.QRect(10, 250, 121, 22))
        self.shareDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.shareDateEdit.setCalendarPopup(True)
        self.shareDateEdit.setDate(QtCore.QDate(2022, 11, 15))
        self.shareDateEdit.setObjectName("shareDateEdit")
        self.portionComboBox = QtWidgets.QComboBox(self.sharePage)
        self.portionComboBox.setGeometry(QtCore.QRect(150, 250, 121, 22))
        self.portionComboBox.setObjectName("portionComboBox")
        self.amountLineEdit = QtWidgets.QLineEdit(self.sharePage)
        self.amountLineEdit.setGeometry(QtCore.QRect(290, 250, 113, 20))
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.shareDateLabel = QtWidgets.QLabel(self.sharePage)
        self.shareDateLabel.setGeometry(QtCore.QRect(10, 230, 47, 13))
        self.shareDateLabel.setObjectName("shareDateLabel")
        self.portionLabel = QtWidgets.QLabel(self.sharePage)
        self.portionLabel.setGeometry(QtCore.QRect(150, 230, 61, 16))
        self.portionLabel.setObjectName("portionLabel")
        self.amountLabel = QtWidgets.QLabel(self.sharePage)
        self.amountLabel.setGeometry(QtCore.QRect(290, 230, 61, 16))
        self.amountLabel.setObjectName("amountLabel")
        self.groupLabel = QtWidgets.QLabel(self.sharePage)
        self.groupLabel.setGeometry(QtCore.QRect(420, 230, 61, 16))
        self.groupLabel.setObjectName("groupLabel")
        self.groupComboBox = QtWidgets.QComboBox(self.sharePage)
        self.groupComboBox.setGeometry(QtCore.QRect(420, 250, 161, 22))
        self.groupComboBox.setObjectName("groupComboBox")
        self.shareSavePushButton = QtWidgets.QPushButton(self.sharePage)
        self.shareSavePushButton.setGeometry(QtCore.QRect(500, 280, 75, 23))
        self.shareSavePushButton.setObjectName("shareSavePushButton")
        self.shareSuggestGroupBox = QtWidgets.QGroupBox(self.sharePage)
        self.shareSuggestGroupBox.setGeometry(QtCore.QRect(10, 310, 571, 201))
        self.shareSuggestGroupBox.setObjectName("shareSuggestGroupBox")
        self.tabWidget.addTab(self.sharePage, "")
        self.licensePage = QtWidgets.QWidget()
        self.licensePage.setObjectName("licensePage")
        self.licenseYearLineEdit = QtWidgets.QLineEdit(self.licensePage)
        self.licenseYearLineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.licenseYearLineEdit.setObjectName("licenseYearLineEdit")
        self.licenseYearLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseYearLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.licenseYearLabel.setObjectName("licenseYearLabel")
        self.licenseAnimalComboBox = QtWidgets.QComboBox(self.licensePage)
        self.licenseAnimalComboBox.setGeometry(QtCore.QRect(130, 30, 141, 22))
        self.licenseAnimalComboBox.setObjectName("licenseAnimalComboBox")
        self.licenseAnimalLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseAnimalLabel.setGeometry(QtCore.QRect(130, 10, 47, 13))
        self.licenseAnimalLabel.setObjectName("licenseAnimalLabel")
        self.licenseAgeGroupComboBox = QtWidgets.QComboBox(self.licensePage)
        self.licenseAgeGroupComboBox.setGeometry(QtCore.QRect(280, 30, 111, 22))
        self.licenseAgeGroupComboBox.setObjectName("licenseAgeGroupComboBox")
        self.licenseAgeGroupLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseAgeGroupLabel.setGeometry(QtCore.QRect(280, 10, 47, 13))
        self.licenseAgeGroupLabel.setObjectName("licenseAgeGroupLabel")
        self.licenseGenderComboBox = QtWidgets.QComboBox(self.licensePage)
        self.licenseGenderComboBox.setGeometry(QtCore.QRect(400, 30, 81, 22))
        self.licenseGenderComboBox.setObjectName("licenseGenderComboBox")
        self.licenseGengerLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseGengerLabel.setGeometry(QtCore.QRect(400, 10, 47, 13))
        self.licenseGengerLabel.setObjectName("licenseGengerLabel")
        self.licenseAmountLineEdit = QtWidgets.QLineEdit(self.licensePage)
        self.licenseAmountLineEdit.setGeometry(QtCore.QRect(490, 30, 61, 20))
        self.licenseAmountLineEdit.setObjectName("licenseAmountLineEdit")
        self.licenseAmountLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseAmountLabel.setGeometry(QtCore.QRect(490, 10, 47, 13))
        self.licenseAmountLabel.setObjectName("licenseAmountLabel")
        self.licenseSavePushButton = QtWidgets.QPushButton(self.licensePage)
        self.licenseSavePushButton.setGeometry(QtCore.QRect(480, 60, 75, 23))
        self.licenseSavePushButton.setObjectName("licenseSavePushButton")
        self.licenseSummaryTableWidget = QtWidgets.QTableWidget(self.licensePage)
        self.licenseSummaryTableWidget.setGeometry(QtCore.QRect(10, 120, 541, 192))
        self.licenseSummaryTableWidget.setObjectName("licenseSummaryTableWidget")
        self.licenseSummaryTableWidget.setColumnCount(0)
        self.licenseSummaryTableWidget.setRowCount(0)
        self.licenseSummaryTableLabel = QtWidgets.QLabel(self.licensePage)
        self.licenseSummaryTableLabel.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.licenseSummaryTableLabel.setObjectName("licenseSummaryTableLabel")
        self.tabWidget.addTab(self.licensePage, "")
        self.maintenancePage = QtWidgets.QWidget()
        self.maintenancePage.setObjectName("maintenancePage")
        self.groupBox = QtWidgets.QGroupBox(self.maintenancePage)
        self.groupBox.setGeometry(QtCore.QRect(300, 10, 281, 181))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.maintenancePage)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 280, 281, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.maintenancePage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 200, 271, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.maintenancePage)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 271, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tabWidget.addTab(self.maintenancePage, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.summaryRefreshPushButton, self.meatSharedTableWidget)
        MainWindow.setTabOrder(self.meatSharedTableWidget, self.groupSummaryTableWidget)
        MainWindow.setTabOrder(self.groupSummaryTableWidget, self.killsKillsTableWidget)
        MainWindow.setTabOrder(self.killsKillsTableWidget, self.licenseSummaryTableWidget)
        MainWindow.setTabOrder(self.licenseSummaryTableWidget, self.shotByComboBox)
        MainWindow.setTabOrder(self.shotByComboBox, self.shotDateEdit)
        MainWindow.setTabOrder(self.shotDateEdit, self.locationLineEdit)
        MainWindow.setTabOrder(self.locationLineEdit, self.animalComboBox)
        MainWindow.setTabOrder(self.animalComboBox, self.ageGroupComboBox)
        MainWindow.setTabOrder(self.ageGroupComboBox, self.genderComboBox)
        MainWindow.setTabOrder(self.genderComboBox, self.weightLineEdit)
        MainWindow.setTabOrder(self.weightLineEdit, self.usageComboBox)
        MainWindow.setTabOrder(self.usageComboBox, self.additionalInfoTextEdit)
        MainWindow.setTabOrder(self.additionalInfoTextEdit, self.saveShotPushButton)
        MainWindow.setTabOrder(self.saveShotPushButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.shareDateEdit)
        MainWindow.setTabOrder(self.shareDateEdit, self.portionComboBox)
        MainWindow.setTabOrder(self.portionComboBox, self.amountLineEdit)
        MainWindow.setTabOrder(self.amountLineEdit, self.groupComboBox)
        MainWindow.setTabOrder(self.groupComboBox, self.shareSavePushButton)
        MainWindow.setTabOrder(self.shareSavePushButton, self.shareKillsTableWidget)
        MainWindow.setTabOrder(self.shareKillsTableWidget, self.licenseYearLineEdit)
        MainWindow.setTabOrder(self.licenseYearLineEdit, self.licenseAnimalComboBox)
        MainWindow.setTabOrder(self.licenseAnimalComboBox, self.licenseAgeGroupComboBox)
        MainWindow.setTabOrder(self.licenseAgeGroupComboBox, self.licenseGenderComboBox)
        MainWindow.setTabOrder(self.licenseGenderComboBox, self.licenseAmountLineEdit)
        MainWindow.setTabOrder(self.licenseAmountLineEdit, self.licenseSavePushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sharedMeatLabel.setText(_translate("MainWindow", "Jaetut lihat ryhmittäin"))
        self.groupSummaryLabel.setText(_translate("MainWindow", "Ryhmän tiedot"))
        self.summaryRefreshPushButton.setText(_translate("MainWindow", "Päivitä"))
        self.summarySuggestGroupBox.setTitle(_translate("MainWindow", "Ehdotukset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summaryPage), _translate("MainWindow", "Yhteenveto"))
        self.shotByLabel.setText(_translate("MainWindow", "Kaataja"))
        self.shotDateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.shotDateLabel.setText(_translate("MainWindow", "Kaatopäivä"))
        self.animalLabel.setText(_translate("MainWindow", "Eläin"))
        self.ageGroupLabel.setText(_translate("MainWindow", "Ikäryhmä"))
        self.genderLabel.setText(_translate("MainWindow", "Sukupuoli"))
        self.weightLabel.setText(_translate("MainWindow", "Paino (kg)"))
        self.usageLabel.setText(_translate("MainWindow", "Käyttö"))
        self.additionalInfoTextEdit.setToolTip(_translate("MainWindow", "Tähän vieraan kaatajan nimi tai havaintoja eläimestä"))
        self.additionalInfoLabel.setText(_translate("MainWindow", "Lisätietoja"))
        self.killsTableLabel.setText(_translate("MainWindow", "Kaadot"))
        self.saveShotPushButton.setText(_translate("MainWindow", "Tallenna"))
        self.locationLineEdit.setToolTip(_translate("MainWindow", "Karttaan merkitty paikannimi"))
        self.locationLabel.setText(_translate("MainWindow", "Paikka"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.killPage), _translate("MainWindow", "Kaato"))
        self.shareKillsTableWidget.setToolTip(_translate("MainWindow", "Valitse kaato, jonka lihoja jaetaan"))
        self.shareKillsLabel.setText(_translate("MainWindow", "Kaadot"))
        self.shareDateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.shareDateLabel.setText(_translate("MainWindow", "Jakopäivä"))
        self.portionLabel.setText(_translate("MainWindow", "Ruhon osa"))
        self.amountLabel.setText(_translate("MainWindow", "Määrä (kg)"))
        self.groupLabel.setText(_translate("MainWindow", "Jakoryhmä"))
        self.shareSavePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.shareSuggestGroupBox.setTitle(_translate("MainWindow", "Jakoehdotukset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sharePage), _translate("MainWindow", "Lihanjako"))
        self.licenseYearLabel.setText(_translate("MainWindow", "Lupavuosi"))
        self.licenseAnimalLabel.setText(_translate("MainWindow", "Eläin"))
        self.licenseAgeGroupLabel.setText(_translate("MainWindow", "Ikäryhmä"))
        self.licenseGengerLabel.setText(_translate("MainWindow", "Sukupuoli"))
        self.licenseAmountLabel.setText(_translate("MainWindow", "Määrä"))
        self.licenseSavePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.licenseSummaryTableLabel.setText(_translate("MainWindow", "Myönnetyt luvat"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.licensePage), _translate("MainWindow", "Luvat"))
        self.groupBox.setTitle(_translate("MainWindow", "Seura"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Seurue"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Jakoryhmä"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Jäsen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintenancePage), _translate("MainWindow", "Ylläpito"))
