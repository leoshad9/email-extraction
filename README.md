# Email Extractor

This repository contains a Python script designed to extract email addresses from a file.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Input File**: The script requires the input file to be in text format (`.txt`) and named as `text_file`. Ensure this file is in the same directory as the script.

## Script Overview

### `email_extractor.py`

**Author**: Mohammad Shadman

**Description**: This script reads from a text file named `text_file.txt`, located in the same directory as the script. It uses a regular expression to extract all email addresses found in the file and writes these email addresses to a new text file named `extracted_emails.txt`.

**Usage**:

To run the script, use the following command in your terminal:

```bash
python email_extractor.py
```

**Functionality**:

1. **File Reading**: Opens and reads the contents of `text_file.txt`.
2. **Email Extraction**: Uses a regular expression to identify and extract email addresses from the text.
3. **Output**:
   - If email addresses are found, the script displays "Found X email addresses. Emails are saved to `extracted_emails.txt`."
   - If no email addresses are found, it displays "No email addresses found."
   - If `text_file.txt` is missing, an error message is displayed in the console.

**Example**:

```bash
python email_extractor.py
```

**Expected Output**:

- If email addresses are found:

  ```
  Found 3 email addresses. Emails are saved to 'extracted_emails.txt'.
  ```

- If no email addresses are found:

  ```
  No email addresses found.
  ```

- If `text_file.txt` is not found:

  ```
  The file 'text_file.txt' was not found. Please check the file path and try again.
  ```

- For other exceptions:

  ```
  An error occurred: [Error details]
  ```

## Contributing

If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
