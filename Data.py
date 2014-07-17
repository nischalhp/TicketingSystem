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
			for row in cursor:
				row_data = {}
				row_data['vehicle_type'] = row[0]
				row_data['vehicle_type_id'] = row[1]
				row_data['toll_type'] = row[2]
				row_data['toll_type_id'] = row[3]
				row_data['price'] = row[4]
				out_list.append(row_data)
		
			return out_list
		except Exception:	
			raise Exception(' Something went wrong while retrieving data')
