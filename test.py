from pywinauto.application import Application

app = Application().start(cmd_line=u'"C://Users//YASH RAJ MANI//AppData//Local//Microsoft//Teams//current//Teams.exe"')
'''
app.MainWindow.Wait('ready')
vbapp = app.window_(title_re="General")
vbButton1 = ButtonWrapper(vbapp.Button.WrapperObject("Join")).Click

\
import pyautogui
import subprocess
import pendulum

pendulum.now()
current=pendulum.now().to_day_datetime_string()
print(current)
subprocess.call('C://Users//YASH RAJ MANI//AppData//Local//Microsoft//Teams//current//Teams.exe')
print("hey, THIS IS YASH ! ")
print("LOADING >>>>>>>>>>>>>>>>")

pyautogui.click('Join.png')
'''
