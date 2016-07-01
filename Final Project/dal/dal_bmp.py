import pymongo
from pymongo import MongoClient
import time

_client = MongoClient()
_database = _client.weather_station
_bmp_table = _database.bmpTable

class bmpDal:
	def add(self, var_temp, var_pressure, var_sea_pressure, var_altitude):
		curr_date = time.strftime("%d-%m-%Y")
		curr_time = time.strftime("%H:%M:%S")
		curr_id = _bmp_table.count() + 1

		new_data = { "_id": curr_id,
			     "temperature": var_temp,
			     "pressure" : var_pressure,
			     "sea_level_pressure": var_sea_pressure,
			     "altitude" : var_altitude, 
			     "date": curr_date,
			     "time": curr_time			
				}
		new_id = _bmp_table.insert_one(new_data).inserted_id
		if not new_id:
			return false
		else:
			return new_id
	
	def read_All(self):
		result = _bmp_table.find()
		return result

	def read_By_Date(self, var_req_date):
		result = _bmp_table.find({"date": var_req_date})
		return result


