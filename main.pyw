import os
import sys
from tkinter import ttk, StringVar
from tkinter import messagebox
#pip install --user fonttools
#from fontTools.ttLib import TTFont

import functions.json_ops
import functions.calculate


def set_project_root():
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_file))))
    
    os.chdir(project_root)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    return project_root
project_root = set_project_root()



path=os.path.dirname(os.path.abspath(__file__))





import ctypes
my_app_id = 'minecraft_builder_calc'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass
try:
    sc = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    sc=sc/100
except Exception as e:
    print(f"Unable to get system scaling! {e}")


def scaled(x):
    global sc
    fx=str(int(x*sc))
    return fx
#custom_font="Segoe "+scaled(12)
sys_font="Courier "+scaled(10)


#############################################################################################################################################

#font = TTFont(path+'\\assets\\mc_lang_font.ttf')
#font.save("C:\\Windows\\Fonts\\Minecraft Rus Regular")
save_=functions.json_ops.get_save(path)

if save_:
    lconfig=functions.json_ops.get_conf(path)
else:
    functions.json_ops.to_default(path)
    lconfig=functions.json_ops.get_conf(path)


def conf():
    os.system(path+"\\config\\code.json")



def how():
    messagebox.showinfo("How to read in Stacks", "i - items\ns - stacks\nc - chests\ndc - double chests")

from tkinter import *

window = Tk()
window.title("Minecraft Builder Calc")
window.geometry(scaled(350)+"x"+scaled(200))
window.resizable(False, False)
window.iconbitmap(path+"\\assets\\icon.ico")


from tkinter import font
custom_font = font.Font(family="Minecraft Rus Regular", size=int(scaled(10)))
custom_font_small = font.Font(family="Minecraft Rus Regular", size=int(scaled(8)))
style = ttk.Style()
style.configure("Custom.TCheckbutton", font=custom_font_small)
style.configure("Custom.TButton", font=custom_font_small)
style.configure("Custom.TLabel", font=custom_font_small)
style.configure("Custom.TCombobox", font=custom_font)

main_menu = Menu()

settings_menu=Menu()

settings_menu.add_command(label="How to read in Stacks?", command=how)
settings_menu.add_command(label="Advanced Config", command=conf)

main_menu.add_cascade(label="Settings", menu=settings_menu)


window.config(menu=main_menu)

lbl_tr = Label(window, text = "To translate:", font=custom_font)
lbl_tr.place(x=0, y=scaled(4))

def reset_():
    ent_1.delete(0, 'end')
    calc()
    cb1.set("blocks")
    cb2.set("blocks")

btn_reset = ttk.Button(window, text = "reset", command=reset_, width=0, style="Custom.TButton")
btn_reset.place(x=scaled(137), y=scaled(4))

def calc(Event=None):
    txt.set(functions.calculate.calc(functions.calculate.calc_to_int(ent_1.get()),cb1.get(),cb2.get(),path))
    print(f"txt.set(functions.calculate.calc({functions.calculate.calc_to_int(ent_1.get())}, {cb1.get()}, {cb2.get()}, {path}))")
    n=functions.calculate.calc(functions.calculate.calc_to_int(ent_1.get()),cb1.get(),cb2.get(),path)
    print(f"{n}!!!")

    functions.json_ops.change_conf(path,6,functions.calculate.calc_to_int(ent_def.get()))
    functions.json_ops.change_conf(path,4,cb1.get())
    functions.json_ops.change_conf(path,5,cb2.get())
window.bind('<Enter>', calc)


ent_def= StringVar(value=lconfig[6])
ent_1 = ttk.Entry(window, width=int(scaled(11)), textvariable=ent_def, font=custom_font_small)
ent_1.place(x=scaled(0), y=scaled(30))
ent_1.bind('<KeyRelease>', calc)
ent_1.bind('<Enter>', calc)


lbl_eq = Label(window, text = "=", font=custom_font)
lbl_eq.place(x=scaled(155), y=scaled(30))


txt= StringVar()

ent_2 = ttk.Entry(window, width=int(scaled(11)), state='readonly', textvariable=txt, font=custom_font_small)
ent_2.place(x=scaled(190), y=scaled(30))


a = functions.json_ops.get_names(path)
var = StringVar()
cb1 = ttk.Combobox(window, values=a, width=int(scaled(9)), postcommand=calc, font=custom_font_small)
cb1.set(lconfig[4])
cb1.place(x=scaled(4), y=scaled(49))
cb1.bind('<Enter>', calc)

cb2 = ttk.Combobox(window, values=a, width=int(scaled(9)), postcommand=calc, font=custom_font_small)
cb2.set(lconfig[5])
cb2.place(x=scaled(190), y=scaled(49))
cb2.bind('<Enter>', calc)

def checkbutton_changed():
    if enabled_logs.get() == 1:
        functions.json_ops.change_conf(path,0,True)
    else:
        functions.json_ops.change_conf(path,0,False)

    if enabled_stack.get() == 1:
        functions.json_ops.change_conf(path,1,True)
    else:
        functions.json_ops.change_conf(path,1,False)

    if enabled_rnd.get() == 1:
        functions.json_ops.change_conf(path,2,True)
    else:
        functions.json_ops.change_conf(path,2,False)

    if enabled_save.get() == 1:
        functions.json_ops.change_conf(path,3,True)
    else:
        functions.json_ops.change_conf(path,3,False)
    calc()


enabled_logs = IntVar(value=lconfig[0])
chb_logs = ttk.Checkbutton(window, text="In logs", variable=enabled_logs, command=checkbutton_changed, style="Custom.TCheckbutton")
chb_logs.place(x=0, y=scaled(75))

enabled_stack = IntVar(value=lconfig[1])
chb_stack = ttk.Checkbutton(window, text="Stack items", variable=enabled_stack, command=checkbutton_changed, style="Custom.TCheckbutton")
chb_stack.place(x=0, y=scaled(100))

enabled_rnd = IntVar(value=lconfig[2])
chb_rnd = ttk.Checkbutton(window, text="Do not round", variable=enabled_rnd, command=checkbutton_changed, style="Custom.TCheckbutton")
chb_rnd.place(x=0, y=scaled(125))

enabled_save = IntVar(value=lconfig[3])
chb_save = ttk.Checkbutton(window, text="Always save values", variable=enabled_save, command=checkbutton_changed, style="Custom.TCheckbutton")
chb_save.place(x=0, y=scaled(150))


window.mainloop()