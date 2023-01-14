FROM python:3.11.1

WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD app /usr/local/app

EXPOSE 5000

CMD ["python", "main.py"]
