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

def prepareComboBox(resultObject, comboBox, ixToShow, IxToReturn):
    """_summary_

    Args:
        resultObject (DatabaseOperation): Instance of DatabaseOperation class -> errors and result set.
        comboBox (QComboBox): Combo box to be updated
        ixToShow (int): Index of the column to show in the combo box
        IxToReturn (int): Index of the column containing values of interest

    Returns:
        list: Value of interest
    """
    # Result set is a list of tuples even when there is only one column in the view
    cBValuesOfInterest = [] # Empty list for values of interest
    cBItems = []  # Empty list for choices in the combo box

    for result in resultObject.resultset:
        cBValueOfInterest = result[IxToReturn] # Choose column to use as value of interest
        resultAsString = str(result[ixToShow]) # Convert element to show in the tuple as a string
        cBItems.append(resultAsString) # Append it to the choices list of the combo box
        cBValuesOfInterest.append(cBValueOfInterest) # Append the value to the list
    comboBox.addItems(cBItems) # Populate the combo box
    return cBValuesOfInterest
