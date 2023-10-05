"""
Title:          ReSlotter
Purpose:        Automate the changing the slot of a character mod
Author:         Yoseff Abu Dayeh
Date:           31/12/2022
"""

import os
import PySimpleGUI as pg

def getInfo():
    c = (os.listdir(path+"\\fighter"))
    global character
    character = c[0]
    #character will store the name of the character that will be changed

    Slots = (os.listdir(path+"\\fighter\\"+character+"\\model\\body"))
    global currentSlot
    currentSlot = ""
    for i in Slots:
        if i == c:
            continue
        currentSlot += i
    #currentSlot will store the current position that the mod is installed

def rename(wantedSlot):
    costumeAndItems = os.listdir(path+ "\\fighter\\" + character + "\\model")
    for item in costumeAndItems:
        os.chdir(f"{path}\\fighter\\{character}\\model\\{item}")
        os.rename(currentSlot,f"c{wantedSlot}")
    #Changes directory to the model folder and replaces it so it is the wanted slot

    DLCorNot = os.listdir(f"{path}\\ui\\") #Checks whether we are going to the DLC folder or not
    amountofchara = os.listdir(f"{path}\\ui\\{DLCorNot[0]}\\chara") #Checks how many chara folders are there
    

    for i in amountofchara:
        os.chdir(f"{path}\\ui\\{DLCorNot[0]}\\chara\\{i}")
        charaNum = os.listdir(f"{path}\\ui\\{DLCorNot[0]}\\chara\\{i}")
        os.rename(f"{charaNum[0]}",f"{i}_{character}_{wantedSlot}.bntx")
        #Renames the file so that it fits the character
    
    sounds = os.listdir(f"{path}\\sound\\bank")
    #Checks how many sound effects it has to replace
    try:    
        sounds = os.listdir(f"{path}\\sound\\bank")
        #Checks how many sound effects it has to replace

        for folder in sounds:
            if folder == "fighter":
                os.rename(f"{path}\\sound\\bank\\{folder}\\se_{character}_{currentSlot}.nus3audio",f"{path}\\sound\\bank\\{folder}\\se_{character}_c{wantedSlot}.nus3audio")
            elif folder == "fighter_voice":
                os.rename(f"{path}\\sound\\bank\\{folder}\\vc_{character}_{currentSlot}.nus3audio",f"{path}\\sound\\bank\\{folder}\\vc_{character}_c{wantedSlot}.nus3audio")
        #renames the things. It's different depending on what is being changed.
    except FileNotFoundError:
        pass
        
pg.set_global_icon(icon= "D:\\Code\\Python\\ReSlotter\\Smash_Ball.ico")
layout = [
    [
        pg.Text("Mod Folder: "),
        pg.In(size = (25,1),enable_events=True,key="-FOLDER-"),
        pg.FolderBrowse(),
    ], #Makes the place to select the folder to choose.
    [
        pg.Text("Select the color you wish to put the mod on.")
    ],
    [
        pg.Radio("Color 1", "SLOT", default = False, key = "C1"),
        pg.Radio("Color 2", "SLOT", default = False, key = "C2"),
        pg.Radio("Color 3", "SLOT", default = False, key = "C3"),
        pg.Radio("Color 4", "SLOT", default = False, key = "C4"),
    ],
    [ # These are the radio buttons that tell what slot the mod will be put on
        pg.Radio("Color 5", "SLOT", default = False, key = "C5"),
        pg.Radio("Color 6", "SLOT", default = False, key = "C6"),
        pg.Radio("Color 7", "SLOT", default = False, key = "C7"),
        pg.Radio("Color 8", "SLOT", default = False, key = "C8"),
    ],
    [
        pg.T("When the above is selected then press this button ↓")
    ],
    [
        pg.Button("Press here when done",size=(40,2), key = "-BUTT-")
    ]
]


window = pg.Window("Character slot changer",layout, size =(355,190))
while True:
    try:
        event, values = window.read()
        if event == pg.WIN_CLOSED:
            break
        if event == '-BUTT-':
            global path
            path = values["-FOLDER-"] # Passes the path from the folder specified
            getInfo() #Sets some variables and gets some information about the mod
            if values["C1"]:
                rename("00")
            elif values["C2"]:
                rename("01")
            elif values ["C3"]:
                rename("02")
            elif values ["C4"]:
                rename("03")
            elif values ["C5"]:
                rename("04")
            elif values ["C6"]:
                rename("05")
            elif values ["C7"]:
                rename("06")
            elif values ["C8"]:
                rename("07")
            #Gives a number according to the decision on the radio buttons
            else:
                raise Exception 
            pg.Popup("Change successfully.")

    except FileNotFoundError as s:
        pg.Popup("That is a stinky path that most likely is wrong.\n\nChoose the folder that has the fighter and ui folders in it.")
        pg.Popup(s)
    except Exception:
        pg.Popup("Please select a color to change the color to.")
window.close()
#Once the program is closed, then closes the program.
