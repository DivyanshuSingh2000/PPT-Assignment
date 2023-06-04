FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]


#docker build -t genre-prediction .

#docker run -p 5000:5000 genre-prediction
