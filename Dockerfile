FROM python:3.7
COPY requirements /app/
WORKDIR /app
RUN pip install -r requirements
CMD ["gunicorn","-w","8","-b", "0.0.0.0:5000", "main:app"]