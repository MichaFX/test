from tkinter import *
#Функции
def digit_get(digit):
    value = calculator.get()
    value = value + digit
    calculator.delete(0, 'end')
    calculator.insert(0, value)

#Переменные

#Основной код
win = Tk()
win.geometry('170x110')
win.config(bg='black')

calculator = Entry(win).grid(row=0, column=0, columnspan=4, sticky='we')
#Кнопки цифр
button1 = Button(win, text='1', command=digit_get(1)).grid(row=1, column=0, stick='we')
button2 = Button(win, text='2', command=digit_get(1)).grid(row=1, column=1, stick='we')
button3 = Button(win, text='3', command=digit_get(1)).grid(row=1, column=2, stick='we')
button4 = Button(win, text='4', command=digit_get(1)).grid(row=2, column=0, stick='we')
button5 = Button(win, text='5', command=digit_get(1)).grid(row=2, column=1, stick='we')
button6 = Button(win, text='6', command=digit_get(1)).grid(row=2, column=2, stick='we')
button7 = Button(win, text='7', command=digit_get(1)).grid(row=3, column=0, stick='we')
button8 = Button(win, text='8', command=digit_get(1)).grid(row=3, column=1, stick='we')
button9 = Button(win, text='9', command=digit_get(1)).grid(row=3, column=2, stick='we')
button0 = Button(win, text='0', command=digit_get(1)).grid(row=4, column=0, stick='we', columnspan=2)
#Кнопки действий
buttonplus = Button(win, text='+').grid(row=2, column=3, stick='we')
buttonminus = Button(win, text='-').grid(row=1, column=3, stick='we')
buttondel = Button(win, text='/').grid(row=3, column=3, stick='we')
buttonumn = Button(win, text='*').grid(row=4, column=2, stick='we')
buttonravn = Button(win, text='=').grid(row=4, column=3, stick='we')

win.grid_columnconfigure(4, minsize=200)

win.mainloop()
