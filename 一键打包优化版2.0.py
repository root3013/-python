import tkinter as tk
window=tk.Tk()
window.geometry('800x600')
window.title('Py一键打包 by:wzl')
##################################
global var1
global var2
global var3
flag1=0
flag2=0
flag3=0
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
commd='pyinstall'
##################################
def def_button_1():
    hidetext.delete(1.0, tk.END)
    box=['0','0','0']
    box[0]=flag1
    box[1]=flag2
    box[2]=flag3
    commd_0='pyinstaller'
    commd_1='-F'
    commd_2='-w'
    commd_3='-i'
    if box[0] and box[1] and box[2]:
        hidetext.insert('insert',f"{commd_0} {commd_1} {commd_2} {commd_3} ")
    elif box[0] and box[1]:
        hidetext.insert('insert',f"{commd_0} {commd_2} {commd_3} ")
    elif box[0] and box[1] and box[2]:
        hidetext.insert('insert',f"{commd_0} {commd_1} {commd_2} {commd_3} ")



def box1():
    global flag1
    if var1.get():
        flag1=1
    else:
        flag1=0
def box2():
    global flag2
    if var2.get():
        flag2=1
    else:
        flag2=0
def box3():
    global flag3
    if var3.get():
        flag3=1
    else:
        flag3=0
##################################
hidetext=tk.Text(window,height=1)
hidetext.insert('insert',commd)
check_1=tk.Checkbutton(window,text='功能一',variable=var1,command=box1)
check_2=tk.Checkbutton(window,text='功能二',variable=var2,command=box2)
check_3=tk.Checkbutton(window,text='功能三',variable=var3,command=box3)
button_1=tk.Button(window,text='test',command=def_button_1)
##################################
check_1.pack()
check_2.pack()
check_3.pack()
button_1.pack()
hidetext.pack()
window.mainloop()