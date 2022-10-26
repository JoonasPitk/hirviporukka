# TEST UPDATE OPERATION

# LIBRARIES AND MODULES
import psycopg2  # For PostgreSQL


# Properties of the connection string
database = "metsastys"
user = "postgres"
password = "Q2werty"
host = "localhost"
port = "5432"

# Try to establish a connection to DB server
try:
    # Create a connection object
    dbaseconnection = psycopg2.connect(database=database, user=user, password=password,
                                      host=host, port=port)
    
    # Create a cursor to execute commands and retrieve result set
    cursor = dbaseconnection.cursor()
    
    # Execute a SQL command to update a group
    command = "UPDATE public.jakoryhma SET ryhman_nimi = 'Ryhmä 4' WHERE ryhma_id = 4;"
    cursor.execute(command)

    # Commit the transaction
    dbaseconnection.commit()
    print("Tietue päivitettiin onnistuneesti")

# Throw an error if connection or cursor creation fails                                     
except(Exception, psycopg2.Error) as e:
    print("Tietokantayhteydessä tapahtui virhe", e)

# If successful close the cursor and the connection
finally:
    if (dbaseconnection):
        cursor.close()
        dbaseconnection.close()
        print("Yhteys tietokantaan katkaistiin")
