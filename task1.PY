# /////////////////////////////////////////////////////////

# Name: Marcel Ciszewski
# Class: 10Y-CS
# Task: NEA_MOCK_ASSESSMENT_TASK_1

# /////////////////////////////////////////////////////////
import os
import time
import sys
from os import system, name
from time import sleep
import subprocess
import sys
import pip
import platform
from datetime import datetime
import socket
import uuid
import re
# /////////////////////////////////////////////////////////
subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'pip'])

try:
    import readchar
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'readchar'])
finally:
    import readchar
from readchar import readkey, key

try:
    import psutil
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'psutil'])
finally:
    import psutil

try:
    import py_cpuinfo
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'py_cpuinfo'])
finally:
    import cpuinfo

# define what system info is

def System_information():
    print("="*40, "Your System Information", "="*40)
    uname = platform.uname()
    print(f"System OS: {uname.system}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"IP-Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"MAC-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")
    print("="*100)


# /////////////////////////////////////////////////////////
# experiment and check if readkey is present and installed using the above subprocess
print(" ")
print("Press Enter to continue.")
while True:
    k = readkey()
    if k == key.ENTER:
        break
    else:
        exit()
# ========================================================
# define what clear is and base it on the os you are using
def clear():
 
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')
# ========================================================
clear()
accept1 = False
device = False
correction = False
print("Please do not run this through IDLE as it won't be the best experience.")
# ========================================================
# greetings and simple response to get name and explain purpose.
print("Welcome to this automated response prompt!")
print("Using a series of question, we'll attempt to resolve your current situation and problem.")
print("Please key in your name to proceed.")
name1 = input()
time.sleep(3)
clear()
# ========================================================
# giant while loop to allow the user if there was a mistype
print("Welcome" ,name1)
while True:
    while correction == False:
        System_information()
        print(" ")
        print("//////////////////////////////////////////////////////////////////////////////////")
        print("For COMPUTERS, if this is the device you are currently experiencing on,")
        print("Use the above system information to help you. If not, ignore, and select an option")
        print("that you have.")
        print("//////////////////////////////////////////////////////////////////////////////////")
        print("For CONSOLES, choose the one that you have.")
        print("//////////////////////////////////////////////////////////////////////////////////")
        time.sleep(15)
        clear()
        print("===============================")
        print("1 for Phone (Mobile Devices)")
        print("2 for Computers")
        print("3 for Consoles")
        print("==============================")
        accept1 = False
        num = None
        while accept1 == False:
            try:
                print("Using the above, press the number you would like to resolve: ")
                num = int(readkey())
                accept1 = True
            except ValueError:
                print("Invalid input. Enter a number.")
        num = str(num)
        if num == "1":
            print("You have an issue with your mobile device. Is this correct?")
            option1 = input()
            if option1 == "yes" or option1 == "Yes":
                print("Great. I'll pull up the troubleshooting questions now.")
                correction = True
                eg = 1
            else:
                print("")
                clear()
        if num == "2":
            print("You have an issue with your computer. Is this correct?")
            option1 = input()
            if option1 == 'yes' or option1 == 'Yes':
                print("Great. I'll pull up the troubleshooting questions now.")
                correction = True
                eg = 2
            else:
                print("")
                clear()
        if num == "3":
            print("You have an issue with your console. Is this correct?")
            option1 = input()
            if option1 == 'yes' or option1 == 'Yes':
                print("Great. I'll pull up the troubleshooting questions now.")
                correction = True
                eg = 3 
            else:
                print("")
                clear()
        else:
            print("Try again.")
            clear()
    break
# ========================================================
# phone problems hence eg = 1, also while looped if there is a mistake, based on previous code.
num = None
resolved = False
if eg == 1:
    while resolved == False:
        clear()
        print("Here are fourteen very common problems with mobile devices. Type the number")
        print("of the problem you are currently experiencing.")
        print("==========================================================================")
        print(" #1 - Your phone is quite slow to open apps.")
        print(" #2 - Your phone is experiencing bad battery life.")
        print(" #3 - Your phone is overheating rapidly.")
        print(" #4 - Your phone cannot store anymore apps / photos.")
        print(" #5 - Your phone's apps freeze randomly and/or stop working completely.")
        print(" #6 - Your phone freezes (even on the home screen) or crashes.")
        print(" #7 - Your phone's app store is not downloading apps at all.")
        print(" #8 - Your phone's MicroSD card is not showing up / not storing anything.")
        print(" #9 - Your phone has gotten wet (in any degree).")
        print(" #a - Your phone has a damaged charging port.")
        print(" #b - Your phone's connected accounts cannot synchronise.")
        print(" #c - Your phone's screen is not bright enough.")
        print(" #d - Your phone cannot connect to the app store.")
        print(" #e - Your phone cannot connect to WiFi (intermittent or not showing up).")
        print("==========================================================================")
        print("Enter the number.")
        num = None
        accept1 = False
        accept2 = False
        while accept1 == False:
            try:
                print("Using the above, press the number or letter you would'd like to resolve: ")
                num = readkey()
                accept1 = True
            except ValueError:
                print("Invalid input. Enter a number.")
        num = str(num)
        if num == "1":
            print("=====================================================================================================")
            print("If your phone is slow to opening apps, try closing previous apps or uninstalling unused ones to help.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "2":
            print("=====================================================================================================")
            print("To improve bad battery life, adjust screen brightness, disable unnecessary background processes,")
            print("and close unused apps. Consider replacing the battery if the issue persists.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "3":
            print("=====================================================================================================")
            print("If your phone is overheating rapidly, try closing resource-intensive apps, keeping it in a cool environment,")
            print("and removing any phone cases that may be trapping heat. If the problem persists, consult the manufacturer or a technician.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "4":
            print("=====================================================================================================")
            print("When your phone cannot store more apps/photos, delete unnecessary files, transfer media to ")
            print("external storage, and consider upgrading to a device with larger internal storage.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "5":
            print("=====================================================================================================")
            print("Address random app freezes by updating apps and your phone's software,")
            print("clearing app caches, and restarting your device regularly.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "6":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "6":
            print("=====================================================================================================")
            print("If your phone freezes or crashes, troubleshoot by uninstalling problematic apps, ")
            print("updating software, and performing a factory reset as a last resort.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "7":
            print("=====================================================================================================")
            print("When the app store won't download apps, check your internet connection,") 
            print("clear app store cache, and ensure there's sufficient storage space.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "9":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "8":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "9":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "a":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "b":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "c":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "d":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "e":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
# ===================================================================================================================================
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ PHONES ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ COMPUTERS \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# ===================================================================================================================================
if eg == 2:
    while resolved == False:
        clear()
        print("Here are fourteen very common problems with mobile devices. Type the number")
        print("of the problem you are currently experiencing.")
        print("==========================================================================")
        print(" #1 - Your phone is quite slow to open apps.")
        print(" #2 - Your phone is experiencing bad battery life.")
        print(" #3 - Your phone is overheating rapidly.")
        print(" #4 - Your phone cannot store anymore apps / photos.")
        print(" #5 - Your phone's apps freeze randomly and/or stop working completely.")
        print(" #6 - Your phone freezes (even on the home screen) or crashes.")
        print(" #7 - Your phone's app store is not downloading apps at all.")
        print(" #8 - Your phone's MicroSD card is not showing up / not storing anything.")
        print(" #9 - Your phone has gotten wet (in any degree).")
        print(" #a - Your phone has a damaged charging port.")
        print(" #b - Your phone's connected accounts cannot synchronise.")
        print(" #c - Your phone's screen is not bright enough.")
        print(" #d - Your phone cannot connect to the app store.")
        print(" #e - Your phone cannot connect to WiFi (intermittent or not showing up).")
        print("==========================================================================")
        print("Enter the number.")
        num = None
        accept1 = False
        accept2 = False
        while accept1 == False:
            try:
                print("Using the above, press the number or letter you would'd like to resolve: ")
                num = readkey()
                accept1 = True
            except ValueError:
                print("Invalid input. Enter a number.")
        num = str(num)
        if num == "1":
            print("=====================================================================================================")
            print("If your phone is slow to opening apps, try closing previous apps or uninstalling unused ones to help.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "2":
            print("=====================================================================================================")
            print("To improve bad battery life, adjust screen brightness, disable unnecessary background processes,")
            print("and close unused apps. Consider replacing the battery if the issue persists.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "3":
            print("=====================================================================================================")
            print("If your phone is overheating rapidly, try closing resource-intensive apps, keeping it in a cool environment,")
            print("and removing any phone cases that may be trapping heat. If the problem persists, consult the manufacturer or a technician.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "4":
            print("=====================================================================================================")
            print("When your phone cannot store more apps/photos, delete unnecessary files, transfer media to ")
            print("external storage, and consider upgrading to a device with larger internal storage.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "5":
            print("=====================================================================================================")
            print("Address random app freezes by updating apps and your phone's software,")
            print("clearing app caches, and restarting your device regularly.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "6":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "6":
            print("=====================================================================================================")
            print("If your phone freezes or crashes, troubleshoot by uninstalling problematic apps, ")
            print("updating software, and performing a factory reset as a last resort.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "7":
            print("=====================================================================================================")
            print("When the app store won't download apps, check your internet connection,") 
            print("clear app store cache, and ensure there's sufficient storage space.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "9":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "8":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "9":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "a":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "b":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "c":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "d":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "e":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
# ==============================================================================================================================================
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ COMPUTERS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ CONSOLES \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# ==============================================================================================================================================
if eg == 3:
    while resolved == False:
        clear()
        print("Here are fourteen very common problems with mobile devices. Type the number")
        print("of the problem you are currently experiencing.")
        print("==========================================================================")
        print(" #1 - Your phone is quite slow to open apps.")
        print(" #2 - Your phone is experiencing bad battery life.")
        print(" #3 - Your phone is overheating rapidly.")
        print(" #4 - Your phone cannot store anymore apps / photos.")
        print(" #5 - Your phone's apps freeze randomly and/or stop working completely.")
        print(" #6 - Your phone freezes (even on the home screen) or crashes.")
        print(" #7 - Your phone's app store is not downloading apps at all.")
        print(" #8 - Your phone's MicroSD card is not showing up / not storing anything.")
        print(" #9 - Your phone has gotten wet (in any degree).")
        print(" #a - Your phone has a damaged charging port.")
        print(" #b - Your phone's connected accounts cannot synchronise.")
        print(" #c - Your phone's screen is not bright enough.")
        print(" #d - Your phone cannot connect to the app store.")
        print(" #e - Your phone cannot connect to WiFi (intermittent or not showing up).")
        print("==========================================================================")
        print("Enter the number.")
        num = None
        accept1 = False
        accept2 = False
        while accept1 == False:
            try:
                print("Using the above, press the number or letter you would'd like to resolve: ")
                num = readkey()
                accept1 = True
            except ValueError:
                print("Invalid input. Enter a number.")
        num = str(num)
        if num == "1":
            print("=====================================================================================================")
            print("If your phone is slow to opening apps, try closing previous apps or uninstalling unused ones to help.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "2":
            print("=====================================================================================================")
            print("To improve bad battery life, adjust screen brightness, disable unnecessary background processes,")
            print("and close unused apps. Consider replacing the battery if the issue persists.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "3":
            print("=====================================================================================================")
            print("If your phone is overheating rapidly, try closing resource-intensive apps, keeping it in a cool environment,")
            print("and removing any phone cases that may be trapping heat. If the problem persists, consult the manufacturer or a technician.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "4":
            print("=====================================================================================================")
            print("When your phone cannot store more apps/photos, delete unnecessary files, transfer media to ")
            print("external storage, and consider upgrading to a device with larger internal storage.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "5":
            print("=====================================================================================================")
            print("Address random app freezes by updating apps and your phone's software,")
            print("clearing app caches, and restarting your device regularly.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "6":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "6":
            print("=====================================================================================================")
            print("If your phone freezes or crashes, troubleshoot by uninstalling problematic apps, ")
            print("updating software, and performing a factory reset as a last resort.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "7":
            print("=====================================================================================================")
            print("When the app store won't download apps, check your internet connection,") 
            print("clear app store cache, and ensure there's sufficient storage space.")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "9":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "8":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "9":
            print("=====================================================================================================")
            print("")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "a":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "b":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "c":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "d":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
        if num == "e":
            print("=====================================================================================================")
            print("ez")
            print("=====================================================================================================")
            while accept2 == False:
                try:
                    print("Did this help? Press 1 for yes (therefore exit) or 2 for no (want to continue resolving the issue.)")
                    num1 = int(readkey())
                    accept2 = True
                except ValueError:
                    print("Invalid input. Enter a number.")
            num1 = str(num1)
            if num1 == "1":
                print("Alright, thank you for using the program!")
                exit()
            if num1 == "2":
                print("Taking back to main menu.")
            else:
                print("InvaLid response. Assuming you want to exit.")
                exit()
else:
    print("No valid option has been selected. Assuming you would like to quit.")
    quit()


        
        
    




