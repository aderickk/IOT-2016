import pymongo
from pymongo import MongoClient
import time

_client = MongoClient()
_database = _client.weather_station
_tsl_table = _database.tslTable

class tslDal:
	def add(self, var_ir_luminosity, var_full_luminosity, var_lux):
		curr_date = time.strftime("%d-%m-%Y")
		curr_time = time.strftime("%H:%M:%S")
		curr_id = _tsl_table.count() + 1

		new_data = { "_id": curr_id,
			     "ir_luminosity": var_ir_luminosity,
			     "full_luminosity" : var_full_luminosity,
			     "lux" : var_lux,
			     "date": curr_date,
			     "time": curr_time			
				}
		new_id = _tsl_table.insert_one(new_data).inserted_id
		if not new_id:
			return false
		else:
			return new_id
	
	def read_All(self):
		result = _tsl_table.find()
		return result

	def read_By_Date(self, var_req_date):
		result = _tsl_table.find({"date": var_req_date})
		return result

