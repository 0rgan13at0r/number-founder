FROM openstax/python3-base

LABEL version = "v0.1.0"
LABEL license="MIT"

WORKDIR /number-founder
VOLUME [ "/number-founder" ]

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "src/main.py" ]
