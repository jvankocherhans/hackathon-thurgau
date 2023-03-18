FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask

ENTRYPOINT [ "python" ]

CMD ["routes.py"]
