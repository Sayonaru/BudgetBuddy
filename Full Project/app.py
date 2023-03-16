from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
from mysql.connector import connect
import datetime
import re

app = Flask(__name__)
app.secret_key = 'GeeksForGeeks'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB']  = 'user-table'

conn = connect(
    host="localhost",
    user="root",
    password="",
    database="user-table"
)

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully!'
            return redirect(url_for('dashboard'))
            # return render_template('dashboard.html')
        else:
            message = 'Please enter correct email or password!'
    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not userName or not password or not email:
            message = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password,))
            mysql.connection.commit()
            message = 'You have successfully registered!'
    elif request.method == 'POST':
        message = 'Please fill you the form!'
    return render_template('register.html', message=message)

@app.route('/dashboard')
def dashboard():
    
    #Define plot data
    labels = [
        "Groceries",
		"Eating Out",
		"Entertainment",
		"Transport",
    	"Health",
    	"Shopping",
		"Bills",
		"Other",
    ]

    data = [3, 3, 6, 7, 2, 9, 4, 1]

    #return the components to the template
    return render_template(
        template_name_or_list='dashboard.html',
        data=data,
        labels=labels,
    )

@app.route('/lastid')
def lastid():
    lastid = get_last_id()
    return lastid

def get_last_id():
    cursor = conn.cursor()
    cursor.execute('SELECT transaction_id FROM transaction ORDER BY transaction_id DESC LIMIT 1')
    row = cursor.fetchone()
    if row is not None:
        lastid = row[0]
    else:
        lastid = 0

    cursor.close()
    return lastid

@app.route('/businessDashboard')
def businessDashboard():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transaction ORDER BY transaction_id ASC")
    results = cursor.fetchall()
    data = []
    for result in results:
        row = {'transaction_id': result[0], 'transaction_date': result[2], 'transaction_type': result[1],
               'transaction_amount': result[3], 'transaction_category': result[4], 'transaction_description': result[5]}
        data.append(row)

    cursor.close()

    return render_template('businessDashboard.html', data=data)

@app.route('/add-transaction', methods=['POST'])
def add_transaction():
    # x = datetime.datetime.now()
    transaction_type = request.form['type']
    transaction_amount = request.form['amount']
    transaction_category = request.form['category']
    transaction_description = request.form['description']

    if not all([transaction_type, transaction_amount, transaction_category, transaction_description]):
        flash('All fields are required.', 'error')
        return redirect(request.referrer)
    
    if not transaction_amount.isdigit():
        flash('Amount must be a number.', 'error')
        return redirect(request.referrer)
    
    # Convert transaction_amount to float
    transaction_amount = float(transaction_amount)

    if transaction_amount <= 0:
        flash('Amount must be greater than 0.00', 'error')
        return redirect(request.referrer)

    transaction_date = datetime.datetime.now()
    transaction_id = get_last_id() + 1
    mycursor = conn.cursor()
    sql = "INSERT INTO transaction (transaction_id, transaction_type, transaction_date, transaction_amount, transaction_category, transaction_description) VALUES (%s, %s, %s, %s, %s, %s)"

    val = (transaction_id, transaction_type, transaction_date, transaction_amount, transaction_category,
           transaction_description)
    mycursor.execute(sql, val)
    conn.commit()

    return redirect('/businessDashboard')

if __name__ == "__main__":
    app.run(debug=True)