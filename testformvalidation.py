from Formvalidation import Formvalidation

obj = Formvalidation()
# try:
# 	obj.validate_data('','','','')

# except Exception as e:
# 	print e

try:
	obj.validate_data('1','1','2014-07-17','55.0','KA01-HV7382')
except Exception as e:
	print e