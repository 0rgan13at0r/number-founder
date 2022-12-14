<h1 align="center">Number Founder</h1>

[![LICENSE: MIT](https://img.shields.io/github/license/0rgan13at0r/number-founder)](LICENSE)
![Files Count](https://img.shields.io/github/directory-file-count/0rgan13at0r/number-founder)
![Code Size](https://img.shields.io/github/languages/code-size/0rgan13at0r/number-founder)
![Last Commit](https://img.shields.io/github/last-commit/0rgan13at0r/number-founder/main)
![Open Issues](https://img.shields.io/github/issues-raw/0rgan13at0r/number-founder)
![Closed Requests](https://img.shields.io/github/issues-pr-closed/0rgan13at0r/number-founder)
![All Start](https://img.shields.io/github/stars/0rgan13at0r/number-founder?style=social)
![Watchers](https://img.shields.io/github/watchers/0rgan13at0r/number-founder?style=social)

## **Description**
Program is searching Belarusian,Russian,Ukraine numbers in text-files, pdf-files, clipboard or on  sites.

## **Install**

Install with pip
```python3
pip3 install -r requirements.txt
```

Install with poetry
```python3
poetry install
```

## **Docker**

```
# Create image
sudo docker build -t number-founder .

# Start container
sudo docker run number-founder -p BY -c # Searching in clipboard

sudo docker run -v $(pwd):/number-founder number-founder -p BY --pdf FILE.pdf # Searching in pdf or text-file
```

## **Demo**
```python3
# Searching in clipboard
python3 main.py -p <BY,UA,RU> -c --output numbers.txt

# Searching in text file
python3 main.py -p <BY,UA,RU> -ft files.txt -o numbers.txt

# Searching in pdf file
python3 main.py -p <BY,UA,RU> --pdf file.pdf
```
