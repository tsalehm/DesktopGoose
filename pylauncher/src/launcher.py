import re
import time 
import pyvda
import win32gui
import subprocess

close_signal=False
#defines
goosepath="F:/Downloads/Programs/DesktopGoose v0.3/GooseDesktop.exe"

#get apps hwnd
def getShell(): 
   thelist = []
   def findit(hwnd,ctx):
         thelist.append(hwnd)
   win32gui.EnumWindows(findit,None)
   return thelist

# open goose and find its hwnd
first_hd=getShell()
subprocess.Popen(goosepath) 
time.sleep(2) #wait for goose to fully open
sec_hd=getShell()
dif_hd = [element for element in sec_hd if element not in first_hd]

#pin goose to all desktops
for honk in dif_hd: 

   try:
      if win32gui.GetWindowText(honk)=='': #goose's main process is named ''
         tsk=pyvda.AppView(hwnd=honk)
         tsk.pin()
   except Exception: # if a process with name '' cannot get pinned
      pass


#look for goose's memes and pin them untill the app gets closed
while not close_signal:
   memeshell=getShell()
   for meme in memeshell :
   
      if re.search(r"Goose|^$",win32gui.GetWindowText(meme)) and meme>0:  #memes are names with 'goose not-epad' and ''
         
         try :
            memeobj=pyvda.AppView(hwnd=meme)
            if not memeobj.is_pinned() : memeobj.pin()
         except Exception: # if a process with name '' cannot get pinned
            pass 

   time.sleep(1)


