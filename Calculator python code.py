#create a simple claculator with 2 numbers including plus and minus and quit buttons

import tkinter as tk
import tkinter.messagebox as tkm

def add():
    #get entry1 and entry2
    value1= entry1.get()
    value2=entry2.get()
    #sum
    number1=float(value1)
    number2=float(value2)
    total=number1 +number2

    #display
    tkm.showinfo('Sum',str(total))

def minus():
    #get entry1 and entry2
    value1= entry1.get()
    value2=entry2.get()
    #sum
    number1=float(value1)
    number2=float(value2)
    diff=number1-number2

    #display
    tkm.showinfo('Sum',str(total))

    
    

window=tk.Tk()
frame1=tk.Frame(window)
frame1.pack()

frame2=tk.Frame(window)
frame2.pack()

frame3=tk.Frame(window)
frame3.pack()

#label and button
#frame 1
label1=tk.Label(frame1,text='Number 1:')
label1.pack(side='left')

entry1=tk.Entry(frame1)
entry1.pack()

#frame2
label2=tk.Label(frame2,text='Number 2:')
label2.pack(side='left')

entry2=tk.Entry(frame2)
entry2.pack()

#frame3

button1=tk.Button(frame3,text='+',command=add)
button1.pack(side='left')

button2=tk.Button(frame3,text='-',command=minus)
button2.pack(side='left')

button3=tk.Button(frame3,text='Quit',command=window.destroy)
button3.pack(side='left')






window.mainloop()
