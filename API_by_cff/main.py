from flask import Flask,request,render_template,url_for
import pymysql

app=Flask(__name__)


def connect_mysql(): 
	db=pymysql.connect('localhost','root','root','api_test')
	return db

def operate_sql(sql):
	print(sql)
	db=connect_mysql()
	print('connect mysql successfull')
	cursor=db.cursor()
	try:
		cursor.execute(sql)
		db.commit()
		print('insert successfull')
	except:
		db.rollback()
		print('insert failed')
		db.close()

def find_one(sql):
	print(sql)
	db=connect_mysql()
	cursor=db.cursor()
	try:
		cursor.execute(sql)
		result=cursor.fetchone()
		print('find success')
		return result
	except:
		print('find failed')
		db.close()

def find_all(sql):
	print(sql)
	db=connect_mysql()
	cursor=db.cursor()
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		print('find success')
		return results
	except:
		print('find failed')
		db.close()




@app.route('/')
def index():
	return "hello,welcome to test my API"

@app.route('/<username>')
def hello_user(username):
	if username:
		print(request.url)
		sql='select * from user where name='+username+';'
		result=find_one(sql)
		return result
	else:
		return "400,username can't be none"

@app.route('/login?',methods=['GET','POST'])
def login():
	if request.method=='POST':
		username=request.json.get('username')
		password=request.json.get('password')
		if username:
			sql='select password from login where username='+username+';'
			result=find_one(sql)
			print(result)
			if result != password:
				return "error!password error"
			else:
				return 'login success'
		return 'username can\'t be none'
	else:
		return 'method error'



if __name__=='__main__':
	app.run(debug=True)