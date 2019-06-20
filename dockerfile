FROM python:3.7.3

WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

#RUN django-admin startproject testpro 

#RUN pip install httpserver
# RUN python testpro/manage.py runserver

COPY . /usr/src/app

CMD exec gunicorn antinationalist.wsgi:application --bind 0.0.0.0:8000 --workers 3

# CMD ["python", "-m", "http.server", "8000"]

# CMD ["python","testpro/manage.py","runserver"]
