# Import the required packages
from bs4 import BeautifulSoup
import requests
import csv

# Specify the URL of the web page to scrape
url = 'https://en.wikipedia.org/wiki/Mobile_Web_Ghana'

# Send an HTTP GET request to the URL and get the web page's content
page = requests.get(url)

# Parse the HTML content of the web page using BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find the HTML table element within the web page
table = soup.table.tbody.contents[1:]

# Create a CSV writer and write the header row
f = csv.writer(open('mwgdata.csv', 'w'))
f.writerow(['Name', 'Link'])

# Iterate through the rows in the table
for row in table:
    # Extract the content of the table cell in the "th" element
    heading = row.th.string
    
    # Extract the content of the table cell in the "td" element
    value = row.td.string
    
    # Print the extracted values
    print(str(heading) + " - " + str(value))
    
    # Add each artist's name and associated link to a row in the CSV file
    f.writerow([str(heading), str(value)])