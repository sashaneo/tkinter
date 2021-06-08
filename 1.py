import builtins
import tkinter as tk


def calculate_discount_percentage(total):
    discount = 0
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount

def calculate_discount(total):
    discount_percentage = calculate_discount_percentage(total)
    discount = total - total / 100 * discount_percentage
    return discount

def get_bill_total():
    
    entered_bill_total = entry_box.get()
    
    try:
        bill_total = float(entered_bill_total)
    except ValueError:
        textbox["text"] = "Incorrect value entered"
        return 

    final_total = format(calculate_discount(bill_total), '.02f')
    textbox["text"] = "USD" + final_total


window = tk.Tk()

window.geometry("400x210")
window.title("Billing Programme")

label = tk.Label(text="Enter Bill Total:")
label.place(x = 10, y = 20, height= 25)

label.config(bg="lightgreen", padx=0)

entry_box = tk.Entry(text="")
entry_box.place(x =10, y = 40, width= 110, height = 25)

button = tk.Button(text= "Calc Bill", command = get_bill_total)
button.config(font="16")
button.place(x = 10, y = 170, width = 380, height = 35)

label2 = tk.Label(text="Total Price (after discount):")
label2.place(x = 140, y = 20)

label2.config(bg="lightgreen", padx=0)
textbox = tk.Message(text="USD 0.00", width=200, font="16")
textbox.config(bg="lightgreen", padx=0)
textbox.place(x = 140, y = 40)



window.mainloop()


