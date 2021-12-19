FROM python:3

RUN apt-get update -qq

RUN apt-get install -y python3-pip
RUN pip install pytest
RUN pip install anytree
RUN mkdir /DailyCodingChallenge
COPY . /DailyCodingChallenge

WORKDIR /DailyCodingChallenge

CMD [ "pytest", "*.py" && "/bin/bash" ]
