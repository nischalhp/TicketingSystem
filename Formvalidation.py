from PostgresConnector import PostgresConnector
class Formvalidation:


	def validate_data(self,vehicle_type,toll_type,price,date):
		if vehicle_type == '' or toll_type = '' or price == '' or date == '':
			return error
		else:
			