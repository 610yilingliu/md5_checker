from tkinter import *
import logic


window = Tk()
window.title('百度网盘防翻车工具')
# init path string
path_1 = StringVar()
path_2 = StringVar()

# init window
# objects have to be initualized before applying bind method, see https://blog.csdn.net/weixin_41004763/article/details/89600748
# first file
Label(window, text = "文件1").grid(row = 0, column = 0)
e1 = Entry(window, textvariable = path_1)
e1.grid(row = 0, column = 1)
bt_f1 = Button(window, text = "选择路径", command = lambda: logic.select_path(path = path_1))
bt_f1.grid(row = 0, column = 2)
# second file
Label(window, text = "文件2").grid(row = 1, column = 0)
e2 = Entry(window, textvariable = path_2)
e2.grid(row = 1, column = 1)
bt_f2 = Button(window, text = "选择路径", command = lambda:logic.select_path(path = path_2))
bt_f2.grid(row = 1, column = 2)
# label to show md5
md5_1 = Label(window, text = "")
md5_1.grid(row = 3)
md5_2 = Label(window, text = "")
md5_2.grid(row = 4)
# print result
result = Label(window, text = "")
result.grid(row = 5)
# count button
bt_count = Button(window,text = "计算并比较文件MD5值", command = lambda: logic.count_show(p1 = path_1.get(), p2 = path_2.get(), m1 = md5_1, m2 = md5_2, result_tag = result))
bt_count.grid(row = 2)

    
window.mainloop()