from flask import Flask ,url_for,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return 'hello world'
	#return '<script>alert ("ok")</script>'
	#return '<ul><li>Tom</li><li>Lily</li><li>Flask</li></ul>'
	#return url_for('static',filename='main.css')

@app.route('/static')
def get_static():
	return render_template('hello.html')


@app.route('/user/<userid>',methods=['POST','GET'])
def hello_user(userid):
	return 'hello %s' %userid



if __name__=='__main__':
	app.run(debug=True)