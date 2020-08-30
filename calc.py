from tkinter import *

# İstifadə olunacaq dəyişənlər
string = ""
fnt = ("Times new roman", 18, "bold")
fnt2 = ("Times new roman", 18, "italic")
bgColor = '#D8D8D8'

# İstifadə olunacaq funksiyalar
def press(num):
    global string
    string += str(num)
    process.set(string)

#Errorlar daha detallı yazıla bilər
def equal_press():
    try:
        global string
        total = str(eval(string))
        process.set(total)
    except:
        process.set(" error ")
        string = ""


def clear():
    global string
    string = ""
    process.set("")


if __name__ == "__main__":
# Tkinter pəncərəsi
    root = Tk()
# Pəncərənin ölçüləri və başlıq
    root.title("Calculator")
    root.geometry("391x340")
    root.resizable(width=False, height=False)
    root.iconbitmap("calc.ico")
# Proqramın input hissəsi
    process = StringVar()
    textArea = Entry(root, font=("Arial", 15, "italic"), textvariable=process, width=27, bg="#F0F0F0")
    textArea.grid(row=0, column=0, columnspan=4, ipadx=3)
    process.set("Əməliyyatı daxil edin")
# Buttonlar
    btn1 = Button(root, text=' 7 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(7), height=1, width=5)
    btn1.grid(row=1, column=0)

    btn2 = Button(root, text=' 8 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(8), height=1, width=5)
    btn2.grid(row=1, column=1)

    btn3 = Button(root, text=' 9 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(9), height=1, width=5)
    btn3.grid(row=1, column=2)

    btn4 = Button(root, text=' 4 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(4), height=1, width=5)
    btn4.grid(row=2, column=0)

    btn5 = Button(root, text=' 5 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(5), height=1, width=5)
    btn5.grid(row=2, column=1)

    btn6 = Button(root, text=' 6 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(6), height=1, width=5)
    btn6.grid(row=2, column=2)

    btn7 = Button(root, text=' 1 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(1), height=1, width=5)
    btn7.grid(row=3, column=0)

    btn8 = Button(root, text=' 2 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(2), height=1, width=5)
    btn8.grid(row=3, column=1)

    btn9 = Button(root, text=' 3 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(3), height=1, width=5)
    btn9.grid(row=3, column=2)

    btn0 = Button(root, text=' 0 ', font=fnt, fg='black', bg=bgColor, command=lambda: press(0), height=1, width=5)
    btn0.grid(row=4, column=1, columnspan=1)

    btnPlus = Button(root, text=' + ', font=fnt2, fg='black', bg=bgColor, command=lambda: press("+"), height=1, width=5)
    btnPlus.grid(row=3, column=3)

    btnMinus = Button(root, text=' - ', font=fnt2, fg='black', bg=bgColor, command=lambda: press("-"), height=1,
                      width=5)
    btnMinus.grid(row=2, column=3)

    btnMultiply = Button(root, text=' * ', font=fnt2, fg='black', bg=bgColor, command=lambda: press("*"), height=1,
                         width=5)
    btnMultiply.grid(row=1, column=3)

    btnDivide = Button(root, text=' / ', font=fnt2, fg='black', bg=bgColor, command=lambda: press("/"), height=1,
                       width=5, padx=6)
    btnDivide.grid(row=4, column=0)

    btnEqual = Button(root, text=' = ', font=fnt2, fg='black', bg=bgColor, command=equal_press, height=1, width=5)
    btnEqual.grid(row=4, column=3)

    btnClear = Button(root, text='Ekranı təmizlə', font=fnt2, fg='black', bg=bgColor, command=clear, height=1, width=23,
                      padx=7)
    btnClear.grid(row=5, column=0, columnspan=4)

    btnDecimal = Button(root, text='.', font=fnt2, fg='black', bg=bgColor, command=lambda: press('.'), height=1,
                        width=5, padx=6)
    btnDecimal.grid(row=4, column=2)

    root.mainloop()
