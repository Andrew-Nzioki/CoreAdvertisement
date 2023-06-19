FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

co

EXPOSE 8000

# ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "advertiesement.wsgi"]
