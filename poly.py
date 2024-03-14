
from flask import Flask, render_template ,  url_for, request,session
#from flask_sqlalchemy import SQLAlchemy
from operator import itemgetter
from function import *

from flask import Flask, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename









poly=Flask(__name__)
poly.config['SQLAlCHEMY_DATABASE_URL']='sqlite:///test.db'



@poly.route("/")
def home():
    return render_template('index.html')



@poly.route("/poly.html")
def ab():
    return render_template('/poly.html')
@poly.route("/pro1.html")
def abb():
    return render_template('/pro1.html')



@poly.route("/metfun.html")
def abb1():
    return render_template('/metfun.html')





    
@poly.route("/runmeta",methods=['GET'])
def fff2():
    filname = request.args.get('v')
    t=impo(filname)
    data,val_obj_fu=met_fun1(t)
    return render_template("resultat2.html",data=data,val_fct_obj=val_obj_fu)



@poly.route("/dynpro.html")
def ab2():
    return render_template('/dynpro.html')



@poly.route("/dyP10",methods=['GET'])
def fdy2():
    filname = request.args.get('v')
    t=impo(filname)
    val_obj_fu,data,=fc_ob(t)
    return render_template("resultat.html",data=data,val_fct_obj=val_obj_fu)


@poly.route("/rundyP10",methods=['GET', 'POST'])
def fff1():
    filname = request.args.get('v')
    t=impo(filname)
    data,val_fct_obj=fff(t) 
    return render_template("resultat.html",data=data,val_fct_obj=val_fct_obj)










@poly.route("/pro2.html")
def abbb2():
    return render_template("/pro2.html")


@poly.route("/met2fun.html")
def abbb22():
    return render_template("/met2fun.html")

@poly.route("/meta2P10",methods=['GET'])
def ffff1():
    filname = request.args.get('v')
    t=impo2(filname)
    data=met_fun(t) 
    return render_template("resultat1.html",data=data)
         


@poly.route("/dyn2pro.html")
def abbb222():
    return render_template("/dyn2pro.html")

    
@poly.route("/dy2P10",methods=['GET'])
def ffff11():
    filname = request.args.get('v')
    t=impo2(filname)
    val_fct_obj,data=fo_ob2(t) 
    return render_template("resultat3.html",data=data,val_fct_obj=val_fct_obj)




@poly.route("/rundyP100",methods=['GET', 'POST'])       
def fffup():
    filname = request.args.get('v')
    if request.args.get('c')=='obj1' and request.args.get('b')=='dy':
        t=impo(filname)
        val_obj_fu,data,=fc_ob(t)
        return render_template("resultat.html",data=data,val_fct_obj=val_obj_fu)
    elif request.args.get('c')=='obj1' and request.args.get('b')=='mt':
        t=impo(filname)
        data,val_obj_fu=met_fun1(t)
        return render_template("resultat2.html",data=data,val_fct_obj=val_obj_fu)
    elif request.args.get('c')=='obj2' and request.args.get('b')=='mt':
        t=impo2(filname)
        data=met_fun(t) 
        return render_template("resultat1.html",data=data)
    elif request.args.get('c')=='obj2' and request.args.get('b')=='dy':
        t=impo2(filname)
        val_fct_obj,data=fo_ob2(t) 
        return render_template("resultat3.html",data=data,val_fct_obj=val_fct_obj)
    else :
        return render_template('index.html')








UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER







def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@poly.route('/1', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('fffup', v=filename,c=request.form['obj12'],b=request.form['dymeta']))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post  enctype=multipart/form-data>
      <input type=file name=file>
     
      <form method=get name=obj12  action= url_for('fffup') >
      <SELECT name=obj12 size="1">
        <OPTION value=obj1 selected >obj1</option>
        <OPTION value=obj2<>obj2</option>
        </SELECT>
        <SELECT name="dymeta" size="1">
        <OPTION value=dy selected>dy</option>
        <OPTION value=mt>mt</option>
        </SELECT>
        
        
        <input type="submit" value="go !">
        </form>
    </form>
    '''




















if __name__=="__main__":
        poly.run()
        