from flask import Flask,send_file
from flask import request
app=Flask(__name__,instance_relative_config=True)


# directing to the page based on url
@app.route('/')
def hello_world():
	return send_file('static/index.html')

@app.route('/ticket', methods=['POST'])
def generate_ticket():
	vehicle_type = request.form['vehicle_type']
	toll_type = request.form['toll_type']
	price = request.form['price']
	timestamp = request.form['time']
	



if __name__=='__main__':
	app.run(host='0.0.0.0',debug=app.config["DEBUG"])