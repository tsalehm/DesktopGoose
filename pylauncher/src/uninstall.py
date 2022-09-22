import winreg
import subprocess
from shutil import rmtree
from colorama import init, Fore
from installer import resource_path, runreg, startmenupath, goosepath


# info
init()
softreg = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'


# you sure?
print(Fore.LIGHTRED_EX + "\n\n\n\n\n\n\n      Hoooooonk! why do you want to uninstall the goose :_(\n\n\n"
      + Fore.MAGENTA + "      1)i'm an idiot\n      2)i'm an idiot\n      3)OK i'll keep the goose")

idiot = input()
if idiot == '1' or idiot == '2':
   print(Fore.LIGHTRED_EX + "\n\n      goodbye, idiot")
elif idiot == '3': quit()
else:
   print(Fore.LIGHTRED_EX + "\n\n      so you're not an idiot..."
         + "\n      goodbye, asswhore...")

subprocess.call(resource_path('closegoose.bat'), stdout=subprocess.DEVNULL)  # closw goose


# remove goose
rmtree(goosepath, True)
rmtree(startmenupath, True)

try:  # remove goose from registery
   with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, softreg, 0, winreg.KEY_ALL_ACCESS) as byekey:
      winreg.DeleteKeyEx(byekey, 'DesktopGoose')
except:
   pass

try:
   with winreg.OpenKey(winreg.HKEY_CURRENT_USER, runreg, 0, winreg.KEY_SET_VALUE) as byekey:
      winreg.DeleteValue(byekey, 'DesktopGoose')
except:
   pass

input(Fore.GREEN + "\n\n      the goose's got rid of you\n      press something and make me get rid of you too")
