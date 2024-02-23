FROM ubuntu

# Installations

RUN apt update
RUN apt install python3 python3-pip -yy
RUN pip install flask requests gunicorn

COPY templates /app/templates/
COPY app.py /app/

EXPOSE 8000

WORKDIR /app

# CMD ["python3", "app.py"]
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:8000","--threads=2","--workers=3","app:app"]
