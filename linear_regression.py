
from math import fabs
from re import X
from numpy import double
import pandas
from sklearn import linear_model

def lin_reg() -> double:   
    dataset = pandas.read_excel("artificial_autismDATA.xls", sheet_name= "Artificial")
    dataset.to_csv('dataset.csv', index = False)
    X = dataset[['A1BG', 'A1BG-AS1', 'A1CF', 'Age']]
    Y = dataset['ASDLevel']

    regression = linear_model.LinearRegression()
    regression.fit(X.values, Y.values)
    
    predicted_severity = regression.predict([[0.67, 0.12, 0.01, 20]])

    return predicted_severity