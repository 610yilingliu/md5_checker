import hashlib
# filedialog have to be imported indiidually
from tkinter import filedialog
from multiprocessing import Process, Queue, Array, RLock
import os



def md5_check(filepath):
    md5_value = hashlib.md5()
    with open(filepath, 'rb') as f:
        while True:
            data_flow = f.read(1024*1024*500)
            if not data_flow:
                break
            md5_value.update(data_flow)
    f.close()
    out = md5_value.hexdigest()
    return out

def compare(md5_1, md5_2):
    if md5_1 == md5_2:
        return True
    return False

def select_path(path):
    p = filedialog.askopenfilename()
    path.set(p)


def print_md5(infile, label):
    md5 = md5_check(infile)
    label.config(text = "MD5值：" + md5)

def count_show(p1, p2, m1, m2, result_tag):
    if p1:
        print_md5(p1, m1)
    if p2:
        print_md5(p2,m2)
    if p1 and p2:
        compared = compare(m1["text"], m2["text"])
        if compared == False:
            result_tag.config(text = "文件MD5不一致")
        elif compared == True:
            result_tag.config(text = "文件MD5一致")
    elif (not p1) and (not p2):
        result_tag.config(text = "未选择文件")
    else:
        result_tag.config(text = "警告：只选择了一个文件")