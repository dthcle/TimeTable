import tkinter as tk
import tkinter.messagebox as mess
import os
import datetime


def main():
    os.system("CLS")
    window = tk.Tk()
    window.title("TimeTable")
    window.geometry("1245x690")

    now = datetime.datetime.now()
    time_list = [now.year, now.month, now.day, now.weekday()]

    note = []
    try:
        with open('information', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                note.append(line)
    except:
        pass

    # print(len(note))
    while len(note) < 31:
            note.append('\n')

    # print(note)

    def click_it():
        temp = tk.Tk()
        temp.title("Input The Date")
        temp.grid()
        temp.geometry("200x90")
        tk.Label(temp,
                 text="Input The Date",
                 font=10).grid(row=0)
        info_text = tk.StringVar()
        info = tk.Entry(temp, textvariable=info_text)
        info.grid(row=1)

        def submit_the_date():
            tmp = int(info.get())
            temp.destroy()
            fun(tmp)

        tk.Button(temp,
                  text="Submit",
                  command=submit_the_date).grid(row=2)
        temp.mainloop()

    def fun(the_date):
        tmp = tk.Tk()
        tmp.title("Date: " + str(the_date))
        tmp.geometry("800x450")
        tk.Label(tmp,
                 text="New Or Edit The Activity:",
                 font=15).grid(row=0)
        information_text = tk.StringVar()
        string_of_it = note[the_date-1]
        information_text.set(string_of_it)
        # print(information_text.get())
        # print(string_of_it)
        information = tk.Entry(tmp, width=100, textvariable=information_text)
        information.grid(row=1)

        def submit():
            note[the_date-1] = information.get()
            # print(note[the_date-1])
            tmp.destroy()

        b = tk.Button(tmp,
                      text="Submit",
                      command=submit)
        b.grid(row=2)
        tmp.mainloop()

    def get_days(time_list):
        if time_list[1] != 2:
            if time_list[1] >= 8:
                if time_list[1] % 2 == 0:
                    return 31
                elif time_list[1] % 2 == 1:
                    return 30
            elif time_list[1] <= 7:
                if time_list[1] % 2 == 1:
                    return 31
                elif time_list[1] % 2 == 0:
                    return 30
        else:
            if time_list[0] % 4 == 0:
                if time_list[0] % 100 == 0:
                    if time_list[0] % 400 == 0:
                        return 29
                    else:
                        return 28
                return 29
            else:
                return 28

    weekday_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(7):
        tk.Label(window,
                 text=weekday_list[i],
                 font=25).grid(row=0, column=i)

    button_list = []
    for i in range(time_list[2], get_days(time_list) + 1):
        b = tk.Button(window,
                      text=(str(i)+'\n'+note[i-1]),
                      width=24, height=5,
                      command=lambda: click_it())
        button_list.append(b)

    a = 1
    for i in range(1, time_list[2]):
        b = tk.Button(window,
                      text=(str(i)+'\n'+note[i-1]),
                      width=24, height=5,
                      command=lambda: click_it())
        button_list.append(b)
        a = i

    flag = 0
    try:
        with open('log', 'r') as f:
            line = f.readline()
            if line != ('\t' + str(time_list[0]) + '年' + str(time_list[1]) + '月' + str(time_list[2]) + '日星期' + str(time_list[3]+1) + ':\n'):
                # print(line)
                flag = 1
    except:
        with open('log', 'w'):
            pass

    with open('log', 'a+') as f:
        if flag == 1:
            f.write('\t' + str(time_list[0]) + '年' + str(time_list[1]) + '月' + str(time_list[2]) + '日星期' + str(time_list[3]+1) + ':\n' + note[a])
            note[a] = '\n'

    tmp = time_list[3] + 1
    for i in button_list:
        i.grid(row=1+tmp//7, column=tmp % 7)
        tmp = tmp+1

    mess.showinfo(title="注意", message='若要查看修改后的计划表，请重新打开本程序！')

    window.mainloop()
    # print(note)

    with open("information", 'w') as f:
        for i in note:
            f.write(i)
            if i[-1] != '\n':
                f.write('\n')

if __name__ == "__main__":
    main()
