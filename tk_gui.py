# pylint: disable=all


from tkinter import *

row_counter = 1
col_counter = 0
calculation = ""
button_arr = ["C", "/", "*", "+", "(", "0", ")", "-", "7",  "8", "9", ".",
              "4", "5", "6", "1", "2", "3"]


def add_calculate(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def evaluate_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert("error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, 'end')


def command_function(text):
    if text in "0123456789+-/*().":
        return lambda b=text: add_calculate(b)
    elif text == "=":
        return evaluate_calc
    else:
        return clear_field


def print_number():
    global row_counter, col_counter
    for i in range(len(button_arr)):
        button_text = button_arr[i]
        color = "#cffad6" if button_arr[i] not in "+-/*().C0" else "#f7dc92"
        button = Button(
            win, text=f'{button_arr[i]}', font="Helvetica 12 bold", width=12, command=command_function(button_text), height=3, activebackground="#a9d1f5", bg="white", pady=3, background=color)
        button.grid(row=row_counter, column=col_counter, padx=5, pady=6)

        col_counter += 1
        if col_counter == 4:
            col_counter = 0
            row_counter += 1
        elif row_counter == 4 and col_counter == 3:
            col_counter = 0
            row_counter += 1


win = Tk()
win.title("Kalkulátor")
win.geometry("560x520")
win.resizable(False, False)
text_result = Text(win, height=2, width=28, font=("Arial", 24), border=5)
text_result.grid(columnspan=5)
print_number()
equal_button = Button(win, text="=", font="Helvetica 12 bold", width=12, command=command_function(
    "="), height=8, activebackground="#0388fc", bg="#53a8f5")
equal_button.place(x=425, y=350)


win.mainloop()
