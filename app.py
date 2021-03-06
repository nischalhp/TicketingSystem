from flask import Flask,send_file,jsonify
from flask import request
from Formvalidation import Formvalidation
from Search import Search
from Data import Data
import json
app=Flask(__name__,instance_relative_config=True)


# directing to the page based on url
@app.route('/')
def index():
	return send_file('static/index.html')

@app.route('/search.html/')
def search():
	return send_file('static/search.html')


@app.route('/ticket/', methods=['POST']	)
def generate_ticket():
	response = {}
	try:
		vehicle_type = request.form['vehicle_type']
		toll_type = request.form['toll_type']
		timestamp = request.form['time']
		price = request.form['price']
		vehicle_no = request.form['vehicle_no']
	except KeyError as e:
		print e
		response['success'] = False
		response['data'] = []
		response['message'] = 'Required Parameters not sent'
		return_obj = jsonify(response)
		return_obj.status_code = 400
		return return_obj
	try:	
		formObject = Formvalidation()
		print vehicle_type,toll_type,timestamp,price,vehicle_no
		status = formObject.validate_data(vehicle_type,toll_type,timestamp,price,vehicle_no)
		if status == 'Success':
			response['success'] = True
			response['data'] = []
			response['message'] = 'Great Success'
			return_obj = jsonify(response)
			return return_obj
	except Exception as e:
			print e
			response['success'] = False 
			response['data'] = []
			response['message'] = str(e)
			return_obj = jsonify(response)
			return_obj.status_code = 500
			return return_obj

@app.route('/search/',methods=['GET'])
def search_ticket():
	response = {}
	vehicle_no = request.args.get('vehicle_no','')
	timestamp = request.args.get('time','')
	try:
		searchobj = Search()
		outlist = searchobj.validate_data(vehicle_no,timestamp)
		out_list = {}
		out_list['data'] = outlist
		return json.dumps(out_list)
	except Exception as e:
		response['success'] = False 
		response['data'] = []
		response['message'] = str(e)
		return_obj = jsonify(response)
		return_obj.status_code = 400 
		return return_obj

@app.route('/data/',methods=['GET'])
def get_data():
	response = {}
	try:
		dataobj = Data()
		outlist = dataobj.get_data()
		out_list = {}
		out_list['data'] = outlist
		return json.dumps(out_list)
	except Exception as e:
		response['success'] = False 
		response['data'] = []
		response['message'] = e 
		return_obj = jsonify(response)
		return_obj.status_code = 500
		return return_obj



if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)