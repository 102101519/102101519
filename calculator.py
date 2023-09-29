import tkinter as tk
import math
from math import sqrt

root = tk.Tk()
root.title("计算器")
root.geometry('320x275+200+200')
root.attributes('-alpha',0.95)
root['background']='white'
result_num = tk.StringVar()
result_num.set('')
#按钮操作的定义
def backspace():
    opt_str = result_num.get()
    new_str = opt_str[:-1]
    result_num.set(new_str)

def dot():
    result_num.set(result_num.get() + '.')

def square():
    result =float(result_num.get())**2
    result_num.set(str(result))

def square_root():
    try:
        result = sqrt(float(result_num.get()))
        result_num.set(str(result))
    except Exception as e:
        result_num.set("Error：负数不能开方")
def calculation():
    try:
        opt_str =result_num.get()
        result = eval(opt_str)
        result_num.set(str(result))
    except Exception as e:
        result_num.set("Error:错误的数字格式")
def clear():
    result=str('')
    result_num.set(str(result))

#按钮界面设计和功能设计
result_entry = tk.Entry(root, textvariable=result_num,font=('宋体',30),width=10,justify=tk.LEFT)
result_entry.grid(row=0, column=0, columnspan=4)

button_0 = tk.Button(root, text="0",width=5,font=('宋体',20),bg='gray',command=lambda: click_button('0'))
button_0.grid(row=6, column=2)

button_1 = tk.Button(root, text="1",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('1'))
button_1.grid(row=5, column=1)

button_2 = tk.Button(root, text="2",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('2'))
button_2.grid(row=5, column=2)

button_3 = tk.Button(root, text="3",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('3'))
button_3.grid(row=5, column=3)

button_4 = tk.Button(root, text="4",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('4'))
button_4.grid(row=4, column=1)

button_5 = tk.Button(root, text="5",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('5'))
button_5.grid(row=4, column=2)

button_6 = tk.Button(root, text="6",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('6'))
button_6.grid(row=4, column=3)

button_7 = tk.Button(root, text="7",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('7'))
button_7.grid(row=3, column=1)

button_8 = tk.Button(root, text="8",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('8'))
button_8.grid(row=3, column=2)

button_9 = tk.Button(root, text="9",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('9'))
button_9.grid(row=3, column=3)

button_plus = tk.Button(root, text="+",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('+'))
button_plus.grid(row=5, column=4)

button_minus = tk.Button(root, text="-",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('-'))
button_minus.grid(row=4, column=4)

button_multiply = tk.Button(root, text="*",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('*'))
button_multiply.grid(row=3, column=4)

button_divide = tk.Button(root, text="/",width=5,font=('宋体',20),bg='gray', command=lambda: click_button('/'))
button_divide.grid(row=2, column=4)

button_equal = tk.Button(root, text="=",width=5,font=('宋体',20),bg='gray', command=calculation)
button_equal.grid(row=6, column=4)

button_decimal = tk.Button(root, text=".",width=5,font=('宋体',20),bg='gray', command=dot)
button_decimal.grid(row=6, column=3)

button_backspace = tk.Button(root, text="del",width=5,font=('宋体',20),bg='gray', command=backspace)
button_backspace.grid(row=2, column=3)

button_square = tk.Button(root, text="square",width=5,font=('宋体',20),bg='gray', command=square)
button_square.grid(row=2, column=2)

button_sqrt = tk.Button(root, text="sqrt",width=5,font=('宋体',20),bg='gray', command=square_root)
button_sqrt.grid(row=2, column=1)

button_clear = tk.Button(root, text="C",width=5,font=('宋体',20),bg='gray', command=clear)
button_clear.grid(row=6, column=1)
def click_button(btn_text):
    opt_str = result_num.get()
    if btn_text == '=':
        try:
            result = eval(opt_str)
            result_num.set(str(result))
        except Exception as e:
            result_num.set("Error")
    else:
        try:
            result_num.set(result_num.get() + btn_text)
        except Exception as e:
            result_num.set("Error")

root.mainloop()