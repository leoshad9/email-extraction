# Email Extractor

This repository contains a Python script for extracting email addresses from a text file and writing the results to a new file.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Text File**: The script requires a text file named `text_file.txt` in the same directory as the script.

## Script Overview

### `email_extractor.py`

**Author**: Mohammad Shadman

**Description**: This script reads `text_file.txt`, extracts email addresses using a regular expression, and writes the results to `extracted_emails.txt`.

**Usage**:

```bash
python email_extractor.py
```

**Functionality**:

- **File Reading**: Opens and reads the contents of `text_file.txt`.
- **Email Extraction**: Uses a regular expression to identify and extract email addresses.
- **Output**: Writes the extracted email addresses to `extracted_emails.txt`. If no email addresses are found, it writes "No email addresses found in the file." If `text_file.txt` is missing, it prints an error message to the console.

**Example**:

```bash
python email_extractor.py
```

**Expected Output**:

- If email addresses are found:

```
Found 3 email addresses:
example1@example.com
user.name@domain.co
test.email+regex@sub.domain.net
```

- If no email addresses are found:

```
No email addresses found in the file.
```

- If `text_file.txt` is not found, the script prints:

```
The file 'text_file.txt' was not found. Please check the file path and try again.
```

- For other exceptions:

```
An error occurred: [Error details]
```

## Contributing

Feel free to fork the repository and submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
