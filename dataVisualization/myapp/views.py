from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd

# Create your views here.

def index(request):
    return render(request,'Layouts/app.html')

def tableau(request):
    dataset = pd.read_csv('StudentsPerformance.csv')
    columns = dataset.columns.tolist()
    dataset = np.array(dataset)
    return render(request,'Layouts/tableau.html',{'columns':columns,'data':dataset})

def statistics(request):
    dataset = pd.read_csv('StudentsPerformance.csv')

    s1 = dataset["math score"]
    s2 = dataset["reading score"]
    s3 = dataset["writing score"]

    t = []

    for i in range (len(s1)):
        cal = (s1[i] + s2[i] + s3[i]) / 3
        t.append(cal)

    dataset["total score"] = t

    columns = dataset.columns.tolist()

    female = dataset[dataset["gender"]=="female"]

    femaleSup70 = female[female["total score"]>= 70]
    femaleSup50 = female[female["total score"]>= 50]
    femaleSup0 = female[female["total score"]<50]

    male = dataset[dataset["gender"]=="male"]

    maleSup70 = male[male["total score"]>= 70]
    maleSup50 = male[male["total score"]>= 50]
    maleSup0 = male[male["total score"]<50]


    femValues = [len(femaleSup70), len(femaleSup50), len(femaleSup0)]

    maleValues = [len(maleSup70), len(maleSup50), len(maleSup0)]

    sc = len(dataset[dataset["parental level of education"]=="some college"])
    ad = len(dataset[dataset["parental level of education"]=="associate's degree"])
    hs = len(dataset[dataset["parental level of education"]=="high school"])
    shs = len(dataset[dataset["parental level of education"]=="some high school"])
    bd = len(dataset[dataset["parental level of education"]=="bachelor's degree"])
    md = len(dataset[dataset["parental level of education"]=="master's degree"])

    level = [sc , ad , hs , shs , bd , md]

    nbMale = len(dataset[dataset["gender"]=="male"])
    nbFemale = len(dataset[dataset["gender"]=="female"])

    gender = [nbMale , nbFemale]

    l1 = len(dataset[dataset["lunch"]=="standard"])
    l2 = len(dataset[dataset["lunch"]=="free/reduced"])

    lunch = [l1 , l2]

    t1 = len(dataset[dataset["test preparation course"]=="none"])
    t2 = len(dataset[dataset["test preparation course"]=="completed"])

    test = [t1 , t2]
    

    return render(request,'Layouts/statistics.html',{'femValues':femValues,'maleValues':maleValues , 'level': level, 'gender': gender, 'lunch': lunch, 'test': test})