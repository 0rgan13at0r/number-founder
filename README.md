<h1 align="center">Number Founder</h1>

[![LICENSE: MIT](https://img.shields.io/github/license/0rgan13at0r/number-founder)](LICENSE)
![Files Count](https://img.shields.io/github/directory-file-count/0rgan13at0r/number-founder)
![Code Size](https://img.shields.io/github/languages/code-size/0rgan13at0r/number-founder)
![Last Commit](https://img.shields.io/github/last-commit/0rgan13at0r/number-founder/main)
![Open Issues](https://img.shields.io/github/issues-raw/0rgan13at0r/number-founder)
![Closed Requests](https://img.shields.io/github/issues-pr-closed/0rgan13at0r/number-founder)
![All Stars](https://img.shields.io/github/stars/0rgan13at0r/number-founder?style=social)
![Watchers](https://img.shields.io/github/watchers/0rgan13at0r/number-founder?style=social)

## **Description**

Program is looking for numbers by your pattern in clipboard or text-files.

## **Install**

Install with pip
```python3
pip3 install -r requirements.txt
```

Install with poetry
```python3
poetry install
```

## **Demo**
```python3
# Looking for in clipboard
python3 main.py -p <YOUR NUMBER PATTERN> -c --output numbers.txt

# Looking for in text file
python3 main.py -p <YOUR NUMBER PATTERN> --text-file files.txt -o numbers.txt
```
