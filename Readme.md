# Phishing URL Awareness Checker

## Project Description

The Phishing URL Awareness Checker is a Python command-line application that checks URL text for common warning signs associated with phishing links.

It is designed to improve cybersecurity awareness and help users identify suspicious URL patterns.

**Note:** This program only checks URL text. It does not open websites or guarantee that a URL is safe.

## Features

The program checks six warning signs:

1. Presence of an `@` symbol.
2. URL length greater than 100 characters.
3. Use of an IP address as the hostname.
4. Five or more hostname segments.
5. Presence of a punycode marker (`xn--`).
6. Use of HTTP instead of HTTPS.

## Bonus Improvements

- Repeat input loop to check multiple URLs.
- Quit option to exit the program.
- Warning summary to help users review results.
- Error handling for malformed URL formats.
- Empty input handling.

## Technologies Used

- Python 3.10+
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)
- Visual Studio Code

## Project Structure

```text
phishing-url-awareness/
│
├── phishing_checker.py
├── README.md
├── requirements.txt
│
├── tests/
│   └── test_samples.md
│
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## How to Run

1. Install Python 3.10 or later.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python phishing_checker.py
```

5. Enter a sample URL when prompted.
6. Type `quit` to exit.

## Testing

The application was tested using five sample URLs provided in the project workbook.

Additional tests were performed for the repeat-input loop, quit option, warning summary, and error handling.

See `tests/test_samples.md` for the test results.

## Limitations

- Checks only visible URL text.
- Does not access the internet.
- Does not verify website ownership or reputation.
- Cannot guarantee that a URL is safe.
- HTTPS alone does not mean a website is trustworthy.

## Safety and Ethics

- Do not enter passwords or personal information.
- Do not open suspicious links for testing.
- Use only sample URL strings.
- This project is intended for cybersecurity awareness and education.

## Future Improvements

- Add more URL pattern checks.
- Improve the user interface.
- Add more test cases.
