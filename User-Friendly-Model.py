from tkinter import *
import math
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))
def predict(x_test):
        return(model.predict([x_test]))

entries = []
labels = []

def calculate(event):
        x_test = []
        valid = 1
        for enter in entries:
                try:
                        x_test.append(10 * int(enter.get('1.0', END)))
                except:
                        labels[0]['text'] = "Invalid Data"
                        valid = 0
        if valid:
                ans = predict(x_test)
                labels[0]['text'] = str(ans)

def mainloop():
        btns = []
        root = Tk()
        texts = '''
3 - Больше среднего по стране
2 - Стреднее по стране
1 - Меньше среднего по стране

'''
        labels.append(Label(root, text = "Calculation", width = 15*8, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Выживаемость", width = 15, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Медицинская безопасность", width = 25, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Качество гопитализации", width = 20, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Облуживание пациентов", width = 20, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Эффективность ухода", width = 20, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Своевременность ухода", width = 20, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = "Эффективность использования медицинской интроскопии", width = 50, height = 5, bg = "white", fg = "black"))
        labels.append(Label(root, text = texts, width = 25, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 13, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 17, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 13, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 13, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 13, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 13, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 43, height = 5, bg = "white", fg = "black"))
        btns.append(Button(root, text = "Посчитать", width = 15, height = 5, bg = "white", fg = "black"))
        btns[0].bind("<Button-1>", calculate)
        for i in range(len(entries)):
                entries[i].grid(row = 2, column = i + 1)
        btns[0].grid(row = 2, column = 8)
        labels[0].grid(row = 3, column = 1, columnspan = 7)
        for i in range(1, 8):
                labels[i].grid(row = 1, column = i)
        labels[8].grid(row = 4, column = 1, columnspan = 7)
        root.mainloop()
mainloop()
