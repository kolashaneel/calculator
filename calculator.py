from tkinter import *

mw = Tk()
mw.title('calculator')
mw.iconbitmap("images/cal.ico")
mw['bg']='#ccccff'


def disp_clear():
    disp.delete(0, END)


def btn_clk(text):
    cnum = disp.get()
    disp_clear()
    fnum = cnum + text
    disp.insert(0, fnum)


first_num = 0

def eq():
    value=disp.get()
    disp_clear()
    disp.insert(0,str(eval(value)))

btn_bg='#ccf2ff'
# create
disp = Entry(mw, width=14, font=('Digital-7 Mono', 28), justify=RIGHT)
btn0 = Button(mw, text='0', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('0'),bg=btn_bg)
btn1 = Button(mw, text='1', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('1'),bg=btn_bg)
btn2 = Button(mw, text='2', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('2'),bg=btn_bg)
btn3 = Button(mw, text='3', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('3'),bg=btn_bg)
btn4 = Button(mw, text='4', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('4'),bg=btn_bg)
btn5 = Button(mw, text='5', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('5'),bg=btn_bg)
btn6 = Button(mw, text='6', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('6'),bg=btn_bg)
btn7 = Button(mw, text='7', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('7'),bg=btn_bg)
btn8 = Button(mw, text='8', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('8'),bg=btn_bg)
btn9 = Button(mw, text='9', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('9'),bg=btn_bg)
clear = Button(mw, text="clear", padx=74, pady=10, font=('Digital-7 Mono', 14), command=disp_clear,bg=btn_bg)
add = Button(mw, text='+', padx=36, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('+'),bg=btn_bg)
sub = Button(mw, text='-', padx=38, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('-'),bg=btn_bg)
div = Button(mw, text='/', padx=38, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('/'),bg=btn_bg)
mul = Button(mw, text='*', padx=38, pady=10, font=('Digital-7 Mono', 14), command=lambda: btn_clk('*'),bg=btn_bg)
eql = Button(mw, text='=', padx=36, pady=40, font=('Digital-7 Mono', 14), command=eq,bg=btn_bg)

# show
disp.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
btn7.grid(row=1, column=0, padx=2, pady=2)
btn8.grid(row=1, column=1, padx=2, pady=2)
btn9.grid(row=1, column=2, padx=2, pady=2)
btn4.grid(row=2, column=0, padx=2, pady=2)
btn5.grid(row=2, column=1, padx=2, pady=2)
btn6.grid(row=2, column=2, padx=2, pady=2)
btn1.grid(row=3, column=0, padx=2, pady=2)
btn2.grid(row=3, column=1, padx=2, pady=2)
btn3.grid(row=3, column=2, padx=2, pady=2)
btn0.grid(row=4, column=0, padx=2, pady=2)
clear.grid(row=4, column=1, padx=2, pady=2, columnspan=2)
add.grid(row=5, column=0, padx=2, pady=2)
sub.grid(row=5, column=1, padx=2, pady=2)
div.grid(row=6, column=0, padx=2, pady=2)
mul.grid(row=6, column=1, padx=2, pady=2)
eql.grid(row=5, column=2, padx=2, pady=2, rowspan=2)

mw.mainloop()
