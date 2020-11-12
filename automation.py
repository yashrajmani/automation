import pyautogui
import time 


import pendulum
from pywinauto.application import Application

app = Application().start(cmd_line=u'"C://Users//YASH RAJ MANI//AppData//Local//Microsoft//Teams//current//Teams.exe"')



pendulum.now()
current=pendulum.now().to_day_datetime_string()
print(current)
time.sleep(7)
'''
subprocess.call('C://Users//YASH RAJ MANI//AppData//Local//Microsoft//Teams//current//Teams.exe')
print("hey, THIS IS YASH ! ")
print("LOADING >>>>>>>>>>>>>>>>")
'''

#MYTIMETABLE:
#maths th join done!


############## MONDAY ###########################
if "Mon" in current:
    if "8:" in current:
        print("EEE1001")
        pyautogui.click(271,622)
        print("EEE th ")
        pyautogui.click('Join now')
    elif "9:" in current:
        print("STS1201")
        pyautogui.click(1717,304)
        print("STS")
    elif "10:" in current:
        print("HUM1021")
        pyautogui.click(1002,322)
        print("ethics")

    elif "12:" in current:
        print("MAT1011")
        pyautogui.click(999,595)                    ##############check this if its working #####################
        print("MAT th")
        time.sleep(3)
        pyautogui.click(732,589)
        
    elif "5:" in current:
        print("CSE1001 L")
        pyautogui.click(297,297)
        print("cse l")
    else:
        print("NEXT")
        pyautogui.alert('         NO CLASS!         ')

############## TUESDAY ####################
elif "Tue" in current:
    if "9:" in current:
        print("MAT1011")
        pyautogui.click(999,595) 
        print("MAT th")
        time.sleep(3)
        pyautogui.click(732,589)                               ##############check this if its working #####################
        
    elif "10:" in current:
        print("PHY1701")
        pyautogui.click(1694,632)
        print("phy th")
    elif "11:" in current:
        print("CHY1002")
        pyautogui.click(1364,325)
        print("EVS")
    elif "4:" in current:
        print("ENG1902 L")
        pyautogui.click(641,317)
        print("ENGLISH l")
    elif "5:" in current:
        print("EEE1001 L")
        pyautogui.click(640,604)
        print("EEE l")
    else:
        print("NEXT")
        pyautogui.alert('         NO CLASS!         ')
########### WEDNESDAY #############################
elif "Wed" in current:
    if "8:" in current:
        print("CHY1002")
        pyautogui.click(1364,325)
        print("EVS")
    elif "9:" in current:
        print("EEE1001")
        pyautogui.click(271,622)
        print("EEE th ")
    elif "10:" in current:
        print("STS1201")
        pyautogui.click(1717,304)
        print("STS")
    elif "2:" in current:
        print("CSE1001 L")
        pyautogui.click(297,297)
        print("cse l")
    elif "4:" in current:
        print("PHY1701 L")
        pyautogui.click(265,902)
        print("phy l")
    else:
        print("NEXT")
        pyautogui.alert('         NO CLASS!         ')
############ THURSDAY ########################
elif "Thu" in current:
    if "8:" in current:
        print("HUM1021")
        pyautogui.click(1002,322)
        print("ethics")
    elif "10:" in current:
        print("MAT1011")
        pyautogui.click(999,595)
        print("MAT th")
        time.sleep(3)
        pyautogui.click(732,589)                               ##############check this if its working #####################

    elif "11:" in current:
        print("PHY1701")
        pyautogui.click(1694,632)
        print("phy th")
    elif "4:" in current:
        print("ENG1902 L")
        pyautogui.click(641,317)
        print("ENGLISH l")
    else:
        print("NEXT")
        pyautogui.alert('         NO CLASS!         ')
############### FRIDAY #####################
elif "Fri" in current:
    if "8:" in current:
        print("PHY1701")
        pyautogui.click(1694,632)
        print("phy th")
    elif "9:" in current:
        print("CHY1002")
        pyautogui.click(1364,325)
        print("EVS")
    elif "11:" in current:
        print("STS1201")
        pyautogui.click(1717,304)
        print("STS")
    elif "2:" in current:
        print("MAT1011 L")
        pyautogui.click(1353,624)
        print("MAT l")
    elif "4:" in current:
        print("CSE1001 L")
        pyautogui.click(297,297)
        print("cse l")
    else:
        print("NEXT")
        pyautogui.alert('         NO CLASS!         ')
#######################################################
else:
    print("HOLIDAY !")
    time.sleep(7) 
    pyautogui.click(1889,24)
    print('EXIT>>>>>>>>>')
    
    pyautogui.alert('Today is a HOLIDAY,PEACE OUT !' "\n"
                    "Closing TEAMS ! ")




