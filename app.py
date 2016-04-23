from flask import Flask
from flask import Flask, render_template
from flask.globals import request
from flask import Markup

#########################Database Setup####################################
import MySQLdb
from flask.helpers import flash

# Open database connection
db = MySQLdb.connect("localhost","root","123","fleet_schedule")

# prepare a cursor object using cursor() method
cursor = db.cursor()



def check_user(email_id, password):
    insertQuery = "SELECT * FROM user_data"
    cursor.execute(insertQuery)
    a = cursor.fetchall()
    for i in range(len(a)):
        if (a[i][0] == email_id and a[i][1] == password):
            return (1, a[i][2])
    
    return (0, a[i][2])
    db.commit()
    

##################################################################


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods = ['POST'])
def login_index():
    email_id = request.form['email']
    password = request.form['password']
    login_out = check_user(email_id, password)

    if login_out[0] == 1 and login_out[1] == "P":
          return render_template('passenger.html')
    
    elif login_out[0] == 1 and login_out[1] == "D":
          return render_template('driver_dashboard.html')
    
    elif login_out[0] == 1 and login_out[1] == "A":
          return render_template('admin_dashboard.html')
    
    return render_template('index.html', message=True)
    
if __name__ == "__main__":
    app.run(port='8888')
    
