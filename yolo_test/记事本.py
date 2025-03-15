# 导入库

# tkinter库
from tkinter import *
import tkinter.ttk

# tkinter中的tk
import tkinter as tk

# 时间库
import time

# os库
import os

# sys库
import sys

# csv库
import csv

# tkinter中的消息提示框库
from tkinter import messagebox

# tkinter中的filedialog，读取文件信息
import tkinter.filedialog
from tkinter import filedialog

# 文件命名
now = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(time.time()))
nameofthefile = now + ".txt"
lingcunweidemingzi = nameofthefile
jishibenmingcheng = "记事本文件：" + nameofthefile
chongmingmingtitle = jishibenmingcheng
root = tkinter.Tk()
root.title(chongmingmingtitle)
root.geometry("750x500")
banbenhao = "20240802_1"


# 主题部分


def lingcunwei():
    gettext = text.get("1.0", "end")
    fname = time.strftime(chongmingmingtitle)
    with open(fname, 'w') as f:
        f.write(gettext)


def baocun():
    def rootcunweizhi_b1_command():
        def lingcunwei_wrongqingkuang():
            get_text = text.get("1.0", "end")
            with open(jishibenmingcheng, 'w') as f:
                f.write(get_text)

        baocunkuangweizhi = rootcunweizhi_e1.get()
        baocunkuangweizhiiii = baocunkuangweizhi
        try:
            rootcunweizhi_b1_command_kai1 = open(baocunkuangweizhiiii, 'r')
            rootcunweizhi_b1_command_kai1.close()

            rootcunweizhi_b1_command_kai2 = open(baocunkuangweizhiiii, 'w')
            get_text = text.get("1.0", "end")
            rootcunweizhi_b1_command_kai2.write(get_text)
            rootcunweizhi_b1_command_kai2.close()

        except:
            rootcunweizhi_wrong = tkinter.Tk()
            rootcunweizhi_wrong.title("错误")
            rootcunweizhi_wrong_l1 = Label(rootcunweizhi_wrong, text="文件还没有保存至电脑，建议先另存为")
            rootcunweizhi_wrong_l1.pack()
            rootcunweizhi_wrong_b1 = Button(rootcunweizhi_wrong, text="去另存为>>>", command=lingcunwei_wrongqingkuang)
            rootcunweizhi_wrong_b1.pack()

    rootcunweizhi = tkinter.Tk()
    rootcunweizhi.title("保存位置")
    rootcunweizhi_l1 = Label(rootcunweizhi, text="请将文件的名称完整填写在下方（包含后缀名）：")
    rootcunweizhi_l1.pack()
    rootcunweizhi_e1 = Entry(rootcunweizhi)
    rootcunweizhi_e1.pack()
    rootcunweizhi_b1 = Button(rootcunweizhi, text="确定", command=rootcunweizhi_b1_command)
    rootcunweizhi_b1.pack()


def open_command():
    def open_a_new_window():
        global filePath
        filePath = tkinter.filedialog.askopenfilename(defaultextension=".txt")
        try:
            root.title("记事本：" + os.path.basename(filePath))
            fopen = open(filePath, "r")
            read_things = fopen.read()
            text.delete(0.0, END)
            text.insert(0.0, read_things)
            fopen.close()
        except:
            messagebox.showinfo('打开错误', '打开 出现错误，请重试')

    open_command_root11 = tkinter.Tk()
    open_command_root11.title("是否打开")
    open_command11_l1 = Label(open_command_root11, text="打开文件后未保存的内容会被删除，是否继续新建")
    open_command11_l1.pack()
    open_command11_b1 = Button(open_command_root11, text="打开", command=open_a_new_window)
    open_command11_b1.pack()


def new_file():
    def make_a_new_window():
        global filePath
        text.delete(0.0, END)
        root.title(jishibenmingcheng)
        filePath = ""

    open_command_root = tkinter.Tk()
    open_command_root.title("是否保存")
    open_command_l1 = Label(open_command_root, text="新建文件后未保存的内容会被删除，是否继续新建")
    open_command_l1.pack()
    open_command_b1 = Button(open_command_root, text="新建", command=make_a_new_window)
    open_command_b1.pack()


def chongmingming():
    global chongmingmingtitle

    def new_name_file():
        global chongmingmingtitle
        chongmingmingtitle = "记事本：" + root_newname_e1.get() + ".txt"
        root.title(chongmingmingtitle)

    root_newname = tkinter.Tk()
    root_newname.title("重命名")
    root_newname_l1 = Label(root_newname, text="请输入新名称：")
    root_newname_l1.pack()
    root_newname_e1 = Entry(root_newname)
    root_newname_e1.pack()
    root_newname_b1 = Button(root_newname, text="确定", command=new_name_file)
    root_newname_b1.pack()


def tuichuxunwen():
    open_command_root = tkinter.Tk()
    open_command_root.title("是否退出")
    open_command_l1 = Label(open_command_root, text="新建文件后未保存的内容会被删除，是否继续退出")
    open_command_l1.pack()
    open_command_b1 = Button(open_command_root, text="退出", command=root.quit)
    open_command_b1.pack()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="重命名", accelerator="Ctrl Shift N", command=chongmingming)
filemenu.add_separator()
filemenu.add_command(label="新建", accelerator="Ctrl N", command=new_file)
filemenu.add_command(label="打开", accelerator="Ctrl O", command=open_command)
filemenu.add_command(label="保存", accelerator="Ctrl S", command=baocun)
filemenu.add_command(label="另存为", accelerator="Ctrl Shift S", command=lingcunwei)
filemenu.add_separator()
filemenu.add_command(label="退出", accelerator="Ctrl+Q", command=tuichuxunwen)
menubar.add_cascade(label="文件", menu=filemenu)
text = tk.Text(root, width=100, height=35, undo=True)
text.pack(expand=YES, fill=BOTH)

editmenu = Menu(menubar, tearoff=False)


def chexiao():
    text.event_generate("<<Undo>>")


def chongzuo():
    text.event_generate("<<Redo>>")


def jianqie():
    text.event_generate("<<Cut>>")


def fuzhi():
    text.event_generate("<<Copy>>")


def zhantie():
    text.event_generate("<<Paste>>")


def quanxuan():
    text.event_generate("<<SelectAll>>")


editmenu.add_command(label="撤销", accelerator="Ctrl Z", command=chexiao)
editmenu.add_command(label="重做", accelerator="Ctrl Y", command=chongzuo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl X", command=jianqie)
editmenu.add_command(label="复制", accelerator="Ctrl C", command=fuzhi)
editmenu.add_command(label="粘贴", accelerator="Ctrl V", command=zhantie)
editmenu.add_separator()
editmenu.add_command(label="全选", accelerator="Ctrl A", command=quanxuan)
menubar.add_cascade(label="编辑", menu=editmenu)
root.config(menu=menubar)

aboutmenu = Menu(menubar, tearoff=False)


def zuozhe():
    messagebox.showinfo('作者', 'zuozhe 1')


def banben():
    global banbenhao
    messagebox.showinfo('版本', banbenhao)


aboutmenu.add_command(label="作者", accelerator="Ctrl Shift MN", command=zuozhe)
aboutmenu.add_command(label="版本", accelerator="Ctrl Shift VC", command=banben)
menubar.add_cascade(label="关于", menu=aboutmenu)
root.config(menu=menubar)

# 结尾
mainloop()