import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Button Test')

    button = tk.Button(root, text = 'test me', padx= '20', pady = '20')
    button.grid()

    root.mainloop()
