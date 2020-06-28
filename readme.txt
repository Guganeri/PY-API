-------- 
pip install requests
pip install requests_toolbelt
pip install http.client
pip install pymongo
pip install flask
pip install dnspython
pip install -U python-dotenv




client = pymongo.MongoClient("mongodb+srv://omnistack:omnistack@cluster0-jg1hn.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

sudo docker run -d --restart=unless-stopped -p 8080:8080 rancher/server --db-host 10.158.0.8 --db-port 3306 --db-user root --db-pass root --db-name cattle

GRANT ALL PRIVILEGES ON . TO 'root'@'192.168.100.%' 
  IDENTIFIED BY 'my-new-password' WITH GRANT OPTION;