from tkinter import *
from datetime import datetime
from tkinter.messagebox import *


class TestTime(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('400x200')
        self.root.resizable(width=False, height=False)
        self.label_a = Label(self.root, text='当前本地时间为：\t\t')
        self.label_a.pack()
        self.label_b = Label(self.root, text="")
        self.label_b.pack()
        self.label_c = Label(self.root, text='\n距离中午吃饭还有：\t\t')
        self.label_c.pack()
        self.label_d = Label(self.root, text="")
        self.label_d.pack()
        self.label_e = Label(self.root, text='\n距离今天下班还有：\t\t')
        self.label_e.pack()
        self.label_f = Label(self.root, text="")
        self.label_f.pack()
        self.update_time()

    def update_time(self):
        self.update_a()
        self.update_b()
        self.update_c()

    def update_a(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.label_b.configure(text=now)
        self.root.after(1000, self.update_a)

    def update_b(self):
        # 获取当日日期，不包含时间，str
        now_day = datetime.now().strftime("%Y-%m-%d")
        # 字符串拼接，组成当日12点
        a = now_day + ' 12:00:00'
        new_time = datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
        t = new_time - datetime.now()
        self.label_d.configure(text=t)
        self.root.after(1000, self.update_b)

    def update_c(self):
        # 获取当日日期，不包含时间，str
        now_day = datetime.now().strftime("%Y-%m-%d")
        # 字符串拼接，组成当日12点
        a = now_day + ' 18:00:00'
        new_time = datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
        t = new_time - datetime.now()
        self.label_f.configure(text=t)
        self.root.after(1000, self.update_c)


if __name__ == '__main__':
    root = Tk()
    root.title('计时小界面')
    # 窗口置顶.
    root.wm_attributes('-topmost', 1)
    TestTime(root)
    root.mainloop()



