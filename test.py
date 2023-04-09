import tkinter as tk
class MyApp():
    def __init__(self, root, case):
        root.geometry('200x700+200+500')
        if case==1:
            tk.Label(root, text='Label', bg='green').pack()
            tk.Label(root, text='Label2', bg='red').pack()
        elif case==2:
            tk.Label(root, text='Label', bg='green').pack(expand=1, fill ='y')
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
        elif case==3:
            tk.Label(root, text='Label', bg='green').pack(expand=1)
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
        elif case==4:
            tk.Label(root, text='Label', bg='green').pack(fill='both', expand=1, side='left')
            tk.Label(root, text='Label2', bg='red').pack(fill='both', expand=1, side='right')
        else: # case 5
            tk.Label(root, text='Label', bg='green').pack(fill = 'both', expand=1)
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both', expand=1)
w1 = tk.Tk()
MyApp(w1,4)
# w2 = tk.Tk()
# MyApp(w2,5)
w1.mainloop()
# w2.mainloop()