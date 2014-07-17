from PostgresConnector import PostgresConnector
import traceback
import psycopg2
class Formvalidation:


	def validate_data(self,vehicle_type,toll_type,date,price,vehicle_no):
		if vehicle_type.strip() == '' or toll_type.strip() == '' or price.strip() == '' or date.strip() == '' or vehicle_no.strip() =='':
			# figure out what to return here!
			raise Exception('input data has nulls')
		else:
			try:
				conn = PostgresConnector().get_connection()
				cursor = conn.cursor()
				query = """ INSERT INTO transactions
					(vehicle_type,toll_type,timestamp,price,vehicle_no
						) values(%s,%s,\'%s\',%s,\'%s\')
					""" % (vehicle_type,toll_type,date,float(price),vehicle_no) 
				#print "Inserting data to table using the query %s" % (query,)
				cursor.execute(query)
				conn.commit()
				return 'Success'
			except psycopg2.IntegrityError as e:
				raise Exception(' Unique key constraint failed ')
			except Exception:	
				raise Exception(' Something else went wrong')
