from Data import Data 

obj = Data()

try:
	out = obj.get_data()
	print out
except Exception as e:
	print e