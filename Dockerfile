FROM python:3.9

# Create app directory
WORKDIR /usr/src/app

EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]