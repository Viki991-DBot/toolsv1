#required
from colored import bg, fg
import os
import time

#color list
color = fg("green")
color2 = fg("red")
color3 = fg("cyan")
color4 = fg("yellow")
color5 = fg("blue")
rescolor = fg("white")


#start making the tools can run
print("Installing Some Data!")
time.sleep(2)
os.system("pkg install colored")
time.sleep(2)
print("Data installed!")
time.sleep(3)
os.system("clear")
print(color3 + "Script By LManChi YT")
print("Dont Forget To Subscribe LManChi YT!")
print("Choose Below !")
print(rescolor + "1.Play moon-buggy games")
print("2.Fake Hacking")
print("3.DDoS(Real)")
print("4.Refresh")
print("5.Check Your Ping")
print("6.Check Web/IP ping")
print("7.Credits")
print("8.Get Web IP")
choose = input(color3 + "Choose By Number > ")

if choose == "1":
    print("Installing The Game Data")
    print("This may take a while")
    time.sleep(3)
    os.system("pkg install moon-buggy")
    time.sleep(2)
    print("Game installed!")
    time.sleep(2)
    os.system("clear")
    os.system("moon-buggy")
    
elif choose == "2":
    os.system("clear")
    print(color + "Preparing The Hack Tools")
    user = input("User : ")
    password = input("Password : ")
    print("Logged in as " + user)
    time.sleep(2)
    print("The Target can be filled with Email,WHATSAPP NUMBER,IG,FACEBOOK,IP")
    print("USE CTRL+C To Stop the Hacking!(ANROID)")
    print("USE CTRL+X To Stop the Hacking(PC)")
    htarget = input("Target : ")
    time.sleep(2)
    print("Connecting to " + htarget)
    time.sleep(2)
    print("Connected!")
    print("starting sent virus to " + htarget)
    time.sleep(3)
    i = 2
    while(i < 10000):
        time.sleep(.200)
        print(color2 + "[WARNING]" + color + "Virus Sent to " + htarget)
        time.sleep(.200)
        print(color2 + "[WARNING]" + color2 + "Virus Sent to " + htarget)
        time.sleep(.200)
        print(color2 + "[WARNING]" + color3 + "Virus Sent to " + htarget)
        time.sleep(.200)
        print(color2 + "[WARNING]" + color4 + "Virus Sent to " + htarget)
        time.sleep(.200)
        print(color2 + "[WARNING]" + color5 + "Virus Sent to " + htarget)
        time.sleep(.200)
        print(color2 + "[WARNING]" + rescolor + "Virus Sent to " + htarget)
    time.sleep(2)
    print("Target is now hacked!")
    time.sleep(2)
    print("bye!")
    time.sleep(2)
    exit()
        
elif choose == "3":
    print(color2 + "This Script Avaible Soon!")
    print(rescolor + "")
    time.sleep(5)
    os.system("python toolsv1.py")

elif choose == "4":
    print("Refreshing The Termux App")
    time.sleep(5)
    os.system("clear")
    os.system("python toolsv1.py")
    
elif choose == "5":
    print("Connecting to your connection")
    time.sleep(5)
    os.system("ping 8.8.8.8")
    
elif choose == "6":
    os.system("clear")
    ipweb = input("IP Or Web : ")
    print("Processing...")
    time.sleep(3)
    os.system("ping" + ipweb)
    
elif choose == "7":
    print(color + "Script Creator : LManChi YT")
    time.sleep(1)
    print("YouTube : LManChi YT")
    time.sleep(1)
    print("Special Thanks To : Fika sm | YouTube : Fika sm :)")
    time.sleep(1)
    print("Thanks For Using This Useless script :)")
    time.sleep(3)
    os.system("clear")
    time.sleep(3)
    os.system("python toolsv1.py")

elif choose == "8":
    os.system("clear")
    webs = input("Web : ")
    time.sleep(2)
    print("Processing...")
    time.sleep(3)
    os.system("ip link " + webs)