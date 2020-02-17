import tkinter as tk  # 使用Tkinter前需要先匯入

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('Entry')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x


def show():
    text = en.get()
    lb.config(text=text)


lb = tk.Label(bg='white', fg='blue', text="顯示內容")
lb.pack()

en = tk.Entry()
en.pack()

btn = tk.Button(text="ok", command=show)
btn.pack()

window.mainloop()
