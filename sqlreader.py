##################################################
# Mike Solie                                     #
# Extracting table from db file                  #
#                                                #
# Description:                                   #
# Opens a SQL db file and executes SQL commands  #
# to perform queries. Below pulls information    #
# from 3 columns and outputs in to the terminal  #
# in a way that is easy to understand.           #
##################################################


#####
# import os to use the operating system for the filepath
# import sqlite3 to work with the sql database
# import datetime to translate the last time visited column
#####
import os
import sqlite3
import datetime


#####
# function: get_path
# purpose: to get the file path to the database file
# inputs: filename
# returns: full path to database file
#####
def get_path(filename):
    # path to current directory for this program
    DIR_NAME = os.path.dirname(__file__)

    # variable to the full path of the file (assuming it is in the same directory as the program
    db_path = os.path.join(DIR_NAME, filename)
    # print(db_path) debug print statement
    # returns the full path to the file
    return db_path


#####
# function: open_db
# purpose: to connect to and open the database
# inputs: SQL command
# returns: database location
#####
def open_db(db_path):
    # connection variable - connects to the db at the end of the db_path
    sqlConn = sqlite3.connect(db_path)

    # connection try/except block
    try:
        # tries to connect to the path stored in the variable
        sqlConn

    # error exception when the database cannot be opened/connected
    except sqlConn.DatabaseError:
        print(f'Unable to open database')
        exit(0)

    # print(f'DB opened successfully') debug print statement
    # database location -> command execution variable. Selects everything from the urls table
    dbLoc = sqlConn.execute('SELECT * FROM urls')

    # returns the location the command points to
    return dbLoc


#####
# function: read_table
# purpose: to read the input from the open_db function
# inputs: database location
# returns: the specified rows from the table
#####
def read_table(dbLoc):
    # empty list for input
    table = []

    # try/except statement for gathering data from the query
    try:

        # for loop that loops through the rows in the dbLoc
        for row in dbLoc:
            # variable that translates the "last visited" time from microseconds to a humanreadable form
            last_visited = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[5])
            # stores the data collected from the different rows into a dictionary to make it easier to organize later
            table_dict = {'url' : row[1], 'visits' : row[3], 'last time visited' : last_visited}
            # appends the dictionary to the empty table list
            table.append(table_dict)

    # exception for any errors that are thrown
    except Exception as e:
        # exception print statement for debugging
        print(f'Error: {e}')

    # returns the appended table
    return table


#####
# function: terminal output
# purpose: to organize the database information and provide output that is readable at a glance
# inputs: the specified information from the table
# returns: nothing, prints to terminal
#####
def terminal_output(table):

    # column width variables for organized output
    url_width = 50
    visits_width = 20
    last_visited_width = 28

    # print statement that puts the headers inbetween two lines and uses the width variables to determine where the headers are placed
    print(f'+------------------------------------------------------------------------------------------------------+\n|{"                       URL":<{url_width}} |{"  Number of Visits":<{visits_width}}| {"     Last Time Visited":<{last_visited_width}}|')

    # for loop pulls the dictionary out of the list and pulls url, visits, and last visited values
    for t in table:
        # variable that stores pulls the websites from the URL column and if they are longer then the defined width are cut off
        website = t['url'][:url_width]

        # if statement that left justifies the output if the url length is less than the url width
        if len(website) < url_width:
            website = website.ljust(url_width)

        # number of visits variable that pulls visits values, converts them to strings and justifies them to the center of the defined width
        num_visits = str(t['visits']).center(visits_width)

        # last visited variable that pulls last time visited values, converts them to strings and justifies them to the center of the defined width
        last_visited = str(t['last time visited']).ljust(last_visited_width)
        print(f'+------------------------------------------------------------------------------------------------------+')
        # print statement for each variable
        print(f'|{website} |{num_visits}| {last_visited}|')

    # end of output print statement
    print(f'+------------------------------------------------------------------------------------------------------+')


#####
# function: main
# purpose: to run the program
# inputs: db file
# returns: nothing, runs the program
#####
def main():
    # variable for the db file
    paths = get_path('CHANGETHIS.db')
    # variable that opens the db file and executes commands
    opens = open_db(paths)
    # variable that reads the table
    tables = read_table(opens)
    # variable that organizes information and prints it to the terminal
    terminal_output(tables)
    # closes the sql connection
    opens.close()


# call to start the program
##---->
main()
##<----
# program end
