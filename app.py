from flask import Flask,send_file
app=Flask(__name__,instance_relative_config=True)


# directing to the page based on url
@app.route('/')
def hello_world():
	return send_file('static/index.html')


if __name__=='__main__':
	app.run(host='0.0.0.0',debug=app.config["DEBUG"])