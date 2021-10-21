###########
# tkinter #
###########

from tkinter import * #Importing GUI operator in python
expression = ""


def press(num): # creating a operator for button
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress(): #Creating a Operator for button 
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
if __name__ == "__main__":
    gui = Tk()# taking tkinter
    x_Left = int(gui.winfo_screenwidth() / 2 - 400 / 2)  # x and left coordinates of the root window
    y_Top = int(gui.winfo_screenheight() / 2 - 300 / 2)  # y and top coordinates of the root window
    gui.configure(background="light grey")# adding background colour
    gui.title("GUI Calculator") # adding the program name
    gui.geometry(f'380x200+{x_Left}+{y_Top}')  # set new geometry
    gui.resizable(0, 0)  # Indicates that window is non resizable
    #gui.geometry("430x210") #the geometric size
    equation = StringVar() # givinng a name to string variable
    expression_field = Entry(gui, textvariable=equation, font=("arial", 15), width= 10, border=5) # Adding a text variable type
    expression_field.grid(columnspan=3, ipadx=80) # adding the size for the textbar
    #expression_field.pack()
    equation.set('Calculate Here') # The first displayed sentence on the textbar
    button1 = Button(gui, text=' 1 ', fg='black', bg='light grey', font=("arial", 15 ), # from here the button type what is inputted what is it's size is defined
                     command=lambda: press(1), height=1, width=8)
    button1.grid(row=3, column=0)


    button2 = Button(gui, text=' 2 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(2), height=1, width=8)
    button2.grid(row=3, column=1)


    button3 = Button(gui, text=' 3 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(3), height=1, width=8)
    button3.grid(row=3, column=2)


    button4 = Button(gui, text=' 4 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(4), height=1, width=8)
    button4.grid(row=4, column=0)


    button5 = Button(gui, text=' 5 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(5), height=1, width=8)
    button5.grid(row=4, column=1)


    button6 = Button(gui, text=' 6 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(6), height=1, width=8)
    button6.grid(row=4, column=2)


    button7 = Button(gui, text=' 7 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(7), height=1, width=8)
    button7.grid(row=5, column=0)


    button8 = Button(gui, text=' 8 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(8), height=1, width=8)
    button8.grid(row=5, column=1)


    button9 = Button(gui, text=' 9 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(9), height=1, width=8)
    button9.grid(row=5, column=2)


    button0 = Button(gui, text=' 0 ', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press(0), height=1, width=8)
    button0.grid(row=4, column=3)


    plus = Button(gui, text=' + ', fg='black', bg='light grey',font=("arial", 15 ),
                  command=lambda: press("+"), height=1, width=8)
    plus.grid(row=2, column=0)


    minus = Button(gui, text=' - ', fg='black', bg='light grey',font=("arial", 15 ),
                   command=lambda: press("-"), height=1, width=8)
    minus.grid(row=2, column=1)


    multiply = Button(gui, text=' x ', fg='black', bg='light grey',font=("arial", 15 ),
                      command=lambda: press("*"), height=1, width=8)
    multiply.grid(row=2, column=2)


    divide = Button(gui, text=' / ', fg='black', bg='light grey',font=("arial", 15 ),
                    command=lambda: press("/"), height=1, width=8)
    divide.grid(row=2, column=3)


    equal = Button(gui, text=' = ', fg='black', bg='light grey',font=("arial", 15 ),
                   command=equalpress, height=1, width=8)
    equal.grid(row=5, column=3)


    clear = Button(gui, text='C', fg='black', bg='light grey',font=("arial", 15,  ),
                   command=clear, height=1, width=8)
    clear.grid(row=0, column=3)


    Decimal = Button(gui, text='.', fg='black', bg='light grey',font=("arial", 15 ),
                     command=lambda: press('.'), height=1, width=8)
    Decimal.grid(row=3, column=3)

    gui.mainloop()#here we add the curser and end the program
