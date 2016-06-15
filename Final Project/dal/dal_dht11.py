import pymongo
from pymongo import MongoClient
import time

_client = MongoClient()
_database = _client.weather_station
_dht11_table = _database.dht11

class dht11Dal:
	def add(self, var_temp, var_humidity):
		curr_date = time.strftime("%d-%m-%Y")
		curr_time = time.strftime("%H:%M:%S")
		curr_id = _dht11_table.count() + 1

		new_data = { "_id": curr_id,
			     "temperature": var_temp,
			     "humidity" : var_humidity,
			     "date": curr_date,
			     "time": curr_time			
				}
		new_id = _dht11_table.insert_one(new_data).inserted_id
		if not new_id:
			return false
		else:
			return new_id
	
	def read_All(self):
		result = _dht11_table.find()
		return result

	def read_By_Date(self, var_req_date):
		result = _dht11_table.find({"date": var_req_date})
		return result

