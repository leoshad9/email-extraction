# Author: MOHAMMAD SHADMAN

import re  # Import the regular expression module to work with regex in Python

def extract_emails(input_file_path, output_file_path):
    """Extracts email addresses from a text file and writes them to a new file if any are found.

    Args:
        input_file_path (str): Path to the input text file.
        output_file_path (str): Path to the output text file.

    Returns:
        None
    """
    # Define a regular expression pattern for matching email addresses
    # This pattern matches standard email formats
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    try:
        # Read the contents of the input file
        with open(input_file_path, 'r') as file:
            file_contents = file.read()

        # Extract email addresses using the regex pattern
        email_addresses = re.findall(email_regex, file_contents)

        if email_addresses:
            # Write extracted email addresses to the output file
            with open(output_file_path, 'w') as file:
                file.write(f"Found {len(email_addresses)} email addresses:\n")
                for email in email_addresses:
                    file.write(f"{email}\n")
            
            # Inform the user that emails have been saved
            print(f"Found {len(email_addresses)} email addresses. Emails are saved to '{output_file_path}'.")
        else:
            # Inform the user if no email addresses are found
            print("No email addresses found.")

    except FileNotFoundError:
        # Handle case where the input file does not exist
        print(f"The file '{input_file_path}' was not found. Please check the file path and try again.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define default file paths
    input_file = 'text_file.txt'
    output_file = 'extracted_emails.txt'

    # Call the function to extract emails and handle file operations
    extract_emails(input_file, output_file)
