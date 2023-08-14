# DataTrash.py
# File used to delete the database used by the project after all algorithms have been run

def trash():
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

    # Delete database
    try:
        mycursor.execute("DROP DATABASE IF EXISTS comparing_trading_algorithms_db")
    except:
        print("Error deleting database")

    # Display All Databases user has access to    
    #mycursor.execute("SHOW DATABASES")
    #for x in mycursor:
    #    print(x)
    
    return


# Entry point for DataTrash.py
# Calls helper function trash() to delete the database at the after the project is run
if __name__ == '__main__':
    trash()