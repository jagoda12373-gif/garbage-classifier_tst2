FROM python:3.10-slim

WORKDIR /app

# kopiujemy wszystko do kontenera
COPY . /app

# instalacja pip i zależności
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Streamlit działa na porcie 8501
EXPOSE 8501

# uruchomienie aplikacji
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
