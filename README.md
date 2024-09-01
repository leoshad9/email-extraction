## Email Extractor

This Python script extracts email addresses from a text file using regular expressions. It's a simple tool designed to help you quickly find and list all email addresses present in a file.

### Author

MOHD SHADMAN

### Overview

The **Email Extractor** script reads the contents of a text file (`text_file.txt`) and uses a regular expression to find and extract all email addresses. The extracted email addresses are then printed to the console, one per line.

### Features

- Extracts email addresses from a text file.
- Uses a regular expression to identify standard email formats.
- Handles file not found errors gracefully.

### Requirements

- **Python 3.x**: Ensure you have Python installed on your system.
- A text file named `text_file.txt` in the same directory as the script.

### Usage

1. **Clone the repository** or download the script directly.

2. **Prepare the text file**:
   - Create a text file named `text_file.txt`.
   - Place the file in the same directory as the script.
   - Add some text containing email addresses to the file.

3. **Run the script**:
   ```bash
   python email_extractor.py
   ```

### Example Output

When you run the script, it will display the number of email addresses found and list each email address on a new line:

```bash
Found 3 email addresses:
example1@example.com
user.name@domain.co
test.email+regex@sub.domain.net
```

### Error Handling

If the script cannot find the `text_file.txt` file, it will output an error message:

```bash
The file 'text_file.txt' was not found. Please check the file path and try again.
```

If any other error occurs, it will display a generic error message with details about the exception.

### License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.
