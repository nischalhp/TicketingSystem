from PostgresConnector import PostgresConnector
import traceback
class Search:

	def validate_data(self,vehicle_no,time):
		if vehicle_no.strip() == '' and time.strip() == '': 
			# figure out what to return here!
			raise Exception('input data has nulls')
		else:
			try:
				conn = PostgresConnector().get_connection()
				cursor = conn.cursor()
				query = ""
				if vehicle_no.strip() != '' and time.strip() != '':
					query = """ SELECT * FROM transactions where vehicle_no = \'%s\' 
						and timestamp = \'%s\'  order by timestamp """ % (vehicle_no,time)
				elif vehicle_no.strip() != '' :
					query = """ SELECT * FROM transactions where vehicle_no = \'%s\' 
						order by timestamp """ % (vehicle_no,)
				else:
					query = """ SELECT * FROM transactions where timestamp = \'%s\' 
						order by timestamp """ % (time,)

				print "selecting data from the table using the query %s" % (query,)
				cursor.execute(query)
				search_list = []
				for row in cursor:
					elements = {}
					elements['vehicle_type'] = row[0]
					elements['toll_type'] = row[1]
					elements['time'] = str(row[2])
					elements['price'] = row[3]
					elements['vehicle_no'] = row[5]
					search_list.append(elements)
				return search_list 
			except Exception:	
				print traceback.format_exc()
