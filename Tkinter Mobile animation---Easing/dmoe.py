import threading
import time
import tkinter as tk
import Easing


win = tk.Tk()
win.geometry('1000x500')


btn = tk.Button(win, text="我是按钮")
btn.place(x=10, y=20)
btn.update()


btn1 = tk.Button(win, text="我是按钮")
btn1.place(x=10, y=70)
btn1.update()


btn2 = tk.Button(win, text="我是按钮")
btn2.place(x=10, y=120)
btn2.update()



btn3 = tk.Button(win, text="我是按钮")
btn3.place(x=10, y=170)
btn3.update()



btn4 = tk.Button(win, text="我是按钮")
btn4.place(x=10, y=220)
btn4.update()




btn5 = tk.Button(win, text="我是按钮")
btn5.place(x=10, y=270)
btn5.update()



btn6 = tk.Entry(win)
btn6.place(x=10, y=320)
btn6.update()


btn7 = tk.Checkbutton(win, text="我是选择框")
btn7.place(x=10, y=370)
btn7.update()



def callback():
    t = 1
    Easing.EaseInQuad(btn, "X", btn.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseInElastic(btn1, "X", btn1.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseOutExpo(btn2, "X", btn2.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EseLinear(btn3, "X", btn3.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseInOutSine(btn4, "X", btn4.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseInCirc(btn5, "X", btn5.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseInSine(btn6, "X", btn6.winfo_x(), 600, 3)
    time.sleep(t)
    Easing.EaseOutQuad(btn7, "X", btn7.winfo_x(), 600, 3)
    # Easing.EaseInElastic(组件, "X或Y轴", 组件初始位置, 组件结束位置, 速度（越大越慢）)
def a():
    threading.Thread(target=callback).start()
print()
btn.configure(command=a)




win.mainloop()