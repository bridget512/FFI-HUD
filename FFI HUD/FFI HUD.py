#github.com/bridget512
#Assetto Corsa Name: Bridget512
#Inspired by the Ferrari FF (2013) passenger display

import ac, acsys, sys, os, os.path, platform, math
if platform.architecture()[0] == "64bit":
    sysdir=os.path.dirname(__file__)+'/stdlib64'
else:
    sysdir=os.path.dirname(__file__)+'/stdlib'
sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."

from sharedMemory.sim_info import info

#==================================================#

appName = "FFI HUD"
imagePath = "apps/python/" + appName + "/_images/"

# Font
fName = "Michroma"
fSmall = 14
fNormal = 16
fGear = 30
fSpeed = 48

# Outputs
speed = 0
gear = 0
text_abs = 0
text_tcs = 0
rpm = 0
max_rpm = 0


hud20 = [
    imagePath + "hud/h00.png",              #0
    imagePath + "hud/h01.png",              #1        
    imagePath + "hud/h02.png",              #2
    imagePath + "hud/h03.png",              #3
    imagePath + "hud/h04.png",              #4
    imagePath + "hud/h05.png",              #5
    imagePath + "hud/h06.png",              #6
    imagePath + "hud/h07.png",              #7
    imagePath + "hud/h08.png",              #8
    imagePath + "hud/h09.png",              #9
    imagePath + "hud/h10.png",            #10
    imagePath + "hud/h11.png",            #11
    imagePath + "hud/h12.png",            #12
    imagePath + "hud/h13.png",            #13
    imagePath + "hud/h14.png",            #14
    imagePath + "hud/h15.png",            #15
    imagePath + "hud/h16.png",             #16
    imagePath + "hud/h17.png",            #17
    imagePath + "hud/h18.png",            #18
    imagePath + "hud/h19.png",            #19
    imagePath + "hud/h20.png"             #20
]


# =============================================================================== #     acMain
def acMain(acVersion):
    global appName, appWindow, info, imagePath
    global fName, fSmall, fNormal, fLarge, fxLarge, fGear, fSpeed
    global output_speed, speed, gear, output_gear
    global absVal, text_abs, tcsVal, text_tcs
    global output_Fuel_R

# App Window MAIN
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, "") 
    ac.setSize(appWindow, 640, 78) 
    ac.setIconPosition(appWindow, 0, -10000)
    ac.drawBorder(appWindow, 0)
    ac.initFont(0, fName, 0, 0)

# Gear
    text_gear = ac.addLabel(appWindow, "gear");
    ac.setFontSize(text_gear, fNormal)
    ac.setPosition(text_gear, 0, 52)
    ac.setFontColor(text_gear, 1, 1, 1, 0.83)
    ac.setCustomFont(text_gear, fName, 0, 0)

    output_gear = ac.addLabel(appWindow, "");
    ac.setFontSize(output_gear, fGear)
    ac.setFontAlignment(output_gear, "center")
    ac.setPosition(output_gear, 26, 4)
    ac.setCustomFont(output_gear, fName, 0, 0)
    ac.setFontColor(output_gear, 0, 0, 0, 0.55)

# TCS
    text_tcs = ac.addLabel(appWindow, "tcs");
    ac.setPosition(text_tcs, 65, 52)
    ac.setFontSize(text_tcs, fNormal)
    ac.setFontColor(text_tcs, 1, 1, 1, 0.83)
    ac.setCustomFont(text_tcs, fName, 0, 0)

# ABS
    text_abs = ac.addLabel(appWindow, "abs");
    ac.setPosition(text_abs, 110, 52)
    ac.setFontSize(text_abs, fNormal)
    ac.setFontColor(text_abs, 1, 1, 1, 0.83)
    ac.setCustomFont(text_abs, fName, 0, 0)

#Speed
    text_speed = ac.addLabel(appWindow, "km\h");
    ac.setPosition(text_speed, 610, 52) 
    ac.setFontAlignment(text_speed, "right")
    ac.setFontSize(text_speed, fNormal)
    ac.setFontColor(text_speed, 1, 1, 1, 0.83)
    ac.setCustomFont(text_speed, fName, 0, 0)

    output_speed = ac.addLabel(appWindow, "");
    ac.setFontSize(output_speed, fSpeed)
    ac.setFontAlignment(output_speed, "right")
    ac.setPosition(output_speed, 610, -6)
    ac.setFontColor(output_speed, 1, 1, 1, 0.83)
    ac.setCustomFont(output_speed, fName, 0, 0)

    #Fuel - Remaining litres
    text_Fuel_R = ac.addLabel(appWindow, "Fuel:");
    ac.setFontSize(text_Fuel_R, fNormal)
    ac.setFontAlignment(text_Fuel_R, "right")
    ac.setPosition(text_Fuel_R, 360, 52)
    ac.setFontColor(text_Fuel_R, 1, 1, 1, 0.83)
    ac.setCustomFont(text_Fuel_R, fName, 0, 0)

    output_Fuel_R = ac.addLabel(appWindow, "%01d");
    ac.setFontSize(output_Fuel_R, fNormal)
    ac.setFontAlignment(output_Fuel_R, "right")
    ac.setPosition(output_Fuel_R, 460, 52)
    ac.setFontColor(output_Fuel_R, 1, 1, 1, 0.83)
    ac.setCustomFont(output_Fuel_R, fName, 0, 0)


    return appName


# =============================================================================== #     acUpdate
def acUpdate(deltaT):
    global appName, appWindow, info, imagePath
    global output_speed, speed, gear, output_gear, max_rpm, rpm
    global output_Fuel_R
    global absVal, text_abs, tcsVal, text_tcs


#Speed
    speed = ac.getCarState(0, acsys.CS.SpeedKMH)
    ac.setText(output_speed, "%01d" % (speed))

#Gear
    gear = ac.getCarState(0, acsys.CS.Gear) - 1

    if gear == -1:
        ac.setText(output_gear, "R")
    elif gear == 0:
        ac.setText(output_gear, "N")
    else:
         ac.setText(output_gear, "%01d" % (gear))

#ABS
    absVal = info.physics.abs

    if absVal == 0:
        ac.setFontColor(text_abs, 1, 1, 1, 0.4)
    else:
        ac.setFontColor(text_abs, 1, 1, 1, 0.83)


#TCS
    tcsVal = info.physics.tc

    if tcsVal == 0:
        ac.setFontColor(text_tcs, 1, 1, 1, 0.4)
    else:
        ac.setFontColor(text_tcs, 1, 1, 1, 0.83)


# RPM Actions
    rpm = info.physics.rpms
    max_rpm = info.static.maxRpm
    max_rpm_remap = round(((rpm) * (20) / (max_rpm)))

# Assign image per Rounded RPM
    for i in hud20:
        ac.setBackgroundTexture(appWindow, imagePath + "hud/h" + str(max_rpm_remap) + ".png")

# max_rpm_remap gets rounded to a solid number (based on the amount of images)
# That number gets used as the image number


# Fuel_Remaining
    fuel_R = info.physics.fuel
    ac.setText(output_Fuel_R, "{:.2f} l".format(fuel_R))



    ac.setBackgroundOpacity(appWindow, 0)