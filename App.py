from flask import Flask,render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'prueba_py_mysql'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'prueba_mysql_python'


app.secret_key = 'mysecretkey'


mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html',contacts = data)
    

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email'] 
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s,%s,%s)',(fullname,phone,email))
        mysql.connection.commit()
        flash('Contactos agregado satisfactoriamente')
        return redirect(url_for('index'))



@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email'] 
        cur = mysql.connection.cursor()
        cur.execute('UPDATE contacts SET fullname = %s, email = %s , phone = %s WHERE id = %s',(fullname,phone,email,id))
        mysql.connection.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('index'))


@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = (%s)',(id))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])


@app.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = (%s)',(id))
    mysql.connection.commit()
    flash('Contacto borrado')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port = 3000, debug=True)