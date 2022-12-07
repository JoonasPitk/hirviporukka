# APPLICATON FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================


# LIBRARIES AND MODULES
import sys # Needed for starting the application
from PyQt5.QtWidgets import * # All widgets
from PyQt5 import QtWebEngineWidgets # For showing html content
from PyQt5.uic import loadUi
from PyQt5.QtCore import * # FIXME: Everything for now, change to individual components
from datetime import date

import pgModule, prepareData, figures


# CLASS DEFINITIONS FOR THE APP
class MultiPageMainWindow(QMainWindow):
    
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create an UI from the ui file
        loadUi("MultiPageMainWindow.ui", self)

        # Read database connection arguments from the setting file
        databaseOperation = pgModule.DatabaseOperation()
        self.connectionArguments = databaseOperation.readDatabaseSettingsFromFile(
                "settings.dat")

        
        # UI ELEMENTS TO PROPERTIES
        # Create a status bar to show informative messages (replaces print function used in previous exercises)
        self.statusBar = QStatusBar() # Create a status bar object
        # Set it as the status bar for the main window
        self.setStatusBar(self.statusBar)
        self.statusBar.show() # Make it visible

        # Set current date when the application launches
        self.currentDate = date.today()

        # Summary page (Yhteenveto)
        self.summaryRefreshBtn = self.summaryRefreshPushButton
        self.summaryRefreshBtn.clicked.connect(self.populateSummaryPage)
        self.summaryMeatSharedTW = self.meatSharedTableWidget
        self.summaryGroupSummaryTW = self.groupSummaryTableWidget
        self.sankeyWebV = self.sankeyWebEngineView
        #TODO: Try to set column widths to fill the space available
        # meatSharedTWHeader = self.summaryMeatSharedTW.horizontalHeader()
        # meatSharedTWHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        
        # Kill page (Kaato)
        self.shotByCB = self.shotByComboBox
        self.shotDateDE = self.shotDateEdit
        self.shotLocationLE = self.locationLineEdit
        self.shotAnimalCB = self.animalComboBox
        self.shotAgeGroupCB = self.ageGroupComboBox
        self.shotGenderCB = self.genderComboBox
        self.shotWeightLE = self.weightLineEdit
        self.shotUsageCB = self.usageComboBox
        self.shotAddInfoTE = self.additionalInfoTextEdit
        self.shotSavePushBtn = self.saveShotPushButton
        self.shotSavePushBtn.clicked.connect(self.saveShot) # Signal
        self.shotKillsTW = self.killsTableWidget

       # Share page (Lihanjako)
        self.shareKillsTW = self.shareKillsTableWidget
        self.shareDateDE = self.shareDateEdit
        self.sharePortionCB = self.portionComboBox
        self.shareAmountLE = self.amountLineEdit
        self.shareGroupCB = self.groupComboBox
        self.shareSavePushBtn = self.shareSavePushButton
        self.shareSavePushBtn.clicked.connect(self.saveShare) # Signal

        # License page (Luvat)
        self.licenseYearLE = self.licenseYearLineEdit
        self.licenseAnimalCB = self.licenseAnimalComboBox
        self.licenseAgeGroupCB = self.licenseAgeGroupComboBox
        self.licenseGenderCB = self.licenseGenderComboBox
        self.licenseAmountLE = self.licenseAmountLineEdit
        self.licenseSavePushBtn = self.licenseSavePushButton
        self.licenseSavePushBtn.clicked.connect(self.saveLicense) # Signal
        self.licenseSummaryTW = self.licenseSummaryTableWidget

        # Maintenance page (Ylläpito)
        # TODO: Add UI elements for Ylläpito

        # Signal when a page is opened
        self.pageTab = self.tabWidget
        self.pageTab.currentChanged.connect(self.populateAllPages)
        
        # Signals other than emitted by UI elements
        self.populateAllPages()


    # SLOTS
    # Create an alert dialog for critical failures, eg no database connection established
    def alert(self, windowTitle, alertMsg, additionalMsg, details):
        """Creates a message box for critical errors.

        Args:
            windowTitle (str): Title of the message box
            alertMsg (str): A short description of the error in Finnish
            additionalMsg (str): Additional info in Finnish
            details (str): Details about the error in English
        """
        alertDialog = QMessageBox() # Create a message box object
        alertDialog.setWindowTitle(windowTitle) # Add appropriate title to the message box
        alertDialog.setIcon(QMessageBox.Critical) # Set icon to critical
        alertDialog.setText(alertMsg) # Basic information about the error in Finnish
        alertDialog.setInformativeText(additionalMsg) # Additional information about the error in Finnish
        alertDialog.setDetailedText(details) # Technical details in English (from psycopg2)
        alertDialog.setStandardButtons(QMessageBox.Ok) # Only OK is needed to close the dialog
        alertDialog.exec_() # Open the message box

    def populateSummaryPage(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(
                self.connectionArguments, "public.jaetut_lihat")

        # Check if an error has occurred
        if databaseOperation1.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation1.errorMessage,
                    databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.summaryMeatSharedTW)

        # Read data from view jakoryhma_yhteenveto
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(
                self.connectionArguments, "public.jakoryhma_yhteenveto")
        
        # figure = figures.createSankeyChart()
        # figure = figures.testChart()
        htmlFile = 'meatstreams.html'
        urlString = f'file:///{htmlFile}'
        # figures.createOfflineFile(figure, htmlFile) # Write the chart to a html file
        url = QUrl(urlString) # Create a relative url to the file
        self.sankeyWebV.load(url) # Load it into the web view element
        
        # Check if an error has occurred
        if databaseOperation2.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation2.errorMessage,
                    databaseOperation2.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation2, self.summaryGroupSummaryTW)
        
    def populateKillPage(self):
        # Set default date to current date
        self.shotDateDE.setDate(self.currentDate)
        
        # Read data from view kaatoluettelo
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(
                self.connectionArguments, "public.kaatoluettelo")
        
        # Check if an error has occurred
        if databaseOperation1.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation1.errorMessage,
                    databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.shotKillsTW)
        
        # Read data from view nimivalinta, and populate the combo box
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(
                self.connectionArguments, "public.nimivalinta")
        
        # Check if an error has occurred
        if databaseOperation2.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation2.errorMessage,
                    databaseOperation2.detailedMessage)
        else:
            self.shotByIdList = prepareData.prepareComboBox(
                databaseOperation2, self.shotByCB, 1, 0)
        
        # Read data from table elain, and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(
                self.connectionArguments, "public.elain")
        
        # Check if an error has occurred
        if databaseOperation3.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation3.errorMessage,
                    databaseOperation3.detailedMessage)
        else:
           self.shotAnimalText = prepareData.prepareComboBox(
                databaseOperation3, self.shotAnimalCB, 0, 0)

        # Read data from table aikuinenvasa, and populate the combo box
        databaseOperation4 = pgModule.DatabaseOperation()
        databaseOperation4.getAllRowsFromTable(
                self.connectionArguments, "public.aikuinenvasa")
        
        # Check if an error has occurred
        if databaseOperation4.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation4.errorMessage,
                    databaseOperation4.detailedMessage)
        else:
            self.shotAgeGroupText = prepareData.prepareComboBox(
                databaseOperation4, self.shotAgeGroupCB, 0, 0)

        # Read data from table sukupuoli, and populate the combo box
        databaseOperation5 = pgModule.DatabaseOperation()
        databaseOperation5.getAllRowsFromTable(
                self.connectionArguments, "public.sukupuoli")
        
        # Check if an error has occurred
        if databaseOperation5.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation5.errorMessage,
                    databaseOperation5.detailedMessage)
        else:
            self.shotGenderText = prepareData.prepareComboBox(
                databaseOperation5, self.shotGenderCB, 0, 0)

        # Read data from table kasittely, and populate the combo box
        databaseOperation6 = pgModule.DatabaseOperation()
        databaseOperation6.getAllRowsFromTable(
                self.connectionArguments, "public.kasittely")
        
        # Check if an error has occurred
        if databaseOperation6.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation6.errorMessage,
                    databaseOperation6.detailedMessage)
        else:
            self.shotUsageIdList = prepareData.prepareComboBox(
                databaseOperation6, self.shotUsageCB, 1, 0)

    # TODO: Finish populateSharePage
    def populateSharePage(self):
        # Set default date to current date
        self.shareDateDE.setDate(self.currentDate)
        
        # Read data from view kaatoyhteenveto
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(
                self.connectionArguments, "public.jaettavat_lihat")
        
        # Check if an error has occurred
        if databaseOperation1.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation1.errorMessage,
                    databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.shareKillsTW)
        
        # Read data from table ruhonosa, and populate the combo box
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(
                self.connectionArguments, "public.ruhonosa")
        
        # Check if an error has occurred
        if databaseOperation2.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation2.errorMessage,
                    databaseOperation2.detailedMessage)
        else:
            self.sharePortionText = prepareData.prepareComboBox(
                databaseOperation2, self.sharePortionCB, 0, 0)
        
        # Read data from table jakoryhma, and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(
                self.connectionArguments, "public.jakoryhma")
        
        # Check if an error has occurred
        if databaseOperation3.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation3.errorMessage,
                    databaseOperation3.detailedMessage)
        else:
           self.shareGroupList = prepareData.prepareComboBox(
                databaseOperation3, self.shareGroupCB, 2, 0)

    # TODO: Finish populateLicensePage
    def populateLicensePage(self):
        # Read data from table lupa
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(
                self.connectionArguments, "public.lupa")
        
        # Check if an error has occurred
        if databaseOperation1.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation1.errorMessage,
                    databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.licenseSummaryTW)
        
        # Read data from table elain, and populate the combo box
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(
                self.connectionArguments, "public.elain")
        
        # Check if an error has occurred
        if databaseOperation2.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation2.errorMessage,
                    databaseOperation2.detailedMessage)
        else:
            self.licenseAnimalList = prepareData.prepareComboBox(
                databaseOperation2, self.licenseAnimalCB, 0, 0)
        
        # Read data from table aikuinenvasa, and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(
                self.connectionArguments, "public.aikuinenvasa")
        
        # Check if an error has occurred
        if databaseOperation3.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation3.errorMessage,
                    databaseOperation3.detailedMessage)
        else:
           self.licenseAgeGroupList = prepareData.prepareComboBox(
                databaseOperation3, self.licenseAgeGroupCB, 0, 0)

        # Read data from table sukupuoli, and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(
                self.connectionArguments, "public.sukupuoli")
        
        # Check if an error has occurred
        if databaseOperation3.errorCode != 0:
            self.alert(
                    "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                    databaseOperation3.errorMessage,
                    databaseOperation3.detailedMessage)
        else:
           self.licenseGenderList = prepareData.prepareComboBox(
                databaseOperation3, self.licenseGenderCB, 0, 0)

    def populateAllPages(self):
        self.populateSummaryPage()
        self.populateKillPage()
        self.populateSharePage()
        self.populateLicensePage()

        testDBConnection = pgModule.DatabaseOperation()
        connectionArgs = testDBConnection.readDatabaseSettingsFromFile('settings.dat')
        testDBConnection.testConnection(connectionArgs)
        if testDBConnection.errorCode == 0:
            self.populateSummaryPage()
            self.populateKillPage()
        else:
            self.alert('Tarkista tietokanta-asetukset', 'settings.dat-tiedostosta','no further information','no further information')

    def saveShot(self):
        errorOccurred = False
        try:
            shotByChosenItemIdx = self.shotByCB.currentIndex() # Row index of the selected row
            shotById = self.shotByIdList[shotByChosenItemIdx] # ID value of the selected row
            shootingDay = self.shotDateDE.date().toPyDate() # Python data is in ISO format
            shootingPlace = self.shotLocationLE.text() # Text value of line edit
            animal = self.shotAnimalCB.currentText() # Selected value of the combo box
            ageGroup = self.shotAgeGroupCB.currentText() # Selected value of the combo box
            gender = self.shotGenderCB.currentText() # Selected value of the combo box
            weight = float(self.shotWeightLE.text()) # Convert line edit value into float (real in the DB)
            useIdx = self.shotUsageCB.currentIndex() # Row index of the selected row
            use = self.shotUsageIdList[useIdx] # ID value of the selected row
            additionalInfo = self.shotAddInfoTE.toPlainText() # Convert multiline text edit into plain text

            # Insert data into kaato table
            # Create an SQL clause to insert element values to the database
            sqlClauseBeginning = """INSERT INTO public.kaato(
                jasen_id, kaatopaiva, ruhopaino, paikka_teksti,
                kasittelyid, elaimen_nimi, sukupuoli,
                ikaluokka, lisatieto) VALUES("""
            sqlClauseValues = f"{shotById}, '{shootingDay}', {weight}, '{shootingPlace}', {use}, '{animal}', '{gender}', '{ageGroup}', '{additionalInfo}'"
            sqlClauseEnd = ");"
            sqlClause = sqlClauseBeginning + sqlClauseValues + sqlClauseEnd

        except Exception as error:
            errorOccurred = True
            self.alert("Virheellinen syöte", "Tarkista antamasi tiedot.",
                "Tyyppivirhe.", str(error))

        finally:
            if errorOccurred == False:
                # Create a databaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(
                        self.connectionArguments, sqlClause)
        
                # Check if an error has occurred
                if databaseOperation.errorCode != 0:
                    self.alert(
                            "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                            databaseOperation.errorMessage,
                            databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data entries
                    # and clear previous data from fields
                    self.populateKillPage()
                    self.shotLocationLE.clear()
                    self.shotWeightLE.clear()
                    self.shotAddInfoTE.clear()

    # TODO: Finish saveShare.
    def saveShare(self):
        errorOccurred = False
        try:
            shareDate = self.shareDateDE.date().toPyDate() # Python data is in ISO format
            portion = self.sharePortionCB.currentText() # Selected value of the combo box
            weight = float(self.shareAmountLE.text()) # Convert line edit value into float (real in the DB)
            shareByChosenItemIdx = self.shareGroupCB.currentIndex() # Row index of the selected row
            group = self.shareGroupList[shareByChosenItemIdx] # ID value of the selected row
            shareKillChosenRowIdx = self.shareKillsTW.currentRow() # The chosen row
            shareKillId = int(self.shareKillsTW.itemAt(shareKillChosenRowIdx, 0).text()) # Convert to text and then int

            # Insert data into jakotapahtuma table
            # Create an SQL clause to insert element values to the database
            sqlClauseBeginning = """INSERT INTO public.jakotapahtuma(
                paiva, osnimitys, maara, ryhma_id, kaato_id) VALUES("""
            sqlClauseValues = f"'{shareDate}', '{portion}', {weight}, '{group}', {shareKillId}"
            sqlClauseEnd = ");"
            sqlClause = sqlClauseBeginning + sqlClauseValues + sqlClauseEnd

        except Exception as error:
            errorOccurred = True
            self.alert("Virheellinen syöte", "Tarkista antamasi tiedot.",
                "Tyyppivirhe.", str(error))

        finally:
            if errorOccurred == False:
                # Create a databaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(
                        self.connectionArguments, sqlClause)
        
                # Check if an error has occurred
                if databaseOperation.errorCode != 0:
                    self.alert(
                            "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                            databaseOperation.errorMessage,
                            databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data entries
                    # and clear previous data from fields
                    self.populateSharePage()
                    self.shareAmountLE.clear()

    # TODO: Finish saveLicense
    def saveLicense(self):
        errorOccurred = False
        try:
            licenseYear = self.licenseYearLE.text() # Text value of line edit
            animal = self.licenseAnimalCB.currentText() # Selected value of the combo box
            ageGroup = self.licenseAgeGroupCB.currentText() # Selected value of the combo box
            gender = self.licenseGenderCB.currentText() # Selected value of the combo box
            amount = self.licenseAmountLE.text() # Text value of line edit
            
            # Insert data into lupa table
            # Create an SQL clause to insert element values to the database
            sqlClauseBeginning = """INSERT INTO public.lupa(
                lupavuosi, seura_id, elaimen_nimi, ikaluokka, sukupuoli, maara) VALUES("""
            sqlClauseValues = f"{licenseYear}, 1, '{animal}', '{ageGroup}', '{gender}', {amount}"
            sqlClauseEnd = ");"
            sqlClause = sqlClauseBeginning + sqlClauseValues + sqlClauseEnd

        except Exception as error:
            errorOccurred = True
            self.alert("Virheellinen syöte", "Tarkista antamasi tiedot.",
                "Tyyppivirhe.", str(error))

        finally:
            if errorOccurred == False:
                # Create a databaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(
                        self.connectionArguments, sqlClause)
        
                # Check if an error has occurred
                if databaseOperation.errorCode != 0:
                    self.alert(
                            "Vakava virhe", "Tietokantaoperaatio epäonnistui.",
                            databaseOperation.errorMessage,
                            databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data entries
                    # and clear previous data from fields
                    self.populateLicensePage()
                    self.licenseYearLE.clear()
                    self.licenseAmountLE.clear()

# APPLICATION CREATION AND STARTUP
# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Create the Main Window object from MultiPageMainWindow Class and show it on the screen
    appWindow = MultiPageMainWindow()
    appWindow.show()  # This can also be included in the MultiPageMainWindow class
    sys.exit(app.exec_())
