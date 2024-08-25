import tkinter as tk
import Easing


win = tk.Tk()
win.geometry('1000x300')


btn = tk.Button(win, text="我是按钮")
btn.place(x=10, y=20)
btn.update()


def callback():
    Easing.EaseInElastic(btn, "X", btn.winfo_x(), 600, 3)
    # Easing.EaseInElastic(组件, "X或Y轴", 组件初始位置, 组件结束位置, 速度（越大越慢）)
print()
btn.configure(command=callback)

win.mainloop()