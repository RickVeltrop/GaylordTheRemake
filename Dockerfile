FROM python:3.10

WORKDIR /usr/app/src

COPY . .
RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
