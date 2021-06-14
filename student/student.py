from flask import *
from DBM import insertData,selectAllStd,deleteData,selectStdById,updateData,logIn

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/reg')
def reg():
    return render_template('register.html')

@app.route('/addStd',methods=['POST'])
def add_Emp():
    id=request.form['id']
    name=request.form['name']
    schoolname=request.form['schoolname']
    address=request.form['address']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']
    t=(id,name,schoolname,address,email,phone,password)
    insertData(t)
    return render_template('home.html')

@app.route('/slist')
def std_list():
    sl=selectAllStd()
    return render_template('stdlist.html',stdlist=sl)

@app.route('/onlylist')
def only_list():
    sl=selectAllStd()
    return render_template('onlylist.html',stdlist=sl)

@app.route('/deleteStd')
def delete_std():
    id=request.args.get('id')
    deleteData(id)
    return redirect('/slist')

@app.route('/editStd')
def edit_std():
    id=request.args.get('id')
    std=selectStdById(id)
    return render_template('updateStd.html',s=std)

@app.route('/updateStd',methods=['POST'])
def update_Std():
    id=request.form['id']
    name=request.form['name']
    schoolname=request.form['schoolname']
    address=request.form['address']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']
    t=(name,schoolname,address,email,phone,password,id)
    updateData(t)
    return redirect('/slist')

@app.route('/login')
def login_std():
    return render_template('login.html')

@app.route('/loginStd',methods=['POST'])
def log_in_std():
    email=request.form['email']
    password=request.form['password']
    ln=logIn(email,password)
    if len(ln)>0:
        return redirect('/slist')  
    else:
        return render_template('login.html')
    
if __name__=='__main__':
    app.run(debug=True)
