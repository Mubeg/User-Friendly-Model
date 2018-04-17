from tkinter import *
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pickle
import random

model = pickle.load(open('model.pkl', 'rb'))

def predict(x_test):
        return(model.predict([x_test]))

alphabet = list(map(chr, range(ord('A'), ord('Z')+1)))
root = Tk()
entries = []
labels = []
btns = []
data_base = {x: [random.randint(1, 3)*10 for _ in range(1, 8)] for x in alphabet}

def get_answer_1(event):
        array = entries[-1].get('1.0', END).split(':')
        arr = sorted(data_base, key = lambda x: predict(data_base[x]), reverse = True)
        print('Верхний - лучший')
        for i in arr:
                if i in array:
                        print(i + ":", predict(data_base[i]))
def get_answer_2(event):
        arr = sorted(data_base, key = lambda x: predict(data_base[x]), reverse = True)
        print('Верхний - лучший')
        for i in arr:
                print(i + ":", predict(data_base[i]))

def change_screen(event):
        for a in btns:
                a.grid_forget()
        for a in labels:
                a.grid_forget()
        for a in entries:
                a.grid_forget()
        labels.append(Label(root, text = "Введите названия больниц (заглавные буквы английкого алфавита) через \":\" без пробелов. Например: \"A:\", \"A:B:C:D\")", width = 15*8, height = 5, bg = "white", fg = "black"))
        entries.append(Text(root, width = 15*8, height = 5, bg = "white", fg = "black"))
        btns.append(Button(root, text = "Посчитать", width = 15*8, height = 5, bg = "white", fg = "black"))
        labels[-1].grid(row = 1, column = 1)
        entries[-1].grid(row = 2, column = 1)
        btns[-1].grid(row = 3, column = 1)
        btns[-1].bind("<Button-1>", get_answer_1)
def calculate(event):
        x_test = []
        valid = 1
        for enter in entries:
                try:
                        x_test.append(10 * int(enter.get('1.0', END)))
                except:
                        labels[0]['text'] = "Неверный формат данных"
                        valid = 0
        if valid:
                ans = predict(x_test)
                labels[0]['text'] = str(ans)

def loop():
        texts = '''
3 - Выше среднего по стране
2 - Стреднее по стране
1 - Ниже среднего по стране

'''
        labels.append(Label(root, text = "Результат", width = 15*8, height = 5, bg = "white", fg = "black"))
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
        btns.append(Button(root, text = "Из моих больниц", width = 15, height = 5, bg = "white", fg = "black"))
        btns.append(Button(root, text = "Из всей базы данных", width = 20, height = 5, bg = "white", fg = "black"))
        
        btns[0].bind("<Button-1>", calculate)
        btns[1].bind("<Button-1>", change_screen)
        btns[2].bind("<Button-1>", get_answer_2)
        for i in range(len(entries)):
                entries[i].grid(row = 2, column = i + 1)
        btns[0].grid(row = 2, column = 8)
        btns[1].grid(row = 3, column = 8)
        btns[2].grid(row = 4, column = 8)
        labels[0].grid(row = 3, column = 1, columnspan = 7)
        for i in range(1, 8):
                labels[i].grid(row = 1, column = i)
        labels[8].grid(row = 4, column = 1, columnspan = 7)

        root.mainloop()
loop()
