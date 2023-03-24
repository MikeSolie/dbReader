# db File Viewer
This Python script reads the Google Chrome browsing history and displays it in a readable format in the terminal.

## Prerequisites
Python 3.x
SQLite3

## Usage
Clone the repository or download the script.
Open the terminal and navigate to the directory containing the script.
Run the command python `sqlreader.py`.
The script will output a list of visited URLs with the number of visits and the last time each URL was visited.

## How it works
The script uses SQLite3 to connect to the Google Chrome browsing history database file (History.db) and execute a query to retrieve the URLs, number of visits, and last visit time. It then formats and outputs the information in a readable format in the terminal.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
