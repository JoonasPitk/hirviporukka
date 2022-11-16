# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES
import sys # Needed for booting up the application
from PyQt5.QtWidgets import * # Bring all Qt widgets
from PyQt5.uic import loadUi # For loading the user interface from .ui file

import pgModule, prepareData

# CLASS DEFINITIONS FOR THE APPLICATION
class GroupMainWindow(QMainWindow):
    
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)
    
        # Create the user interface from the .ui file
        loadUi("groupInfoMainWindow.ui", self,)
    
        # Define properties for UI elements
        self.refreshBtn = self.refreshPushButton
        self.meatShrInfo = self.meatShareTableWidget
        self.groupSumInfo = self.groupSummaryTableWidget
        
        
        # SIGNALS
        #Emit a signal when refresh button is pressed
        self.refreshBtn.clicked.connect(self.agentRefreshData)


    # SLOTS
    # Agent method, used for receiving a signal from UI elements
    def agentRefreshData(self):

        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile("settings.dat")
        databaseOperation1.getAllRowsFromTable(connectionArguments, "public.jaetut_lihat",)
        print(databaseOperation1.detailedMessage)
        # Read data from view jakoryhma_yhteenveto, no need to read connection args again
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(connectionArguments, "public.jakoryhma_yhteenveto",)
        print(databaseOperation2.detailedMessage)
        # Let's call the real method which updates the widget
        self.refreshData(databaseOperation1, self.meatShrInfo)
        self.refreshData(databaseOperation2, self.groupSumInfo)


    # This is a function that updates table widgets in UI,
    # because it does not receive signals; it's not a slot
    def refreshData(self, databaseOperation, widget):
        prepareData.prepareTable(databaseOperation, widget)


# APPLICATION CREATION AND STARTUP
# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = GroupMainWindow()
    appWindow.show()  # This can also be included in the FormWithTable class
    sys.exit(app.exec_())
