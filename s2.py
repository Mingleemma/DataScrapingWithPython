# Import the required packages
from bs4 import BeautifulSoup
import csv
import requests

# Open an HTML file for reading
HTMLFileToBeOpened = open("index.html", "r")

# Create a CSV writer and write the header row
f = csv.writer(open('adscdata.csv', 'w'))
f.writerow(['Name', 'Session', 'Gender'])

# Read the contents of the HTML file and store it in a variable
contents = HTMLFileToBeOpened.read()

# Create a BeautifulSoup object and specify the parser
beautifulSoupText = BeautifulSoup(contents, 'html.parser')

# Find all <tr> elements in the HTML, excluding the first and last row
table = beautifulSoupText.find_all('tr')
table = table[1:-1]

# Iterate through each row in the table
for row in table:
    # Find all <td> elements within the current row
    td_elements = row.find_all('td')
    
    # Extract and store the text from each <td> element in variables
    value1 = td_elements[0].get_text()
    value2 = td_elements[1].get_text()
    value3 = td_elements[2].get_text()
    
    # Write the values to the CSV file
    f.writerow([str(value1), str(value2), str(value3)])