# coding=utf-8
from Tkinter import *
from upgrades import *


root = Tk()
score = Score()
pixel = PhotoImage(width=1, height=1)
root_width = 900
root_height = 600
hb_width = 274
hb_height = 46
upg_width = 274
upg_height = 70
pref_width = 46
pref_height = 46
head_buttons = []
upg_str = []
upg_buttons = []
upg_infostr = u'\nИмеется: %s\nЦена: %s волос\nУбирает: %s волос/сек (%s каждый)'
curscore_str = u'%d волос'
curspeed_str = u'%.1f волос/сек'
label_curscore = Label(font='arial 20')
label_curspeed = Label(font='arial 14')
hero_button = Button(command=score.click)


class HeadButton(Button):
    def __init__(self, text, image):
        Button.__init__(self, text=text, image=image, width=hb_width, height=hb_height, compound='c')

class UpgButton(Button):
    def __init__(self, text, image, command, id):
        Button.__init__(self, text=text, image=image, width=upg_width, height=upg_height, compound='c', command=command)
        self.myid = id


def window_deleted(root):
    print u'Окно закрыто'
    root.quit()  # явное указание на выход из программы

def format_bignum(number):
    # return str(number)
    i = 0
    final_str = ''
    for cym in reversed(str(number)):
        final_str += cym
        if (i == 2):
            final_str += ','
            i = 0
        else:
            i += 1
    if (final_str[len(final_str) - 1] == ','):
        return final_str[len(final_str) - 2::-1]
    return final_str[::-1]

def format_float_bignum(number):
    cur = '%.1f' % number
    return format_bignum(cur[:len(cur)-2]) + cur[len(cur)-2:len(cur)]

def upg_click_0():
    upg_click(0)
def upg_click_1():
    upg_click(1)
def upg_click_2():
    upg_click(2)
def upg_click_3():
    upg_click(3)
def upg_click_4():
    upg_click(4)
def upg_click_5():
    upg_click(5)
def upg_click_6():
    upg_click(6)

def upg_click(i):
    print i
    if (upgrades[i].price <= score.curscore):
        score.curscore -= upgrades[i].price
        score.curspeed -= upgrades[i].speed
        upgrades[i].buy(1)
        score.curspeed += upgrades[i].speed

dict_cmd = {i: lambda: upg_click(i) for i in range(7)}


def upg_update():
    for i in range(7):
        upg_buttons[i]['text'] = upgrades[i].name + upg_infostr % (format_bignum(upgrades[i].owned),
                                                                format_bignum(int(upgrades[i].price)),
                                                                format_float_bignum(upgrades[i].speed),
                                                                format_float_bignum(upgrades[i].baserate))
    root.after(100, upg_update)

def score_update():
    score.curscore += score.curspeed / 50.0
    # print score.curspeed / 1000.0
    # print score.curscore
    label_curscore['text'] = curscore_str % int(score.curscore)
    label_curspeed['text'] = curspeed_str % score.curspeed
    root.after(20, score_update)

def gui_build():
    # global head_buttons, upg_buttons, label_curscore, label_curspeed, hero_button
    head_str = [u'Улучшения', u'Магия', u'Достижения', u'Нстрйки']
    for i in range(3):
        head_buttons.append(HeadButton(head_str[i], pixel))
    head_buttons.append(Button(text=head_str[3], image=pixel, width=pref_width, height=pref_height, compound='c'))

    build_upgrades()
    for i in range(7):
        upg_str.append(upgrades[i].name + upg_infostr % (format_bignum(upgrades[i].owned),
                                                                format_bignum(int(upgrades[i].price)),
                                                                format_float_bignum(upgrades[i].speed),
                                                                format_float_bignum(upgrades[i].baserate)))
    for i in range(7):
        print globals()['upg_click_%d' % i]
        upg_buttons.append(UpgButton(upg_str[i], pixel, globals()['upg_click_%d' % i], i))

    label_curscore['text'] = curscore_str % (0)
    label_curspeed['text'] = curspeed_str % (0)

    hero_str = u'Герой\n\n(мааам, памагити...)'
    hero_button['text'] = hero_str

def gui_start(root):
    # global head_buttons, upg_buttons, label_curscore, label_curspeed, hero_button
    gui_build()
    root.title(u'Really Unruly Hair')
    screen_size = '%dx%d+%d+%d' % (root_width, root_height,
                                   (root.winfo_screenwidth() - root_width) // 2,
                                   (root.winfo_screenheight() - root_height) // 3)
    root.geometry(screen_size)
    root.resizable(False, False)
    root.protocol('WM_DELETE_WINDOW', window_deleted(root))  # обработчик закрытия окна

    for i in range(4):
        head_buttons[i].grid(row=0, column=i)
    for i in range(7):
        upg_buttons[i].grid(row=i+1, column=0)
    label_curscore.grid(row=1, column=1, columnspan=3, sticky='n', pady=16)
    label_curspeed.grid(row=1, column=1, columnspan=3, sticky='s', pady=0)
    hero_button.grid(row=2, column=1, rowspan=6, columnspan=3, ipadx=60, ipady=180)
    upg_update()
    score_update()
    root.mainloop()
