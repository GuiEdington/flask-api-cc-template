FROM python:3

RUN apt-get update
RUN apt-get install -y unixodbc unixodbc-dev
RUN apt-get install -y apt-transport-https ca-certificates 
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install msodbcsql17


RUN python3 -m pip install Flask
RUN python3 -m pip install requests
RUN python3 -m pip install pyodbc
RUN python3 -m pip install tablib

COPY ./app/ /opt/app
WORKDIR /opt/app
EXPOSE 5000
ENTRYPOINT [ "python3", "-u", "main.py"]