### HOW TO RUN ###

1. Set MongoDB
	python
		python test_database.py (in /dal)
	mongo 
		show dbs (show "weather_station" is imported)
		use weather_station
		db.addUser('admin','password')
2. sudo mongod
3. python run.py

Now the service will be open on "127.0.0.1/5000" by default.

### MONGODB INFO ###

username = 'admin'
password = 'password'
dbname = 'weather_station'



