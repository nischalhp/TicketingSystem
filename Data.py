from PostgresConnector import PostgresConnector
import traceback
import psycopg2
class Data:


	def get_data(self):
		out_list = []
		try:
			conn = PostgresConnector().get_connection()
			cursor = conn.cursor()
			query = """ SELECT vehicle_type,vehicle_type_id,
						toll_type,toll_type_id,price
						from master_data"""
			cursor.execute(query)
			resultset = cursor.fetchall()
			out_list = [] 
			vehicle_dict = {}
			for row in resultset:
				row_data = {}
				row_value_dict = {}
				id = row[1]
				vehicle_name = row[0]
				journey_list = []
				if id not in vehicle_dict.keys():
					vehicle_dict_out = {}
					vehicle_dict[id] = 1
					for row_in in resultset:
						journey_type = {}
						if row_in[1] == id:
							journey_type['toll_type'] = row_in[2]
							journey_type['toll_id'] = str(row_in[3])
							journey_type['price'] = str(row_in[4])
							journey_list.append(journey_type)	
					vehicle_dict_out['vehicle_type'] = vehicle_name
					vehicle_dict_out['vehicle_type_id'] = id
					vehicle_dict_out['journey'] = journey_list
					out_list.append(vehicle_dict_out)

			return out_list 
		except Exception as e:	
			print e

			raise Exception(' Something went wrong while retrieving data')
