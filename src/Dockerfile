FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python app.py"]
EXPOSE 5000
#ENTRYPOINT ["python3"]
#ENV_FILE .env