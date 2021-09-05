import blynklib #библиотека Blynk (перед этим в CMD сделать pip install blynklib)
import subprocess #библиотека для запуска параллельных процессов
import webbrowser #библиотека для работы с веб
import pyautogui #библиотека для эмуляции нажатий клавиш клавиатуры (перед этим в CMD сделать pip install pyautogui)
import ctypes 
import config
import subprocess
#import keyboard

BLYNK_AUTH = 'rJ8UsbSsxKcFnGBrhnCums5clai_FhRL' #вставить токен

blynk = blynklib.Blynk(BLYNK_AUTH)


#функция для запуска отдельным процессом приложений и команд
def startcmd(cmd):
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell = True)
    p.poll();


def keyswork(pinname):
    print ('Сочетание клавиш')
    if len(pinname)==2:
        pyautogui.hotkey(pinname[1])
    elif len(pinname)==3:
        pyautogui.hotkey(pinname[1],pinname[2])
    elif len(pinname)==4:
        pyautogui.hotkey(pinname[1],pinname[2],pinname[3])
    elif len(pinname)==5:
        pyautogui.hotkey(pinname[1],pinname[2],pinname[3],pinname[4])
    elif len(pinname)==6:
        pyautogui.hotkey(pinname[1],pinname[2],pinname[3],pinname[4],pinname[5])
    else:
        pass

def clean_symb (text):
            if not isinstance(text, str):
                raise TypeError('Это не текст')
            for i in [' ','[',']','\"','\'']:
                text = text.replace(i,'')
            return text 

def workwithpin (pinname):
    if pinname[1] == "None":
        ctypes.windll.user32.MessageBoxW(0, "Не указаны параметры для виртуального пина в config.py!", "Blynk Controller by Xottabb14", 0)
    else:
        pinV = pinname[1]
        if pinname[0] == 0:
            print ("Значение: "+pinV) 
            startcmd(pinV)
            print ('открываю '+pinV)
        elif pinname[0] == 1:
            print ("Значение: "+pinV)
            webbrowser.open(pinV)
            print ('открываю сайт '+pinV)
        elif pinname[0] == 2:
            keyswork(pinname)
        else:
            pass
def flask_request_run_alisa():
	ngrokFile = "/home/pin/Downloads"
	s_4 = subprocess.Popen(["gnome-terminal -- bash -c \
	'cd /home/pin/SkillAlisa/skill-alisa; export FLASK_APP=app.py;python3 -m flask run --port=4000; exec bash;'"],shell=True)
	s_1 = subprocess.Popen(["/home/pin/Downloads/ngrok", 
	"http", "4000"])
	
#	s_4 = subprocess.Popen(["cd /home/pin/SkillAlisa/skill-alisa && gnome-terminal && export FLASK_APP=app.py && python3 -m flask run --port=80"], shell=True)
#	s_4 = subprocess.Popen(["gnome-terminal -- bash -c 'cd /home/pin/SkillAlisa/skill-alisa;exec bash' "],shell=True )
#	s_2 = subprocess.run(["export FLASK_APP=/home/pin/SkillAlisa/skill-alisa/app.py"],shell=True)
#	s_3 = subprocess.Popen(["python3", "-m", "flask", "run", "--port=80"])
	#gnome-terminal
#	print("func")
#	subprocess.call(["cd", ngrokFile])
#	print("func_1")

@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
#	print("{} {}".format(pin,value))
	if str(value) == "['1']":
#		print("Next1")
#		flask_request_run_alisa()
#		print("Next")
		app="/opt/google/chrome/google-chrome"
		subprocess.Popen(app)
		flask_request_run_alisa()
#		startcmd(app)
		print('open' + app)

#---------------------Начало блока функций для виртуальных пинов blynk-----------------
@blynk.handle_event('write V1') #данный пин используем для управления общей громкостью ПК
def write_virtual_pin_handler(pin, value):
    valuepin = clean_symb (str(value))
    volset = (65535/100)*int(valuepin) #в nircmd 65535 уровней громкость, маппим их на наши 100%
    nirpath = config.curpath+"\\nircmd.exe setsysvolume "+str(volset)
    startcmd(nirpath)
    print ("Громкость: "+str(valuepin)+" %")

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V1
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V2
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V3
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V4
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V5
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V6')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V6
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V7')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V7
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V8')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V8
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V9')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V9
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V10')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V10
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V11')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V11
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)


@blynk.handle_event('write V12')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V12
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V13')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V13
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V14')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V14
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V15')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V15
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V16')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V16
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V17')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V17
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V18')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V18
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V19')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V19
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V20')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V20
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V21')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V21
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V22')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V22
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V23')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V23
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V24')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V24
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V25')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V25
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V26')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V26
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V27')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V27
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V28')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V28
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V29')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V29
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V30')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V30
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V31')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V31
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V32')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V32
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V33')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V33
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V34')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V34
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V35')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V35
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)


@blynk.handle_event('write V36')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V36
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V37')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V37
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V38')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V38
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V39')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V39
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V40')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V40
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V41')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V41
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V42')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V42
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V43')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V43
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V44')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V44
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V45')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V45
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V46')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V46
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V47')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V47
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V48')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V48
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)
@blynk.handle_event('write V49')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V49
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

@blynk.handle_event('write V50')
def write_virtual_pin_handler(pin, value):
    valuepin = str(value)[2:3]
    pinname = config.V50
    if valuepin == "1":
        workwithpin(pinname)
    elif valuepin == "0":
        print ("Выключено")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Формат данного виртуального пина указан неверно в приложении Blynk.", "Blynk Controller by Xottabb14", 0)

#---------------------Конец блока функций для виртуальных пинов blynk-----------------

while True:
    blynk.run()

    
