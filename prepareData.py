# MODULE FOR PREPARING DATA TO DISPLAY IT ON THE WIDGETS
# ======================================================

# LIBRARIES AND MODULES
from PyQt5.QtWidgets import QTableWidgetItem # For preparing cell data


'''
# Temporary object to bring object properties
resultObject = pgModule.DatabaseOperation()
testConnectionArgs = resultObject.readDatabaseSettingsFromFile("settings.dat")
resultObject.getAllRowsFromTable(testConnectionArgs, "public.jakoryhma_yhteenveto")

testTableWidget = QTableWidget()
'''

# DATA PREPARATION FUNCTIONS
def prepareTable(resultObject, tableWidget):
    """Updates an existing TableWidget using an instance of DatabaseOperation
       class defined in the pgModule.

    Args:
        resultObject (DatabaseOperation): Instance of DatabaseOperation class -> errors and result set.
        tableWidget (QTableWidget): Instance of QTableWidget to be updated from the result set.
    """
    
    # If there is no error start processing rows and columns of the result set
    if resultObject.errorCode == 0:
        tableWidget.setRowCount(resultObject.rows)
        tableWidget.setColumnCount(resultObject.columns)
        tableWidget.setHorizontalHeaderLabels(resultObject.columnHeaders)

        rowIndex = 0 # Initialise the row index
        
        for tupleIndex in resultObject.resultSet: # Cycle through a list of tuples
            columnIndex = 0 # Initialise the column index

            for cell in tupleIndex: # Cycle through values in the tuple
                cellData = QTableWidgetItem(str(cell)) # Format cell data into a string object
                tableWidget.setItem(rowIndex, columnIndex, cellData) # Set cell
                columnIndex += 1
            
            rowIndex += 1
