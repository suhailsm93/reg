from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details=request.form
        firstName=details['fname']
        uemail=details['email']
        tdate=details['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, uemail, tdate) VALUES (%s, %s, %s)", (firstName, uemail, tdate))
        mysql.connection.commit()
        cur.close()
    if request.method=="POST":
        return redirect(url_for('user'))
    return render_template('index.html')

@app.route('/user')
def user():
	cur=mysql.connection.cursor()
	cur.execute("select * from MyDB.MyUsers")
	rv=cur.fetchall()
	return render_template('table.html',data=rv)


if __name__ == '__main__':
    app.debug=true
    app.run()
