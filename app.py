from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import re
import uuid
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegressionCV

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",href="travel")

@app.route("/travel",methods=["GET", "POST"])
def travel():
    request_type_str = request.method
    if request_type_str == "GET":
        return render_template("travel.html")
    if request_type_str == "POST":
        return ticket()

def Lname(x):
        pattern = r"([a-zA-Z]*), ([a-zA-Z]*). ([a-zA-Z ]*)"
        results = re.match(pattern,str(x))
        if results is not None:
            return results[1]
        else:
            return "-"

def title(x):
        pattern = r"([a-zA-Z]*), ([a-zA-Z ]*). ([a-zA-Z ]*)"
        results = re.match(pattern,str(x))
        if results is not None:
            return results[2]
        else:
            return "-"

def cabin(x):
        pattern = "([a-zA-Z]*)[0-9]*"
        results = re.match(pattern,str(x))
        if results is not None:
            return results[1]
        else:
            return "-"

@app.route("/ticket",methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        name = request.form['last name']+", "+request.form["title"]+". "+request.form["first name"]
        sex = request.form["sex"]
        pclass = request.form["class"]
        embarked = request.form['embarked']
        age = request.form['age']
        SibSp = int(request.form["siblings"])+int(request.form["epouses"])
        Parch = int(request.form["parents"])+int(request.form["children"])
        Ticket = random.randint(100000,1000000000)
        Fare = random.randint(0,600)
        Cabin = ''.join((random.choice('ABCDEFG') for i in range(1)))+str(random.randint(10,99))
        l = [pclass, name, sex, age, SibSp, Parch, Ticket,Fare, Cabin, embarked]
        L = [pclass, name, sex, age, Ticket, Cabin, embarked]
        print(l)
    train_set = pd.read_csv("./titanic/train.csv").set_index('PassengerId')
    test_set = pd.DataFrame([l],columns=['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket','Fare', 'Cabin', 'Embarked'])
    # extract Last name
    train_set["Last name"] = train_set["Name"].apply(Lname)
    test_set["Last name"] = test_set["Name"].apply(Lname)
    # extract title
    train_set["title"] = train_set["Name"].apply(title)
    test_set["title"] = test_set["Name"].apply(title)
    # remove name
    train_set = train_set.drop("Name",axis=1)
    test_set = test_set.drop("Name",axis=1)

    # extract Cabin
    train_set["Cabin"] = train_set["Cabin"].apply(cabin)

    y = train_set[["Survived"]]
    train_set = train_set.drop("Survived",axis=1)
    y['Survived'] = y['Survived'].astype(float)

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    train_set_num = train_set.select_dtypes(include=numerics)
    test_set_num = test_set.select_dtypes(include=numerics)
    l=[]
    for col in train_set.columns:
        if col not in train_set_num.columns:
            l.append(col)
    train_set_cat = train_set[l]
    test_set_cat = test_set[l]

    # Numerical Pipeline
    num_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean'))
        ,('scaler', StandardScaler())
    ])
    # Categorical Pipeline
    cat_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant'))
        ,('encoder', OrdinalEncoder())
    ])

    # ColumnTransformer
    preprocessor = ColumnTransformer(
    transformers=[
        ('numeric', num_pipeline, train_set_num.columns)
    ,('categorical', cat_pipeline, train_set_cat.columns)
    ])

    train_set_prepared = preprocessor.fit_transform(train_set)
    test_set_prepared = preprocessor.fit_transform(test_set)
    train_set_prepared = pd.DataFrame(train_set_prepared,columns=train_set.columns)
    test_set_prepared = pd.DataFrame(test_set_prepared,columns=test_set.columns)

    log_clf = LogisticRegressionCV(solver='liblinear')
    log_clf.fit(train_set_prepared,y["Survived"])
    y_pred = int(log_clf.predict(test_set_prepared))
    print(y_pred)
    print(log_clf.score(train_set_prepared,y["Survived"]))
    
    return render_template("ticket.html",y_pred = y_pred,L = L)