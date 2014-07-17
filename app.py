from flask import Flask,send_file,jsonify
from flask import request
from Formvalidation import Formvalidation
from Search import Search
app=Flask(__name__,instance_relative_config=True)


# directing to the page based on url
@app.route('/')
def hello_world():
	return send_file('static/index.html')

@app.route('/ticket/', methods=['POST']	)
def generate_ticket():
	response = {}
	try:
		vehicle_type = request.form['vehicle_type']
		toll_type = request.form['toll_type']
		price = request.form['price']
		timestamp = request.form['time']
		vehicle_no = request.form['vehicle_no']
	except KeyError as e:
		response['success'] = False
		response['data'] = []
		response['message'] = 'Required Parameters not sent'
		return_obj = jsonify(response)
		return_obj.status_code = 400
		return return_obj
	try:	
		formObject = Formvalidation()
		status = formObject.validate_data(vehicle_type,toll_type,timestamp,price,vehicle_no)
		if status == 'Success':
			response['success'] = True
			response['data'] = []
			response['message'] = 'Great Success'
			return_obj = jsonify(response)
			return return_obj
	except Exception as e:
			response['success'] = False 
			response['data'] = []
			response['message'] = str(e)
			return_obj = jsonify(response)
			return_obj.status_code = 500
			return return_obj

@app.route('/search/',methods=['GET'])
def search_ticket():
	vehicle_no = request.args.get('vehicle_no','')
	timestamp = request.args.get('time','')
	try:
		searchobj = Search()
		outlist = searchobj.validate_data(vehicle_no,timestamp)
		print outlist
		return jsonify(outlist)
	except Exception as e:
		response['success'] = False 
		response['data'] = []
		response['message'] = e 
		return_obj = jsonify(response)
		return_obj.status_code = 500
		return return_obj

@app.route('/data/',methods=['GET'])

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)