FROM continuumio/anaconda3
#FROM python:3.8-slim-buster
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
MAINTAINER Wellington Guilherme da Luz Uczak <uczak@rede.ulbra.br>

# Dependencias
#ADD . /app
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 
COPY ./webApp /app
WORKDIR /app

ENTRYPOINT [ "python", "/app/main.py" ]
#ENTRYPOINT ["python", "/app/main.py"]
# Inicia a aplicação
#CMD ["python", "/app/main.py", "-p" ,"8000"]
#CMD ["python", "/app/main.py"]
