FROM python:3
WORKDIR /usr/src/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
#ENV_FILE .env