# Author: MOHAMMAD SHADMAN

import re  # Import the regular expression module to work with regex in Python

# Define a regular expression pattern for matching email addresses
# This pattern matches standard email formats with the following structure:
# - Begins with word characters (letters, digits, underscores), dots, percent signs, plus signs, or hyphens
# - Followed by an '@' symbol
# - Followed by more word characters or dots (domain name)
# - Ends with a dot and a domain suffix of at least two letters (e.g., .com, .org, .net)
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Try to open the text file for reading
try:
    # 'with' statement ensures the file is properly closed after its suite finishes, even if an error occurs
    with open('text_file.txt', 'r') as f:
        # Read the entire contents of the file into a string variable
        file_contents = f.read()

        # Use the 'findall' method from the 're' module to extract all email addresses
        # that match the defined pattern within the file contents
        email_addresses = re.findall(email_regex, file_contents)

        # Define the output file path
        output_file_path = 'extracted_emails.txt'

        # Open the output file for writing
        with open(output_file_path, 'w') as out_file:
            # Check if any email addresses were found
            if email_addresses:
                out_file.write(f"Found {len(email_addresses)} email addresses:\n")
                # Write each extracted email address to the file on a new line
                for email in email_addresses:
                    out_file.write(f"{email}\n")
            else:
                # Inform the user in the output file if no email addresses were found
                out_file.write("No email addresses found in the file.")

# Handle the case where the file is not found and provide user guidance
except FileNotFoundError:
    print("The file 'text_file.txt' was not found. Please check the file path and try again.")

# Catch any other exceptions and print the error message to help with debugging
except Exception as e:
    print(f"An error occurred: {e}")
