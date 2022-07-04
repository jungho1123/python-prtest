import tkinter
from tkinter import *

def calculate():
    money = int(et.get())
    print('일반커피 300원')
    money -= 300
    et.delete(0, tkinter.END)
    et.insert(0, money)

def calculate2():
    money=int(et.get())
    money -= 500
    print('고급커피 500원')
    et.delete(0, tkinter.END)
    et.insert(0, money)

def putmoney():
    a = int(input('돈을 넣어주세요 '))
    et.delete(0, END)
    et.insert(0, int(a))

def change():
    change = int(et.get())
    ch2.delete(0,END)
    ch2.insert(0,int(change))

def getcoin():
    ch2.delete(0,END)
    et.delete(0, END)
    et.insert(0,'이용해주셔서 감사합니다')

win = Tk()
win.geometry('810x600')
win.title('커피 자판기')

title = Label(win, text='coffee 자판기', font=('Arial', 25))
title.grid(row=0, columnspan=4, pady=7)
title.anchor(CENTER)

m = Button(win, text='밀크커피(일반)', width=26, height=10, command=calculate)
m.grid(row=1, column=0, padx=5)
s = Button(win, text='설탕커피(일반)', width=26, height=10, command=calculate)
s.grid(row=1, column=1, padx=5)
b = Button(win, text='블랙커피(일반)', width=26, height=10, command=calculate)
b.grid(row=1, column=2, padx=5)
c = Button(win, text='크림커피(일반)', width=26, height=10, command=calculate)
c.grid(row=1, column=3, padx=5)

lb = Label(win, height=1)
lb.grid(row=2, column=0)

m = Button(win, text='밀크커피(고급)', width=26, height=10, command=calculate2)
m.grid(row=3, column=0, padx=5)
s = Button(win, text='설탕커피(고급)', width=26, height=10, command=calculate2)
s.grid(row=3, column=1, padx=5)
b = Button(win, text='블랙커피(고급)', width=26, height=10, command=calculate2)
b.grid(row=3, column=2, padx=5)
c = Button(win, text='크림커피(고급)', width=26, height=10, command=calculate2)
c.grid(row=3, column=3, padx=5)

lb2 = Label(win, height=1)
lb2.grid(row=4, column=0)


m = Button(win, text='돈을 넣어주세요', width=26, command=putmoney)
m.grid(row=5, column=0, padx=5, pady=10)
et = Entry(win, width=26)
et.grid(row=5, column=1)

ch1=Button(win, text='주문 종료', width=26, command=change)
ch1.grid(row=5, column=2, pady=10)
ch2=Entry(win, width=26)
ch2.grid(row=5, column=3, pady=10)

re=Button(win, text='반환', width=26, height=3, command=getcoin)
re.grid(row=6, column=0, columnspan=4, pady=10)

price=Label(win, text='일반 커피 300원, 고급 커피 500원!', font=(12))
price.grid(row=7, columnspan=4, pady=10)

win.mainloop()
