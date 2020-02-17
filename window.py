import tkinter as tk  # 使用Tkinter前需要先匯入

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長 * 寬)
# geometry('長x寬＋Ｘ＋Ｙ')
window.geometry('500x300')  # 這裡的乘是小x

window.mainloop()
