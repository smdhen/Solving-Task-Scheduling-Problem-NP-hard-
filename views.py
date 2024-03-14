from flask import Blueprint, render_template, request
from functions import fc_ob, fo_ob2, fff, met_fun1, met_fun2
from data import *
import flask

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    print('**********' + str(flask.__version__))
    return render_template('index.html')

@views.route("/methodes/<type>")
def methodes(type):
    return render_template('methodes.html', methode=type)


#---------------------------------------------------Programmation Dynamique---------------------------------------------------#

@views.route("/DP/<obj>/<nbTaches>")
def DP(obj, nbTaches):
    if int(obj) == 1:
        if int(nbTaches) == 10:
            data = data1_10
        elif int(nbTaches) == 50:
            data = data1_50 
        elif int(nbTaches) == 200:
            data = data1_200
        else:
            data = data1_500
        return render_template('methodes.html', methode="Programmation Dynamique", resultat=fc_ob(data))
    
    else:
        if int(nbTaches) == 10:
            data = data2_10
        elif int(nbTaches) == 100:
            data = data2_100
        elif int(nbTaches) == 200:
            data = data2_200
        else:
            data = data2_500
        
        return  render_template('methodes.html', methode="Programmation Dynamique", resultat=fo_ob2(data))

#---------------------------------------------------Métaheuristique---------------------------------------------------#

@views.route("/meta/<obj>/<nbTaches>")
def meta(obj, nbTaches):
    if int(obj) == 1:
        if int(nbTaches) == 10:
            data = data1_10
        elif int(nbTaches) == 50:
            data = data1_50 
        elif int(nbTaches) == 200:
            data = data1_200
        else:
            data = data1_500
        return render_template('methodes.html', methode="Métaheuristique", resultat=met_fun1(data, int(nbTaches)))
    
    else:
        if int(nbTaches) == 10:
            data = data2_10
        elif int(nbTaches) == 100:
            data = data2_100
        elif int(nbTaches) == 200:
            data = data2_200
        else:
            data = data2_500
        
        return  render_template('methodes.html', methode="Métaheuristique", resultat=met_fun2(data, int(nbTaches)))

#---------------------------------------------------Algorithme Polynomiale---------------------------------------------------#
    
@views.route("/poly/<obj>/<nbTaches>")
def poly(obj, nbTaches):
    if int(obj) == 1:
        if int(nbTaches) == 10:
            data = data1_10
        elif int(nbTaches) == 50:
            data = data1_50 
        elif int(nbTaches) == 200:
            data = data1_200
        else:
            data = data1_500
            
        return render_template('methodes.html', methode="Algorithme Polynomiale", resultat=fff(data))
    

#---------------------------------------------------Formulaire---------------------------------------------------#

@views.route("/upload/<algo>", methods = ['GET', 'POST'])
def upload(algo):
    if request.method == 'POST':    
        f = request.files['file']
        nb = int(f.readline().split()[0])
        list_P1 = f.readline().split()
        list_D1 = f.readline().split()
        
        
        list_P1 = list(map(int, list_P1))
        list_D1 = list(map(int, list_D1))
        
        if request.form.get('obj') == 'obj1':

            data = [[i, list_P1[i], list_D1[i]] for i in range(nb)]
        
            if algo == 'Programmation Dynamique':
                return render_template('methodes.html', methode="Programmation Dynamique", resultat=fc_ob(data))
            elif algo == 'Métaheuristique':
                return render_template('methodes.html', methode="Métaheuristique", resultat=met_fun1(data, nb))
            else:
                return render_template('methodes.html', methode="Algorithme Polynomiale", resultat=fff(data))
                
                
        else:
            list_ai = f.readline().split()
            list_bi = f.readline().split()
            
            list_ai = list(map(int, list_ai))
            list_bi = list(map(int, list_bi))
            
            data = [[i, list_P1[i], list_D1[i], list_ai[i], list_bi[i]] for i in range(nb)]
            
            if algo == 'Programmation Dynamique':
                 return  render_template('methodes.html', methode="Programmation Dynamique", resultat=fo_ob2(data))
            else:
                return  render_template('methodes.html', methode="Métaheuristique", resultat=met_fun2(data, nb))
            