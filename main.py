from tkinter import *
from calculate import calculate

def main():
    n, k, d = map(int, input().split())
    root = Tk()
    root.geometry("200x200")
    answer = Label(root, text=calculate(n, k, d)).pack()
    root.mainloop()    


if __name__ == "__main__":
    main()
