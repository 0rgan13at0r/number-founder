FROM openstax/python3-base

LABEL version = "v0.1.0"
LABEL license="MIT"

WORKDIR /number-founder
VOLUME [ "/number-founder" ]

COPY . .
RUN apt update && apt upgrade -y && pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "src/main.py" ]
