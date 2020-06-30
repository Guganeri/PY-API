FROM python:3
COPY . /app 
RUN ls
RUN pip requirements.txt
WORKDIR /app
#ENV_FILE .env
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]