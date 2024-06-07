# Author: MOHD SHADMAN

# Defining a regular expression for matching email addresses
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Open the text file for reading
with open('text_file.txt', 'r') as f:
    # Read the entire file contents into a string
    file_contents = f.read()

    # Use the findall method of the re module to extract all email addresses
    email_addresses = re.findall(email_regex, file_contents)

    # Print the extracted email addresses
    print(email_addresses)
