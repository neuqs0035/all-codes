import tkinter as tk

window = tk.Tk()
window.geometry("300x380")
message = tk.Label(text="Calculator",font=("monospace",13))

def read_input():
    val1 = val1entry.get()
    operator = operatorentry.get()
    val2 = val2entry.get()

    if (not val2.isdigit() or (not val2.isdigit()) ):
        outputmessage.config(text="Invalid Input")
    elif( operator not in ["+","-","*","/","%"]):
        outputmessage.config(text="Invalid Operator")
    else:
        match operator:
            case "+":
                answer = float(val1) + float(val2)
            case "-":
                answer = float(val1) - float(val2)
            case "*":
                answer = float(val1) * float(val2)
            case "/":
                answer = float(val1) / float(val2)
            case "%":
                answer = float(val1) % float(val2)

        outputmessage.config(text=f"Answer = {answer}")

val1message = tk.Label(text="Enter 1st Value : ",font=("monospace",10))
val1entry = tk.Entry(width="25")
operatormessage = tk.Label(text="Enter Operator : ",font=("monospace",10))
operatorentry = tk.Entry(width="25")
val2message = tk.Label(text="Enter 2nd Value : ",font=("monospace",10))
val2entry = tk.Entry(width="25")
button = tk.Button(text="Calculate",command=read_input,font=("monospace",10))
outputmessage = tk.Label(font=("monospace",10))

message.pack(ipady="20")
val1message.pack(ipady="10")
val1entry.pack(ipady="5")
operatormessage.pack(ipady="10")
operatorentry.pack(ipady="5")
val2message.pack(ipady="10")
val2entry.pack(ipady="5")
button.pack(pady="15")
outputmessage.pack(pady="15")
window.mainloop()
