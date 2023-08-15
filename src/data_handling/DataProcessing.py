# DataProcessing.py
# File used to read in CSV files of all stock and etf data and place into a MySQL database


def clean():
    # Import mysql.connector
    try:
        import mysql.connector
    except:
        print("Error with importing mysql.connector")
        return

    # Connecting to mysql server
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "Comparing_Trading_Algorithms",
            password = "password"
        )
    except:
        print("Error with connecting to MySQL server")
        return

    # Set cursor for user
    mycursor = mydb.cursor()

    # Create necessary database if not already created
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS comparing_trading_algorithms_db")
    except:
        print("Error creating database")
        return

    # Select database to connect to
    try:
        mycursor.execute("USE comparing_trading_algorithms_db")
    except:
        print("Error selecting database")
    
    print("Current:")
    # Display current 
    mycursor.execute("SELECT DATABASE()")
    for x in mycursor:
        print(x)

    print("All:")
    # Display all databases the user has access to
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

    mydb.close()
    return


# Entry point for DataProcesssing.py
# Calls helper function clean() to clean data and place in database
if __name__ == '__main__':
    clean()