FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]


# docker build -t research-paper-titles .
# docker run -p 5000:5000 research-paper-titles
