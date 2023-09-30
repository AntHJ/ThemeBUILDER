##################################################
## CUSTOM VITA THEME BUILDER - CREATED BY ANTHJ ##
##################################################

##  Both the theme builder and the icon builer are my first attempts at creating Pyton apps
##  so i apoligise if there are any issuse and for the untidyness and sloppy code in places
##  they both do what i set out to achive and arent pervect but could be helpful to someone
## feel free to make edits and re-releases but dont forget to give me a shout out, thanks.!

from pathlib import Path
from PIL import Image, ImageGrab
import PySimpleGUI as sg
import os
import ctypes
import webbrowser
import subprocess

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
sg.theme('PythonPlus')
default_button = sg.theme_button_color()
sg.set_options(font=("Helvetica", 13))
box_coordinates = ((0,48),(226,80))
txt_coordinates = (113,65)

# DEFAULT THEME INFORMATION
ThemeName = ""
ThemeVers = "01.00"
Creator = ""

# LOAD CREATOR NAME FROM FILE
SETTINGS_PATH = Path.cwd()
settings = sg.UserSettings(path=SETTINGS_PATH, filename="assets\default.ini", use_config_file=True)
Creator = settings["DEFAULT_CREATOR"]["Creator"]

# DELETE PREVIOUS TEMPORARY IMAGES
TEMPfolder = 'assets\preview\TEMP'
if not os.path.exists(TEMPfolder):
                os.makedirs(TEMPfolder)
for filename in os.listdir(TEMPfolder):
    file_path = os.path.join(TEMPfolder, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
SCREEN = ('UPDADED')
exportable=0
firstrun=1
Swapped=0
bypass=0
retry=0

def c(elems):
    return [sg.Stretch(), *elems, sg.Stretch()]
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

if 1==1:    # DEFAULT USER OPTIONS
    LS = ""
    PG1 = ""
    PG2 = ""
    PG3 = ""
    PG4 = ""
    PG5 = ""
    PG6 = ""
    PG7 = ""
    PG8 = ""
    PG9 = ""
    PG10 = ""
    PG1w = "13"
    PG2w = "13"
    PG3w = "13"
    PG4w = "13"
    PG5w = "13"
    PG6w = "13"
    PG7w = "13"
    PG8w = "13"
    PG9w = "13"
    PG10w = "13"
    BGM = "Default"
    CLOPOS = "Bottom Left"
    ICOSET = "Default"

    # DEFAULT IMAGES
    Image_LS_Overlay = "assets/preview/default/overlay.png"
    Image_NoteNO = "assets/preview/default/LAnoteno.png"
    Image_NoteNOx = "assets\preview\TEMP\LAnoteno.png"
    Image_NoteNEW = "assets/preview/default/LAnotenew.png"
    Image_NoteNEWx = "assets\preview\TEMP\LAnotenew.png"
    NOTI_inon = "assets/preview/default/LAnoteno_def.png"
    NOTI_inew = "assets/preview/default/LAnotenew_def.png"
    NOTI_imsk = "assets/preview/default/LAnotemsk.png"
    Image_Icon1 = "assets/preview/default/icon_web.png"
    Image_Icon2 = "assets/preview/default/icon_settings.png"
    Image_Icon3 = "assets/preview/default/icon_calendar.png"
    Image_Icon4 = "assets/preview/default/icon_photos.png"
    Image_base = "assets/preview/default/base.png"
    Image_curs = "assets/preview/default/curs.png"
    ORIG_BGM = "assets\preview\default\origional.at9"

    # MORE DEFAULTS
    TBC = rgb_to_hex((0,0,0))
    TBTC = rgb_to_hex((255,255,255))

    CCr = 255
    CCg = 255
    CCb = 255
    CLOCOL = rgb_to_hex((255,255,255))

    TBRED = 0
    TBGRE = 0
    TBBLU = 0
    TBTRED = 255
    TBTGRE = 255
    TBTBLU = 255
    
    NOT_BOX_RED = 42
    NOT_BOX_GRE = 42
    NOT_BOX_BLU = 42
    NOT_TX_RED = 255
    NOT_TX_GRE = 255
    NOT_TX_BLU = 255
    NOT_BOXc = '#2a2a2a'
    NOT_TXTc = '#ffffff'

    NOT_BOX_BOX_COL = '#2a2a2a'
    NOT_BOX_FRA_COL = '#cccccc'
    NOT_BOX_TXT_COL = '#ffffff'
    NOT_BBL_TXT_COL = '#ffffff'
    
    PG1txtc = '#ffffff'
    PG2txtc = '#ffffff'
    PG3txtc = '#ffffff'
    PG4txtc = '#ffffff'
    PG5txtc = '#ffffff'
    PG6txtc = '#ffffff'
    PG7txtc = '#ffffff'
    PG8txtc = '#ffffff'
    PG9txtc = '#ffffff'
    PG10txtc = '#ffffff'

    VITA = 0
    LA_View = 1
    NOT_View = 0
    H1,V1 = 0,110
    H2,V2 = 0,110

def EDIT_THEME():
    global ThemeName
    global ThemeVers
    global Creator
    global ThemeExists
    global CLOCOL
    global CLOPOS
    global NOT_BOXc
    global NOT_BOX_BOX_COL
    global NOT_TXTc
    global NOT_BBL_TXT_COL
    global NOTI_inew
    global NOTI_inon
    global TBC
    global TBTC
    global LS
    global PG1
    global PG2
    global PG3
    global PG4
    global PG5
    global PG6
    global PG7
    global PG8
    global PG9
    global PG10
    global PG1_old
    global PG2_old
    global PG3_old
    global PG4_old
    global PG5_old
    global PG6_old
    global PG7_old
    global PG8_old
    global PG9_old
    global PG10_old
    global PG1w
    global PG2w
    global PG3w
    global PG4w
    global PG5w
    global PG6w
    global PG7w
    global PG8w
    global PG9w
    global PG10w
    global PG1txtc
    global PG2txtc
    global PG3txtc
    global PG4txtc
    global PG5txtc
    global PG6txtc
    global PG7txtc
    global PG8txtc
    global PG9txtc
    global PG10txtc
    global exportable
    global GUI_Choice
    
    layoutINFO = [
        [sg.Text("")],
        [sg.Text('Name :',s=9,justification='r'), sg.Input(default_text=ThemeName,k='1st'),sg.Text("  ")],
        [sg.Text('Version :',s=9,justification='r'), sg.Input(default_text=ThemeVers,k='2nd'),sg.Text("  ")],
        [sg.Text('Creator :',s=9,justification='r'), sg.Input(default_text=Creator,k='3rd'),sg.Text("  ")],
        [sg.Text("")],
        c([sg.Text("           "),sg.Button('Ok',s=12),sg.Button('Cancel',s=12),sg.Text("    "),sg.Input(default_text="0", key='iniFILE',visible=False),sg.FileBrowse('Load',s=12,k='-load-',file_types=(('theme.ini', 'theme.ini'),))]),
        [sg.Text("")]
        ]

    layoutINFOx = [[sg.Column(layoutINFO)]]
    windowINFO = sg.Window('THEME INFORMATION', layoutINFOx, grab_anywhere=True, no_titlebar=True, keep_on_top=True, finalize=True, background_color='#015BBB',margins=(0,0))
    windowINFO['1st'].SetFocus()
    windowINFO['1st'].Widget.icursor('end')
    windowINFO['1st'].bind('<Return>', 'return')
    windowINFO['2nd'].bind('<Return>', 'return')
    windowINFO['3rd'].bind('<Return>', 'return')
    if firstrun==0:
            windowINFO['-load-'].update(visible=False)
    while True:
        eventI, valuesI = windowINFO.read(10)
        
        if eventI == sg.WIN_CLOSED or eventI == 'Cancel':
            if valuesI['1st'] == "":
                ThemeName = '-CLOSE-APP-'
                quit()
            windowINFO.close()
            break
        
        if eventI == '1streturn':
            windowINFO['2nd'].SetFocus()
            windowINFO['2nd'].Widget.icursor('end')
        if eventI == '2ndreturn':
            windowINFO['3rd'].SetFocus()
            windowINFO['3rd'].Widget.icursor('end')
        if eventI == '3rdreturn':
            eventI = 'Ok'
        
        if not valuesI['iniFILE'] == "0":
                iniFILE = valuesI['iniFILE']
                exportable = 1
                ThemeBUILD = sg.UserSettings(path=SETTINGS_PATH, filename=iniFILE, use_config_file=True)
                ThemePATH = iniFILE.replace("theme.ini","")
                
                ThemeName = ThemeBUILD["THEME"]["Name"]
                window['Theme_Name'].update(ThemeName)
                ThemeVers = ThemeBUILD["THEME"]["Version"]
                window['Theme_Version'].update(ThemeVers)
                Creator = ThemeBUILD["THEME"]["Creator"]
                window['Theme_Creator'].update(Creator)
                
                CLOCOL = ThemeBUILD["CLOCK"]["Color"]
                CLOCOL = ("#"+CLOCOL)
                CLOPOS = ThemeBUILD["CLOCK"]["Position"]
                if CLOPOS=="0": CLOPOS="Bottom Left"
                if CLOPOS=="1": CLOPOS="Top Left"
                if CLOPOS=="2": CLOPOS="Bottom Right"
                window['-CLOPOS-'].update(CLOPOS)
                
                NOT_BOXc = ThemeBUILD["NOTIFICATION"]["Box Color"]
                NOT_BOXc = ("#"+NOT_BOXc)
                NOT_BOX_BOX_COL = NOT_BOXc
                NOT_TXTc = ThemeBUILD["NOTIFICATION"]["Text Color"]
                NOT_TXTc = ("#"+NOT_TXTc)
                NOT_BBL_TXT_COL = NOT_TXTc
                
                if os.path.isfile(ThemePATH+"notice.png"):
                    with open(ThemePATH+"notice.png", 'rb') as src_file:
                        with open('assets\preview\TEMP\LAnotenew_def.png', 'wb') as dest_file:
                            dest_file.write(src_file.read())
                    NOTI_inew = "assets\preview\TEMP\LAnotenew_def.png"
                else:
                    NOTI_inew = "assets/preview/default/LAnotenew_def.png"
                    
                if os.path.isfile(ThemePATH+"notices.png"):
                    with open(ThemePATH+"notices.png", 'rb') as src_file:
                        with open('assets\preview\TEMP\LAnoteno_def.png', 'wb') as dest_file:
                            dest_file.write(src_file.read())
                    NOTI_inon = "assets\preview\TEMP\LAnoteno_def.png"
                else:
                    NOTI_inon = "assets/preview/default/LAnoteno_def.png"
                    
                convINON_1a = ('call assets\scale.bat -source "assets\preview\TEMP\LAnoteno_def.png" -target "assets\preview\TEMP\LAnoteno.png" -max-height 37 -keep-ratio yes -force yes')
                convINON_1b = ('assets\convert "assets\preview\TEMP\LAnoteno.png" "assets\mask_not.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\LAnoteno.png')
                os.system(convINON_1a)
                os.system(convINON_1b)
                convINEW_1a = ('call assets\scale.bat -source "assets\preview\TEMP\LAnotenew_def.png" -target "assets\preview\TEMP\LAnotenew.png" -max-height 37 -keep-ratio yes -force yes')
                convINEW_1b = ('assets\convert "assets\preview\TEMP\LAnotenew.png" "assets\mask_not.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\LAnotenew.png')
                os.system(convINEW_1a)
                os.system(convINEW_1b)
                
                TBC = ThemeBUILD["INFOBAR"]["Bar Color"]
                TBC = ("#"+TBC)
                TBTC = ThemeBUILD["INFOBAR"]["Text Color"]
                TBTC = ("#"+TBTC)
                
                ICOSET = ThemePATH
                window['ICOSET'].update(ICOSET)
                BGM = (ThemePATH+"bgm.at9")
                window['BGM'].update(BGM)
                
                cmdline1 = ('copy "{}\lockscreen.png" "assets\preview\TEMP\\bg0.png"').format(ThemePATH)
                cmdline2 = ('copy "{}\BG?.png" "assets\preview\TEMP\\bg?.png"').format(ThemePATH)
                cmdline3 = ('copy "{}\BG10.png" "assets\preview\TEMP\\bg10.png"').format(ThemePATH)
                os.system(cmdline1)
                os.system(cmdline2)
                os.system(cmdline3)
                LS="assets\preview\TEMP\\bg0.png"
                PG1="assets\preview\TEMP\\bg1.png"
                PG2="assets\preview\TEMP\\bg2.png"
                PG3="assets\preview\TEMP\\bg3.png"
                PG4="assets\preview\TEMP\\bg4.png"
                PG5="assets\preview\TEMP\\bg5.png"
                PG6="assets\preview\TEMP\\bg6.png"
                PG7="assets\preview\TEMP\\bg7.png"
                PG8="assets\preview\TEMP\\bg8.png"
                PG9="assets\preview\TEMP\\bg9.png"
                PG10="assets\preview\TEMP\\bg10.png"
                
                window['LS'].update(LS)
                window['PG1'].update(PG1)
                window['PG2'].update(PG2)
                window['PG3'].update(PG3)
                window['PG4'].update(PG4)
                window['PG5'].update(PG5)
                window['PG6'].update(PG6)
                window['PG7'].update(PG7)
                window['PG8'].update(PG8)
                window['PG9'].update(PG9)
                window['PG10'].update(PG10)
                
                PG1w = ThemeBUILD["WAVE PATTERNS"]["Page 1"]
                window['PG1w'].update(PG1w)
                PG2w = ThemeBUILD["WAVE PATTERNS"]["Page 2"]
                window['PG2w'].update(PG2w)
                PG3w = ThemeBUILD["WAVE PATTERNS"]["Page 3"]
                window['PG3w'].update(PG3w)
                PG4w = ThemeBUILD["WAVE PATTERNS"]["Page 4"]
                window['PG4w'].update(PG4w)
                PG5w = ThemeBUILD["WAVE PATTERNS"]["Page 5"]
                window['PG5w'].update(PG5w)
                PG6w = ThemeBUILD["WAVE PATTERNS"]["Page 6"]
                window['PG6w'].update(PG6w)
                PG7w = ThemeBUILD["WAVE PATTERNS"]["Page 7"]
                window['PG7w'].update(PG7w)
                PG8w = ThemeBUILD["WAVE PATTERNS"]["Page 8"]
                window['PG8w'].update(PG8w)
                PG9w = ThemeBUILD["WAVE PATTERNS"]["Page 9"]
                window['PG9w'].update(PG9w)
                PG10w = ThemeBUILD["WAVE PATTERNS"]["Page 10"]
                window['PG10w'].update(PG10w)
                
                PG1txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 1"]
                PG1txtc =("#"+PG1txtc)
                window['PG1tc'].update(button_color=PG1txtc)
                PG2txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 2"]
                PG2txtc =("#"+PG2txtc)
                window['PG2tc'].update(button_color=PG2txtc)
                PG3txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 3"]
                PG3txtc =("#"+PG3txtc)
                window['PG3tc'].update(button_color=PG3txtc)
                PG4txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 4"]
                PG4txtc =("#"+PG4txtc)
                window['PG4tc'].update(button_color=PG4txtc)
                PG5txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 5"]
                PG5txtc =("#"+PG5txtc)
                window['PG5tc'].update(button_color=PG5txtc)
                PG6txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 6"]
                PG6txtc =("#"+PG6txtc)
                window['PG6tc'].update(button_color=PG6txtc)
                PG7txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 7"]
                PG7txtc =("#"+PG7txtc)
                window['PG7tc'].update(button_color=PG7txtc)
                PG8txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 8"]
                PG8txtc =("#"+PG8txtc)
                window['PG8tc'].update(button_color=PG8txtc)
                PG9txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 9"]
                PG9txtc =("#"+PG9txtc)
                window['PG9tc'].update(button_color=PG9txtc)
                PG10txtc = ThemeBUILD["PAGE TEXT COLORS"]["Page 10"]
                PG10txtc =("#"+PG10txtc)
                window['PG10tc'].update(button_color=PG10txtc)
                
                checkfile=('Created Themes/'+ThemeName+'/Theme.xml')
                if Path(checkfile).is_file():
                    ThemeExists=1
                    window['Warn'].update(visible=True)
                else:
                    ThemeExists=0
                    window['Warn'].update(visible=False)
                
                windowINFO.close()
                break
                
        if eventI == 'Ok':
            settings["DEFAULT_CREATOR"]["Creator"] = valuesI['3rd']
            if valuesI['2nd'] == "":
                valuesI['2nd'] = "01.00"
            ThemeName = valuesI['1st']
            ThemeVers = valuesI['2nd']
            Creator = valuesI['3rd']
            ThemeVers=float(ThemeVers)
            ThemeVers='{:0>5.2f}'.format(ThemeVers)
            if float(ThemeVers)>99.99:
                ThemeVers=99.99
            if float(ThemeVers)<01.00:
                ThemeVers=01.00
                ThemeVers=float(ThemeVers)
                ThemeVers='{:0>5.2f}'.format(ThemeVers)
            window['Theme_Name'].update(valuesI['1st'])
            window['Theme_Version'].update(ThemeVers)
            window['Theme_Creator'].update(valuesI['3rd'])

            checkfile=('Created Themes/'+ThemeName+'/Theme.xml')
            if Path(checkfile).is_file():
                ThemeExists=1
                window['Warn'].update(visible=True)
            else:
                ThemeExists=0
                window['Warn'].update(visible=False)
            windowINFO.close()
            break

def CLOCK_COLOR():
    global CLOCOL
    global CCr
    global CCg
    global CCb
    global SCREEN
    
    layoutCLOCK = [
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCr,k='CCr'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCg,k='CCg'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCb,k='CCb')],
        c([sg.Button("CLO_BLACK",s=1,button_color=('Black','Black')),sg.Button("CLO_RED",s=1,button_color=('Red','Red')),sg.Button("CLO_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("CLO_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("CLO_GREEN",s=1,button_color=('Green','Green')),sg.Button("CLO_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("CLO_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("CLO_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("CLO_PINK",s=1,button_color=('Pink','Pink')),sg.Button("CLO_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        [sg.Stretch(),sg.Text("19:30",font=('Helvetica', 60), text_color=CLOCOL, justification='c',k='CLOCOLORC'),sg.Stretch()],
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        c([sg.Button("OK",s=10),sg.Button("Cancel",s=10)]),
        [sg.Text("")],
        ]

    layoutCLOCKx = [[sg.Column(layoutCLOCK)]]
    windowCLOCK = sg.Window('Select Clock Color', layoutCLOCKx, no_titlebar=True, grab_anywhere=True, keep_on_top=True,background_color='#015BBB',margins=(0,0))
    window.hide()
    while True:
        eventC, valuesTC = windowCLOCK.read(10)
        if eventC == sg.WIN_CLOSED or eventC == 'Cancel':
            windowCLOCK.close()
            window.UnHide()
            break
        if eventC == 'CLO_BLACK':
            windowCLOCK['CCr'].update(0)
            windowCLOCK['CCg'].update(0)
            windowCLOCK['CCb'].update(0)
        if eventC == 'CLO_RED':
            windowCLOCK['CCr'].update(255)
            windowCLOCK['CCg'].update(0)
            windowCLOCK['CCb'].update(0)
        if eventC == 'CLO_ORANGE':
            windowCLOCK['CCr'].update(255)
            windowCLOCK['CCg'].update(125)
            windowCLOCK['CCb'].update(0)
        if eventC == 'CLO_YELLOW':
            windowCLOCK['CCr'].update(255)
            windowCLOCK['CCg'].update(255)
            windowCLOCK['CCb'].update(0)
        if eventC == 'CLO_GREEN':
            windowCLOCK['CCr'].update(0)
            windowCLOCK['CCg'].update(125)
            windowCLOCK['CCb'].update(0)        
        if eventC == 'CLO_CYAN':
            windowCLOCK['CCr'].update(0)
            windowCLOCK['CCg'].update(255)
            windowCLOCK['CCb'].update(255)
        if eventC == 'CLO_BLUE':
            windowCLOCK['CCr'].update(0)
            windowCLOCK['CCg'].update(0)
            windowCLOCK['CCb'].update(255)
        if eventC == 'CLO_PURPLE':
            windowCLOCK['CCr'].update(125)
            windowCLOCK['CCg'].update(0)
            windowCLOCK['CCb'].update(125)
        if eventC == 'CLO_PINK':
            windowCLOCK['CCr'].update(255)
            windowCLOCK['CCg'].update(125)
            windowCLOCK['CCb'].update(255)
        if eventC == 'CLO_WHITE':
            windowCLOCK['CCr'].update(255)
            windowCLOCK['CCg'].update(255)
            windowCLOCK['CCb'].update(255)
        
        CCRED = int(valuesTC['CCr'])
        CCGRE = int(valuesTC['CCg'])
        CCBLU = int(valuesTC['CCb'])
        CCOL = CCRED,CCGRE,CCBLU
        CLOCOL = rgb_to_hex(CCOL)
        windowCLOCK['CLOCOLORC'].update(text_color=(CLOCOL))
        if eventC == 'OK':
            CCr = CCRED
            CCg = CCGRE
            CCb = CCBLU
            SCREEN = ('UPDADED')
            windowCLOCK.close()
            window.UnHide()

def BAR_COLOR():
    global TBC
    global TBTC
    global TBTr
    global TBTg
    global TBTb
    global TBRED
    global TBGRE
    global TBBLU
    global TBTRED
    global TBTGRE
    global TBTBLU
    global SCREEN
    
    layoutCOL = [
        [sg.Text("")],
        c([sg.Text("BAR COLOR",font=('Helvetica', 12))]),
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBRED,k='TBr'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBGRE,k='TBg'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBBLU,k='TBb')],
        c([sg.Button("BAR_BLACK",s=1,button_color=('Black','Black')),sg.Button("BAR_RED",s=1,button_color=('Red','Red')),sg.Button("BAR_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("BAR_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("BAR_GREEN",s=1,button_color=('Green','Green')),sg.Button("BAR_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("BAR_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("BAR_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("BAR_PINK",s=1,button_color=('Pink','Pink')),sg.Button("BAR_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        c([sg.Text("TEXT COLOR",font=('Helvetica', 12))]),
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBTRED,k='TBTr'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBTGRE,k='TBTg'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=TBTBLU,k='TBTb')],
        c([sg.Button("TXT_BLACK",s=1,button_color=('Black','Black')),sg.Button("TXT_RED",s=1,button_color=('Red','Red')),sg.Button("TXT_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("TXT_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("TXT_GREEN",s=1,button_color=('Green','Green')),sg.Button("TXT_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("TXT_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("TXT_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("TXT_PINK",s=1,button_color=('Pink','Pink')),sg.Button("TXT_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Stretch(),sg.Text("Titlebar text",background_color=TBC,s=30,font=('Helvetica', 16), text_color=TBTC, justification='c',k='TITLECOL'),sg.Stretch()],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        c([sg.Button("OK",s=10),sg.Button("Cancel",s=10)]),
        [sg.Text("")],
        ]
    
    layoutCOLx = [[sg.Column(layoutCOL)]]
    windowCOL = sg.Window('Select Titlebar Colors', layoutCOLx, no_titlebar=True, grab_anywhere=True, keep_on_top=True,background_color='#015BBB',margins=(0,0))
    window.hide()
    
    while True:
        eventC, valuesC = windowCOL.read(10)
        if eventC == sg.WIN_CLOSED or eventC == 'Cancel':
            windowCOL.close()
            window.UnHide()
            break
        if eventC == 'BAR_BLACK':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_RED':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_ORANGE':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_YELLOW':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_GREEN':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(0)        
        if eventC == 'BAR_CYAN':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_BLUE':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_PURPLE':
            windowCOL['TBr'].update(125)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(125)
        if eventC == 'BAR_PINK':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_WHITE':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(255)
        if eventC == 'TXT_BLACK':
            windowCOL['TBTr'].update(0)
            windowCOL['TBTg'].update(0)
            windowCOL['TBTb'].update(0)
        if eventC == 'TXT_RED':
            windowCOL['TBTr'].update(255)
            windowCOL['TBTg'].update(0)
            windowCOL['TBTb'].update(0)
        if eventC == 'TXT_ORANGE':
            windowCOL['TBTr'].update(255)
            windowCOL['TBTg'].update(125)
            windowCOL['TBTb'].update(0)
        if eventC == 'TXT_YELLOW':
            windowCOL['TBTr'].update(255)
            windowCOL['TBTg'].update(255)
            windowCOL['TBTb'].update(0)
        if eventC == 'TXT_GREEN':
            windowCOL['TBTr'].update(0)
            windowCOL['TBTg'].update(125)
            windowCOL['TBTb'].update(0)        
        if eventC == 'TXT_CYAN':
            windowCOL['TBTr'].update(0)
            windowCOL['TBTg'].update(255)
            windowCOL['TBTb'].update(255)
        if eventC == 'TXT_BLUE':
            windowCOL['TBTr'].update(0)
            windowCOL['TBTg'].update(0)
            windowCOL['TBTb'].update(255)
        if eventC == 'TXT_PURPLE':
            windowCOL['TBTr'].update(125)
            windowCOL['TBTg'].update(0)
            windowCOL['TBTb'].update(125)
        if eventC == 'TXT_PINK':
            windowCOL['TBTr'].update(255)
            windowCOL['TBTg'].update(125)
            windowCOL['TBTb'].update(255)
        if eventC == 'TXT_WHITE':
            windowCOL['TBTr'].update(255)
            windowCOL['TBTg'].update(255)
            windowCOL['TBTb'].update(255)
        
        TBTRED = int(valuesC['TBTr'])
        TBTGRE = int(valuesC['TBTg'])
        TBTBLU = int(valuesC['TBTb'])
        TBTCOL = TBTRED,TBTGRE,TBTBLU
        TBTC = rgb_to_hex(TBTCOL)
        windowCOL['TITLECOL'].update(text_color=(TBTC))
        
        TBRED = int(valuesC['TBr'])
        TBGRE = int(valuesC['TBg'])
        TBBLU = int(valuesC['TBb'])
        TBCOL = TBRED,TBGRE,TBBLU
        TBC = rgb_to_hex(TBCOL)
        windowCOL['TITLECOL'].update(background_color=(TBC))
        
        if eventC == 'OK':
            TBTr = TBTRED
            TBTg = TBTGRE
            TBTb = TBTBLU
            TBr = TBRED
            TBg = TBGRE
            TBb = TBBLU
            SCREEN = ('UPDADED')
            windowCOL.close()
            window.UnHide()
def PAGE_TEXT_COLOR():
    global PAGE_TEXT
    global PG1txtc
    global PG2txtc
    global PG3txtc
    global PG4txtc
    global PG5txtc
    global PG6txtc
    global PG7txtc
    global PG8txtc
    global PG9txtc
    global PG10txtc
    CLOCOL='White'
    
    if PAGE_TEXT == 1:
        CLOCOL = PG1txtc
    if PAGE_TEXT == 2:
        CLOCOL = PG2txtc
    if PAGE_TEXT == 3:
        CLOCOL = PG3txtc
    if PAGE_TEXT == 4:
        CLOCOL = PG4txtc
    if PAGE_TEXT == 5:
        CLOCOL = PG5txtc
    if PAGE_TEXT == 6:
        CLOCOL = PG6txtc
    if PAGE_TEXT == 7:
        CLOCOL = PG7txtc
    if PAGE_TEXT == 8:
        CLOCOL = PG8txtc
    if PAGE_TEXT == 9:
        CLOCOL = PG9txtc
    if PAGE_TEXT == 10:
        CLOCOL = PG10txtc
    
    global SCREEN
    
    layoutTEXTCOL = [
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCr,k='CCr'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCg,k='CCg'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=CCb,k='CCb')],
        c([sg.Button("CLO_BLACK",s=1,button_color=('Black','Black')),sg.Button("CLO_RED",s=1,button_color=('Red','Red')),sg.Button("CLO_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("CLO_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("CLO_GREEN",s=1,button_color=('Green','Green')),sg.Button("CLO_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("CLO_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("CLO_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("CLO_PINK",s=1,button_color=('Pink','Pink')),sg.Button("CLO_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        [sg.Stretch(),sg.Text("Icon Text",font=('Helvetica', 60), text_color=CLOCOL, justification='c',k='CLOCOLORC'),sg.Stretch()],
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        c([sg.Button("OK",s=10),sg.Button("Cancel",s=10),sg.Button("Set ALL",s=10)]),
        [sg.Text("")],
        ]

    layoutTEXTCOLx = [[sg.Column(layoutTEXTCOL)]]
    windowTEXTCOL = sg.Window('Select Icon Text Color', layoutTEXTCOLx, grab_anywhere=True, no_titlebar=True, keep_on_top=True, background_color='#015BBB',margins=(0,0))
    window.hide()
    
    while True:
        eventTC, valuesTC = windowTEXTCOL.read(10)
        if eventTC == sg.WIN_CLOSED or eventTC == 'Cancel':
            windowTEXTCOL.close()
            window.UnHide()
            break
        if eventTC == 'CLO_BLACK':
            windowTEXTCOL['CCr'].update(0)
            windowTEXTCOL['CCg'].update(0)
            windowTEXTCOL['CCb'].update(0)
        if eventTC == 'CLO_RED':
            windowTEXTCOL['CCr'].update(255)
            windowTEXTCOL['CCg'].update(0)
            windowTEXTCOL['CCb'].update(0)
        if eventTC == 'CLO_ORANGE':
            windowTEXTCOL['CCr'].update(255)
            windowTEXTCOL['CCg'].update(125)
            windowTEXTCOL['CCb'].update(0)
        if eventTC == 'CLO_YELLOW':
            windowTEXTCOL['CCr'].update(255)
            windowTEXTCOL['CCg'].update(255)
            windowTEXTCOL['CCb'].update(0)
        if eventTC == 'CLO_GREEN':
            windowTEXTCOL['CCr'].update(0)
            windowTEXTCOL['CCg'].update(125)
            windowTEXTCOL['CCb'].update(0)        
        if eventTC == 'CLO_CYAN':
            windowTEXTCOL['CCr'].update(0)
            windowTEXTCOL['CCg'].update(255)
            windowTEXTCOL['CCb'].update(255)
        if eventTC == 'CLO_BLUE':
            windowTEXTCOL['CCr'].update(0)
            windowTEXTCOL['CCg'].update(0)
            windowTEXTCOL['CCb'].update(255)
        if eventTC == 'CLO_PURPLE':
            windowTEXTCOL['CCr'].update(125)
            windowTEXTCOL['CCg'].update(0)
            windowTEXTCOL['CCb'].update(125)
        if eventTC == 'CLO_PINK':
            windowTEXTCOL['CCr'].update(255)
            windowTEXTCOL['CCg'].update(125)
            windowTEXTCOL['CCb'].update(255)
        if eventTC == 'CLO_WHITE':
            windowTEXTCOL['CCr'].update(255)
            windowTEXTCOL['CCg'].update(255)
            windowTEXTCOL['CCb'].update(255)
        
        CCRED = int(valuesTC['CCr'])
        CCGRE = int(valuesTC['CCg'])
        CCBLU = int(valuesTC['CCb'])
        CCOL = CCRED,CCGRE,CCBLU
        CLOCOL = rgb_to_hex(CCOL)
        windowTEXTCOL['CLOCOLORC'].update(text_color=(CLOCOL))        

        if eventTC == 'OK':
            if PAGE_TEXT == 1:
                PG1txtc = CLOCOL
                window['PG1tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 2:
                PG2txtc = CLOCOL
                window['PG2tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 3:
                PG3txtc = CLOCOL
                window['PG3tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 4:
                PG4txtc = CLOCOL
                window['PG4tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 5:
                PG5txtc = CLOCOL
                window['PG5tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 6:
                PG6txtc = CLOCOL
                window['PG6tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 7:
                PG7txtc = CLOCOL
                window['PG7tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 8:
                PG8txtc = CLOCOL
                window['PG8tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 9:
                PG9txtc = CLOCOL
                window['PG9tc'].update(button_color=(CLOCOL))
            if PAGE_TEXT == 10:
                PG10txtc = CLOCOL
                window['PG10tc'].update(button_color=(CLOCOL))
            
            SCREEN = ('UPDADED')
            windowTEXTCOL.close()
            window.UnHide()
            
        if eventTC == 'Set ALL':
            PG1txtc=PG2txtc=PG3txtc=PG4txtc=PG5txtc=PG6txtc=PG7txtc=PG8txtc=PG9txtc=PG10txtc = CLOCOL
            window['PG1tc'].update(button_color=(CLOCOL))
            window['PG2tc'].update(button_color=(CLOCOL))
            window['PG3tc'].update(button_color=(CLOCOL))
            window['PG4tc'].update(button_color=(CLOCOL))
            window['PG5tc'].update(button_color=(CLOCOL))
            window['PG6tc'].update(button_color=(CLOCOL))
            window['PG7tc'].update(button_color=(CLOCOL))
            window['PG8tc'].update(button_color=(CLOCOL))
            window['PG9tc'].update(button_color=(CLOCOL))
            window['PG10tc'].update(button_color=(CLOCOL))
            
            SCREEN = ('UPDADED')
            windowTEXTCOL.close()

def NOTIFICATION_EDIT():
    
    global H1
    global V1
    global H2
    global V2
    global NOT_BOXc
    global NOT_TXTc
    global NOT_BOX_RED
    global NOT_BOX_GRE
    global NOT_BOX_BLU
    global NOT_TX_RED
    global NOT_TX_GRE
    global NOT_TX_BLU
    global NOT_View
    global NOT_BOX_BOX_COL
    global NOT_BOX_TXT_COL
    global NOTI_inon
    global NOTI_inew
    if Path('assets\preview\TEMP\LAnoteno_def.png').is_file():
        NOTI_inon = 'assets\preview\TEMP\LAnoteno_def.png'
        H1,V1=0,110
        HH1=120
    if Path('assets\preview\TEMP\LAnotenew_def.png').is_file():
        NOTI_inew = 'assets\preview\TEMP\LAnotenew_def.png'
        H2,V2=0,110
        HH2=120
    old_NOTI_inon = NOTI_inon
    old_NOTI_inew = NOTI_inew   
    CUSTOM_CHANGE=0
    cm1=0
    cm2=0
    global SCREEN

    layoutCOL1 = [
        [sg.Text("")],
        c([sg.Text("NOTIFICATION BAR COLOR",font=('Helvetica', 12))]),
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_BOX_RED,k='TBr'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_BOX_GRE,k='TBg'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_BOX_BLU,k='TBb')],
        c([sg.Button("BAR_BLACK",s=1,button_color=('Black','Black')),sg.Button("BAR_RED",s=1,button_color=('Red','Red')),sg.Button("BAR_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("BAR_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("BAR_GREEN",s=1,button_color=('Green','Green')),sg.Button("BAR_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("BAR_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("BAR_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("BAR_PINK",s=1,button_color=('Pink','Pink')),sg.Button("BAR_WHITE",s=1,button_color=('White','White')),]),
       #c([sg.Checkbox('Semi Transparent',default=True,k='NOT_TRAN')]), #Possible future feature?
        [sg.Text("")],
        c([sg.Text("TEXT COLOR",font=('Helvetica', 12))]),
        [sg.HorizontalSeparator()],
        [sg.Text("R : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_TX_RED,k='NOT_TX_r'),
        sg.Text("G : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_TX_GRE,k='NOT_TX_g'),
        sg.Text("B : "),sg.Slider(range=(0, 255), orientation='h', resolution=1, disable_number_display=False, size=(10, 15), default_value=NOT_TX_BLU,k='NOT_TX_b')],
        c([sg.Button("TXT_BLACK",s=1,button_color=('Black','Black')),sg.Button("TXT_RED",s=1,button_color=('Red','Red')),sg.Button("TXT_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("TXT_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("TXT_GREEN",s=1,button_color=('Green','Green')),sg.Button("TXT_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("TXT_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("TXT_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("TXT_PINK",s=1,button_color=('Pink','Pink')),sg.Button("TXT_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        [sg.Text("")],
        [sg.HorizontalSeparator()],
        [sg.Stretch(),sg.Text("Notification text",background_color=NOT_BOX_BOX_COL,s=30,font=('Helvetica', 16), text_color=NOT_TXTc, justification='c',k='TITLECOL'),sg.Stretch()],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        c([sg.Button("Defaults",s=10)]),
        [sg.Text("")],
        ]
        
    layoutCOL2 = [
        [sg.Text("")],
        c([sg.Input(key='ICONno',default_text=NOTI_inon,visible=False),sg.FileBrowse(s=8),sg.Button("Default",s=8,k='DEF1')]),
        c([sg.Button("Capture mask",k='capture1',s=16)]),
        [sg.Text("")],
        c([sg.Button("Copy this image -->",k='CopyAtoB',s=19)]),
        c([sg.Button("Copy image position -->",k='copy1',s=21)]),
        c([sg.Button("Reset image position",k='rip1',s=17)]),
        [sg.Text("")],
        c([sg.Button("UP",k='1u')]),
        c([sg.Button("LEFT",k='1l'),sg.Graph((120,110), (0,0), (120,110), key='-NOTInon-'),sg.Button("RIGHT",k='1r')]),
        c([sg.Button("DOWN",k='1d')]),
        [sg.Text("")],
        c([sg.Button("Zoom in",k='1zi'),sg.Button("Zoom out",k='1zo')]),
        [sg.Text("")],
        c([sg.Button("Make image B&W",s=19)]),
        [sg.Text("")],
        ]
        
    layoutCOL3 = [
        [sg.Text("")],
        c([sg.Input(key='ICONnew',default_text=NOTI_inew,visible=False),sg.FileBrowse(s=8),sg.Button("Default",s=8,k='DEF2')]),
        c([sg.Button("Capture mask",k='capture2',s=16)]),
        [sg.Text("")],
        c([sg.Button("<-- Copy this image",k='CopyBtoA',s=19)]),
        c([sg.Button("<-- Copy image position",k='copy2',s=21)]),
        c([sg.Button("Reset image position",k='rip2',s=17)]),
        [sg.Text("")],
        c([sg.Button("UP",k='2u')]),
        c([sg.Button("LEFT",k='2l'),sg.Graph((120,110), (0,0), (120,110), key='-NOTInew-'),sg.Button("RIGHT",k='2r')]),
        c([sg.Button("DOWN",k='2d')]),
        [sg.Text("")],
        c([sg.Button("Zoom in",k='2zi'),sg.Button("Zoom out",k='2zo')]),
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("")],
        ]

    layoutCOL4 = [
        [sg.Text("")],
        c([sg.Button("OK",s=10),sg.Text("     "),sg.Button("Cancel",s=10)]),
        [sg.Text("")],
        ]
    
    layoutCOL = [
        [sg.Column(layoutCOL1), sg.VerticalSeparator(), sg.VerticalSeparator(), sg.Column(layoutCOL2), sg.Column(layoutCOL3)],
        [sg.HorizontalSeparator()],
        c([sg.Column(layoutCOL4)])
        ]
        
    layoutCOLx = [[sg.Column(layoutCOL)]]    
    windowCOL = sg.Window('Select Noticication Options', layoutCOLx, transparent_color='#000001',no_titlebar=True, keep_on_top=True, grab_anywhere=True,    background_color='#015BBB',margins=(0,0))
    window.hide()
    SCREEN = ('UPDADED')
    NEW_File = 0
    HH1,HH2=120,120
    WW1,WW2=110,110
    graph = windowCOL['-NOTInon-']
    graph2 = windowCOL['-NOTInew-']
    SAVE = 0

    while True:
        eventC, valuesC = windowCOL.read(10)

        if eventC=='CopyAtoB':
            if os.path.isfile("assets\preview\TEMP\ICONno.png"):
                with open("assets\preview\TEMP\ICONno.png", 'rb') as src_file:
                    with open("assets\preview\TEMP\clonedA.png", 'wb') as dest_file:
                        dest_file.write(src_file.read())
            windowCOL['ICONnew'].update ("assets\preview\TEMP\clonedA.png")
            CUSTOM_CHANGE=2
            
        if eventC=='CopyBtoA':
            if os.path.isfile("assets\preview\TEMP\ICONnew.png"):
                with open("assets\preview\TEMP\ICONnew.png", 'rb') as src_file:
                    with open("assets\preview\TEMP\clonedB.png", 'wb') as dest_file:
                        dest_file.write(src_file.read())
            windowCOL['ICONno'].update ("assets\preview\TEMP\clonedB.png")
            CUSTOM_CHANGE=1

        if eventC=='capture1':
            if cm1==0:
                cm1=1
                NOTI_inon = "assets\IconBuilder\Colors\Snapshot.png"
                windowCOL['ICONno'].update ("assets\IconBuilder\Colors\Snapshot.png")
                windowCOL['capture1'].update (text='Save snapshot',button_color=('Black','DarkOrange'))
                H1,V1=0,110
                HH1=120
                CUSTOM_CHANGE=1
            else:
                cm1=0
                bbox= graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
                ImageGrab.grab(bbox=bbox).save('assets\preview\TEMP\LAnoteno_def.png')
                windowCOL['ICONno'].update ("assets\preview\TEMP\LAnoteno_def.png")
                windowCOL['capture1'].update (text='Capture mask',button_color=default_button)
                
        if eventC=='capture2':
            if cm2==0:
                cm2=1
                NOTI_inew = "assets\IconBuilder\Colors\Snapshot.png"
                windowCOL['ICONnew'].update ("assets\IconBuilder\Colors\Snapshot.png")
                windowCOL['capture2'].update (text='Save snapshot',button_color=('Black','DarkOrange'))
                H2,V2=0,110
                HH2=120
                CUSTOM_CHANGE=2
            else:
                cm2=0
                bbox = graph2.Widget.winfo_rootx(), graph2.Widget.winfo_rooty(), graph2.Widget.winfo_rootx() + graph2.Widget.winfo_width(), graph2.Widget.winfo_rooty() + graph2.Widget.winfo_height()
                ImageGrab.grab(bbox=bbox).save('assets\preview\TEMP\LAnotenew_def.png')
                windowCOL['ICONnew'].update ("assets\preview\TEMP\LAnotenew_def.png")
                windowCOL['capture2'].update (text='Capture mask',button_color=default_button)
                
        if eventC=='copy1':
            H2,V2,HH2 = H1,V1,HH1
            SCREEN = 'UPDADED'
            
        if eventC=='copy2':
            H1,V1,HH1 = H2,V2,HH2
            SCREEN = 'UPDADED'

        if eventC=='DEF1':
            NOTI_inon = "assets/preview/default/LAnoteno_def.png"
            windowCOL['ICONno'].update ("assets/preview/default/LAnoteno_def.png")
            H1,V1=0,110
            HH1=120
            CUSTOM_CHANGE=1
            
        if eventC=='DEF2':
            NOTI_inew = "assets/preview/default/LAnotenew_def.png"
            windowCOL['ICONnew'].update ("assets/preview/default/LAnotenew_def.png")
            H2,V2=0,110
            HH2=120
            CUSTOM_CHANGE=2

        if eventC=='rip1':
            H1,V1=0,110
            HH1=120
            CUSTOM_CHANGE=1

        if eventC=='rip2':
            H2,V2=0,110
            HH2=120
            CUSTOM_CHANGE=2
       
        if not valuesC['ICONno'] == old_NOTI_inon:
            CUSTOM_CHANGE=1
            
        if not valuesC['ICONnew'] == old_NOTI_inew:
            CUSTOM_CHANGE=2
            
        if CUSTOM_CHANGE==1:
            if not old_NOTI_inon == valuesC['ICONno']:
                H1,V1=0,110
                HH1=120
            old_NOTI_inon = valuesC['ICONno']
            NOTI_inon = valuesC['ICONno']
            convINON_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\ICONno.png" -max-height {} -keep-ratio yes -force yes').format(NOTI_inon,HH1)
            convINON_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\ICONno.png" -o "assets\preview\TEMP\ICONno.png"')
            os.system(convINON_1a)
            os.system(convINON_1b)
            if Path(NOTI_inon).is_file():
                NOTI_inon = "assets\preview\TEMP\ICONno.png"
            else:
                NOTI_inon = "assets/preview/default/LAnoteno_def.png"
            CUSTOM_CHANGE=0
            SCREEN = ('UPDADED')

        if CUSTOM_CHANGE==2:
            if not old_NOTI_inew == valuesC['ICONnew']:
                H2,V2=0,110
                HH2=120
            old_NOTI_inew = valuesC['ICONnew']
            NOTI_inew = valuesC['ICONnew']
            convINEW_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\ICONnew.png" -max-height {} -keep-ratio yes -force yes').format(NOTI_inew,HH2)
            convINEW_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\ICONnew.png" -o "assets\preview\TEMP\ICONnew.png"')
            os.system(convINEW_1a)
            os.system(convINEW_1b)
            if Path(NOTI_inew).is_file():
                NOTI_inew = "assets\preview\TEMP\ICONnew.png"
            else:
                NOTI_inew = "assets/preview/default/LAnotenew_def.png"
            CUSTOM_CHANGE=0
            SCREEN = ('UPDADED')

        if SAVE == 2 : eventC = 'OKx'

        if SCREEN == ('UPDADED'):
            windowCOL['-NOTInon-'].erase()
            windowCOL['-NOTInew-'].erase()
            windowCOL['-NOTInon-'].draw_image(filename=NOTI_inon,location=(H1,V1))
            windowCOL['-NOTInew-'].draw_image(filename=NOTI_inew,location=(H2,V2))
            if SAVE == 0:
                windowCOL['-NOTInon-'].draw_image(filename=NOTI_imsk,location=(0,110))
                windowCOL['-NOTInew-'].draw_image(filename=NOTI_imsk,location=(0,110))
            if SAVE == 1:
                SAVE = 2
            SCREEN = 0
        
        if eventC == 'Make image B&W':
            cmdline = ('assets\convert assets\preview\TEMP\ICONno.png -colorspace Gray assets\preview\TEMP\ICONno.png')
            os.system(cmdline)
            SCREEN = 'UPDADED'
        
        if eventC == '1u':
            V1 = V1 + 2
            SCREEN = ('UPDADED')
        if eventC == '1d':
            V1 = V1 - 2
            SCREEN = ('UPDADED')
        if eventC == '1l':
            H1 = H1 - 2
            SCREEN = ('UPDADED')
        if eventC == '1r':
            H1 = H1 + 2
            SCREEN = ('UPDADED')
            
        if eventC == '1zo':
            V1 = V1 - 5
            HH1 = HH1 - 10
            CUSTOM_CHANGE=1
            SCREEN = ('UPDADED')
        if eventC == '1zi':
            V1 = V1 + 5
            HH1 = HH1 + 10
            CUSTOM_CHANGE=1
            SCREEN = ('UPDADED')
            
        if eventC == '2u':
            V2 = V2 + 2
            SCREEN = ('UPDADED')
        if eventC == '2d':
            V2 = V2 - 2
            SCREEN = ('UPDADED')
        if eventC == '2l':
            H2 = H2 - 2
            SCREEN = ('UPDADED')
        if eventC == '2r':
            H2 = H2 + 2
            SCREEN = ('UPDADED')
            
        if eventC == '2zo':
            V2 = V2 - 5
            HH2 = HH2 - 10
            CUSTOM_CHANGE=2
            SCREEN = ('UPDADED')
        if eventC == '2zi':
            V2 = V2 + 5
            HH2 = HH2 + 10
            CUSTOM_CHANGE=2
            SCREEN = ('UPDADED')            

        if eventC == sg.WIN_CLOSED or eventC == 'Cancel':
            windowCOL.close()
            window.UnHide()
            break
            
        if eventC == 'BAR_BLACK':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_RED':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_ORANGE':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_YELLOW':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(0)
        if eventC == 'BAR_GREEN':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(0)        
        if eventC == 'BAR_CYAN':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_BLUE':
            windowCOL['TBr'].update(0)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_PURPLE':
            windowCOL['TBr'].update(125)
            windowCOL['TBg'].update(0)
            windowCOL['TBb'].update(125)
        if eventC == 'BAR_PINK':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(125)
            windowCOL['TBb'].update(255)
        if eventC == 'BAR_WHITE':
            windowCOL['TBr'].update(255)
            windowCOL['TBg'].update(255)
            windowCOL['TBb'].update(255)
        if eventC == 'TXT_BLACK':
            windowCOL['NOT_TX_r'].update(0)
            windowCOL['NOT_TX_g'].update(0)
            windowCOL['NOT_TX_b'].update(0)
        if eventC == 'TXT_RED':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(0)
            windowCOL['NOT_TX_b'].update(0)
        if eventC == 'TXT_ORANGE':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(125)
            windowCOL['NOT_TX_b'].update(0)
        if eventC == 'TXT_YELLOW':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(255)
            windowCOL['NOT_TX_b'].update(0)
        if eventC == 'TXT_GREEN':
            windowCOL['NOT_TX_r'].update(0)
            windowCOL['NOT_TX_g'].update(125)
            windowCOL['NOT_TX_b'].update(0)        
        if eventC == 'TXT_CYAN':
            windowCOL['NOT_TX_r'].update(0)
            windowCOL['NOT_TX_g'].update(255)
            windowCOL['NOT_TX_b'].update(255)
        if eventC == 'TXT_BLUE':
            windowCOL['NOT_TX_r'].update(0)
            windowCOL['NOT_TX_g'].update(0)
            windowCOL['NOT_TX_b'].update(255)
        if eventC == 'TXT_PURPLE':
            windowCOL['NOT_TX_r'].update(125)
            windowCOL['NOT_TX_g'].update(0)
            windowCOL['NOT_TX_b'].update(125)
        if eventC == 'TXT_PINK':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(125)
            windowCOL['NOT_TX_b'].update(255)
        if eventC == 'TXT_WHITE':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(255)
            windowCOL['NOT_TX_b'].update(255)
        if eventC == 'Defaults':
            windowCOL['NOT_TX_r'].update(255)
            windowCOL['NOT_TX_g'].update(255)
            windowCOL['NOT_TX_b'].update(255)
            windowCOL['TBr'].update(42)
            windowCOL['TBg'].update(42)
            windowCOL['TBb'].update(42  )
        
        NOT_TX_RED = int(valuesC['NOT_TX_r'])
        NOT_TX_GRE = int(valuesC['NOT_TX_g'])
        NOT_TX_BLU = int(valuesC['NOT_TX_b'])
        NOT_TXTcOL = NOT_TX_RED,NOT_TX_GRE,NOT_TX_BLU
        NOT_TXTc = rgb_to_hex(NOT_TXTcOL)
        windowCOL['TITLECOL'].update(text_color=(NOT_TXTc))
        
        NOT_BOX_RED = int(valuesC['TBr'])
        NOT_BOX_GRE = int(valuesC['TBg'])
        NOT_BOX_BLU = int(valuesC['TBb'])
        NOT_BOXcOL = NOT_BOX_RED,NOT_BOX_GRE,NOT_BOX_BLU
        NOT_BOXc = rgb_to_hex(NOT_BOXcOL)
        windowCOL['TITLECOL'].update(background_color=(NOT_BOXc))

        if eventC == 'OK':
            SCREEN = 'UPDADED'
            SAVE = 1
                        
        if eventC == 'OKx':
            
            NOT_TX_r = NOT_TX_RED
            NOT_TX_g = NOT_TX_GRE
            NOT_TX_b = NOT_TX_BLU
            TBr = NOT_BOX_RED
            TBg = NOT_BOX_GRE
            TBb = NOT_BOX_BLU            
            NOT_BOX_BOX_COL = NOT_BOXc
            NOT_BOX_TXT_COL = NOT_TXTc
            
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            bbox2 = graph2.Widget.winfo_rootx(), graph2.Widget.winfo_rooty(), graph2.Widget.winfo_rootx() + graph2.Widget.winfo_width(), graph2.Widget.winfo_rooty() + graph2.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets\preview\TEMP\LAnoteno_def.png')
            convINON_1a = ('call assets\scale.bat -source "assets\preview\TEMP\LAnoteno_def.png" -target "assets\preview\TEMP\LAnoteno.png" -max-height 37 -keep-ratio yes -force yes')
            convINON_1b = ('assets\convert "assets\preview\TEMP\LAnoteno.png" "assets\mask_not.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\LAnoteno.png')
            os.system(convINON_1a)
            os.system(convINON_1b)
            ImageGrab.grab(bbox=bbox2).save('assets\preview\TEMP\LAnotenew_def.png')
            convINEW_1a = ('call assets\scale.bat -source "assets\preview\TEMP\LAnotenew_def.png" -target "assets\preview\TEMP\LAnotenew.png" -max-height 37 -keep-ratio yes -force yes')
            convINEW_1b = ('assets\convert "assets\preview\TEMP\LAnotenew.png" "assets\mask_not.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\LAnotenew.png')
            os.system(convINEW_1a)
            os.system(convINEW_1b)
            SCREEN = ('UPDADED')
            windowCOL.close()
            window.UnHide()
            break

def EXTRA_TOOLS():
    global File1
    global File2
    global VitaPATH
    global Swapped
    fileCHANGE=0
    
    convINON_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\LS_Grab.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(File1)
    convINON_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\LS_Grab.png" -o "assets\preview\TEMP\preview_ls.png"')
    os.system(convINON_1a)
    os.system(convINON_1b)
    convINON_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\LA_Grab.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(File2)
    convINON_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\LA_Grab.png" -o "assets\preview\TEMP\preview_la.png"')
    os.system(convINON_1a)
    os.system(convINON_1b)
    
    layoutTOOLS_Top = [
        c([sg.Text("")]),
        c([sg.Text("For a custom theme to be submitted and accepted on the"),sg.Text("'PSVita Custom Themes Repository'",enable_events=True, key='-LINK-', text_color='yellow'),sg.Text("<-- click here to google")]),
        c([sg.Text("you must first install your theme and take a snapshot of the Lockscreen and any Livearea page.. To do this, just")]),
        c([sg.Text("press both the 'PS button' and 'START' at the same time, first on the Lockscreen, then any Livearea page")]),
        c([sg.Text("if you get an error message, try rebooting the vita, or connect then disconnect VitaShell")]),
        c([sg.Text("")]),
        c([sg.Text("NOTE : For best results, try rearanging your bubbles to help show off your theme.")]),
        c([sg.Text("")]),
        c([sg.Text("This app 'should' show the last 2 snapshots taken and display them here. Check to make sure that the screens shown")]),
        c([sg.Text("are correct and in the correct place.. If you dont see your snapshot images, close this window and reopen it.")]),
        c([sg.Text("")]),
        ]
    
    layoutTOOLS_Right = [
        [sg.Text("LIVEAREA"),sg.Stretch()],
        c([(sg.Graph((480,272), (0,0), (480,272), key='LA_Preview_Grab'))]),
        ]

    layoutTOOLS_Left = [
        [sg.Text("LOCKSCREEN"),sg.Stretch()],
        c([(sg.Graph((480,272), (0,0), (480,272), key='LS_Preview_Grab'))]),
        ]
    
    layoutTOOLS = [
        c([sg.Column(layoutTOOLS_Top)]),
        [sg.HorizontalSeparator()],
        [sg.Column(layoutTOOLS_Left),sg.VerticalSeparator(),sg.Column(layoutTOOLS_Right)],
        [sg.Stretch(),sg.Input(key='-LSPRE-',default_text=File1,visible=False),sg.FileBrowse(initial_folder=VitaPATH,file_types=(('Images', '*.png *.jpg'),('ALL','*.* *'))),sg.Stretch(),sg.Button("<-----    SWAP IMAGES    ----->"),sg.Stretch(),sg.Input(key='-LAPRE-',default_text=File2,visible=False),sg.FileBrowse(initial_folder=VitaPATH,file_types=(('Images', '*.png *.jpg'),('ALL','*.* *'))),sg.Stretch()],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        c([sg.Button("Export",button_color=('yellow','black'),s=12),sg.Text("",s=2),sg.Button("Cancel",s=12)]),
        [sg.Text("")],
        ]
        
    layoutTOOLSx = [[sg.Column(layoutTOOLS)]]
    windowTOOLS = sg.Window('Extra Tools', layoutTOOLSx, no_titlebar=True, keep_on_top=True, grab_anywhere=True, background_color='#015BBB',margins=(0,0))
    window.hide()
    SCREEN = "UPDADED"
    LSPRE_old = File1
    LAPRE_old = File2
    
    while True:
        eventT, valuesT = windowTOOLS.read(5)
        
        if eventT == sg.WIN_CLOSED or eventT == 'Cancel':
            windowTOOLS.close()
            window.UnHide()
            break

        if eventT == 'Export':
            if not os.path.exists('Created Themes'):
                os.makedirs('Created Themes')
            ThemePATH=('Created Themes\\'+ThemeName)
            print("ThemePATH = ",ThemePATH)
            if not os.path.exists(ThemePATH):
                os.makedirs(ThemePATH)
            if not os.path.exists('Exported'):
                os.makedirs('Exported')
            ThemePATH=(ThemePATH+'\\')
            targetfile1=(ThemePATH+'preview_lockscreen.png')
            targetfile2=(ThemePATH+'preview_page.png')
            File1=('assets\\preview\\TEMP\\preview_ls.png')
            File2=('assets\\preview\\TEMP\\preview_la.png')
            cmdline1=('copy "{}" "{}"').format(File1,targetfile1)
            cmdline2=('copy "{}" "{}"').format(File2,targetfile2)
            cmdline3=('cd "Created Themes" && cd "{}" && ..\..\\assets\\7z a "..\\..\\Exported\\{}.zip" -x!theme.ini && cd.. && cd..').format(ThemeName,ThemeName)
            os.system(cmdline1)
            os.system(cmdline2)
            os.system(cmdline3)
            windowTOOLS.close()
            popuptxt = ("\nYour theme has been exported\nand was saved as : -\n\n'/Exported/"+ThemeName+".zip'\n")
            sg.popup(popuptxt,title='Complete.!')
            window.UnHide()
        
        if eventT == '-LINK-':
            webbrowser.open_new_tab('https://www.google.com/search?q=PSVita+Custom+Themes+Repository')
        
        if SCREEN=="UPDADED":
            SCREEN=""
            windowTOOLS['LS_Preview_Grab'].draw_image(filename="assets\preview\TEMP\preview_ls.png", location=(0,272))
            windowTOOLS['LA_Preview_Grab'].draw_image(filename="assets\preview\TEMP\preview_la.png", location=(0,272))

        if eventT=="<-----    SWAP IMAGES    ----->":
            FileT=File1
            File1=File2
            File2=FileT
            if Swapped==0:
                Swapped=1
            else:
                Swapped=0
            fileCHANGE=1

        if not valuesT['-LSPRE-'] == LSPRE_old:
            LSPRE_old=valuesT['-LSPRE-']
            File1=valuesT['-LSPRE-']
            fileCHANGE=1

        if not valuesT['-LAPRE-'] == LAPRE_old:
            LAPRE_old=valuesT['-LAPRE-']
            File2=valuesT['-LAPRE-']
            fileCHANGE=1
            
        if fileCHANGE==1:
            convINON_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\LS_Grab.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(File1)
            convINON_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\LS_Grab.png" -o "assets\preview\TEMP\preview_ls.png"')
            os.system(convINON_1a)
            os.system(convINON_1b)
            convINON_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\LA_Grab.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(File2)
            convINON_1b = ('assets\pngquant.exe -f "assets\preview\TEMP\LA_Grab.png" -o "assets\preview\TEMP\preview_la.png"')
            os.system(convINON_1a)
            os.system(convINON_1b)
            fileCHANGE=0
            SCREEN="UPDADED"


def MoreTOOLS_CHECK():
    global bypass
    global VitaPATH
    global VitaDRIVE
    global Swapped
    global File1
    global File2
    global ThemeName
    
    SCREEN="UPDADED"
    if bypass==1:
        VitaDRIVE=('Not Found')
    else:
        VitaDRIVE=("Not Detected")        
    if os.path.exists("D:\SceIoTrash"):
        VitaDRIVE=("D")
    if os.path.exists("E:\SceIoTrash"):
        VitaDRIVE=("E")
    if os.path.exists("F:\SceIoTrash"):
        VitaDRIVE=("F")
    if os.path.exists("G:\SceIoTrash"):
        VitaDRIVE=("G")
    if os.path.exists("H:\SceIoTrash"):
        VitaDRIVE=("H")
    if os.path.exists("I:\SceIoTrash"):
        VitaDRIVE=("I")
    if os.path.exists("J:\SceIoTrash"):
        VitaDRIVE=("J")
    if os.path.exists("K:\SceIoTrash"):
        VitaDRIVE=("K")
    if os.path.exists("L:\SceIoTrash"):
        VitaDRIVE=("L")
    if os.path.exists("M:\SceIoTrash"):
        VitaDRIVE=("M")
    if os.path.exists("N:\SceIoTrash"):
        VitaDRIVE=("N")
    if os.path.exists("O:\SceIoTrash"):
        VitaDRIVE=("O")
    if os.path.exists("P:\SceIoTrash"):
        VitaDRIVE=("P")
    if os.path.exists("Q:\SceIoTrash"):
        VitaDRIVE=("Q")
    if os.path.exists("R:\SceIoTrash"):
        VitaDRIVE=("R")
    if os.path.exists("S:\SceIoTrash"):
        VitaDRIVE=("S")
    if os.path.exists("T:\SceIoTrash"):
        VitaDRIVE=("T")
    if os.path.exists("U:\SceIoTrash"):
        VitaDRIVE=("U")
    if os.path.exists("V:\SceIoTrash"):
        VitaDRIVE=("V")
    if os.path.exists("W:\SceIoTrash"):
        VitaDRIVE=("W")
    if os.path.exists("X:\SceIoTrash"):
        VitaDRIVE=("X")
    if os.path.exists("Y:\SceIoTrash"):
        VitaDRIVE=("Y")
    if os.path.exists("Z:\SceIoTrash"):
        VitaDRIVE=("Z")
    if not VitaDRIVE==("Not Detected"):
        if not bypass==1:
            VitaPATH = (VitaDRIVE+":/picture/screenshot")
            last_two_files = find_last_two_files_created(VitaPATH)
            if Swapped==1:
                File2, File1 = last_two_files
            else:
                File1, File2 = last_two_files
        else:
            bypass=0
            VitaPATH=('')
            ThemeFILE1=('Created Themes/'+ThemeName+'/preview_lockscreen.png')
            ThemeFILE2=('Created Themes/'+ThemeName+'/preview_page.png')
            if os.path.isfile(ThemeFILE1):
                File1=(ThemeFILE1)
            else:
                File1=('assets/preview/default/defaultLS.png')
            if os.path.isfile(ThemeFILE2):
                File2=(ThemeFILE2)
            else:
                File2=('assets/preview/default/defaultLA.png')
        EXTRA_TOOLS()
    else:
        MoreTOOLS_NO()

def MoreTOOLS_NO():
    global Swapped
    global VitaPATH
    global VitaDRIVE
    global bypass
    global retry
    global File1
    global File2
    
    layoutTOOLS = [
        [sg.Text("")],
        c([sg.Text("VITA not automatically detected.!",s=50,justification='c',font=('Helvetica', 16), text_color='Red',)]),
        c([sg.Text("",s=50,justification='c')]),
        c([sg.Text("- Please connect your Vita to a USB port and open VitaShell",s=50,justification='l')]),
        c([sg.Text("- Press 'START' and check that you have USB mode selected",s=50,justification='l')]),
        c([sg.Text("- If you are using an SD2VITA, make sure this is also set and",s=50,justification='l')]),
        c([sg.Text("   you are not selected to the Sony 'Memory Card'..",s=50,justification='l')]),
        c([sg.Text("")]),
        c([sg.Text("USB device ",s=20,justification='r',text_color='grey',background_color='black',pad=(0,0)),sg.Text(" sd2vita",s=20,justification='l',text_color='lightgreen',background_color='black',pad=(0,0))]),
        c([sg.Text("SELECT button ",s=20,justification='r',text_color='grey',background_color='black',pad=(0,0)),sg.Text(" USB",s=20,justification='l',text_color='lightgreen',background_color='black',pad=(0,0))]),
        c([sg.Text("")]),
        c([sg.Text("Press 'START' again to close the settings and press 'SELECT'",s=50,justification='c')]),
        c([sg.Text("this should begin the USB data transfer connection..",s=50,justification='c')]),
        [sg.Text("")],
        c([sg.Button("Continue",s=12),sg.Text("",s=2),sg.Button("Cancel",s=12)]),
        [sg.Text("")],
        ]
        
    layoutTOOLSx = [[sg.Column(layoutTOOLS)]]
    windowTOOLS = sg.Window('Extra Tools', layoutTOOLSx, no_titlebar=True, keep_on_top=True, grab_anywhere=True, background_color='Red',margins=(0,0))

    while True:
        eventT, valuesT = windowTOOLS.read(5)
        
        VitaDRIVE=("Not Detected")
        if os.path.exists("D:\SceIoTrash"):
            VitaDRIVE=("D")
        if os.path.exists("E:\SceIoTrash"):
            VitaDRIVE=("E")
        if os.path.exists("F:\SceIoTrash"):
            VitaDRIVE=("F")
        if os.path.exists("G:\SceIoTrash"):
            VitaDRIVE=("G")
        if os.path.exists("H:\SceIoTrash"):
            VitaDRIVE=("H")
        if os.path.exists("I:\SceIoTrash"):
            VitaDRIVE=("I")
        if os.path.exists("J:\SceIoTrash"):
            VitaDRIVE=("J")
        if os.path.exists("K:\SceIoTrash"):
            VitaDRIVE=("K")
        if os.path.exists("L:\SceIoTrash"):
            VitaDRIVE=("L")
        if os.path.exists("M:\SceIoTrash"):
            VitaDRIVE=("M")
        if os.path.exists("N:\SceIoTrash"):
            VitaDRIVE=("N")
        if os.path.exists("O:\SceIoTrash"):
            VitaDRIVE=("O")
        if os.path.exists("P:\SceIoTrash"):
            VitaDRIVE=("P")
        if os.path.exists("Q:\SceIoTrash"):
            VitaDRIVE=("Q")
        if os.path.exists("R:\SceIoTrash"):
            VitaDRIVE=("R")
        if os.path.exists("S:\SceIoTrash"):
            VitaDRIVE=("S")
        if os.path.exists("T:\SceIoTrash"):
            VitaDRIVE=("T")
        if os.path.exists("U:\SceIoTrash"):
            VitaDRIVE=("U")
        if os.path.exists("V:\SceIoTrash"):
            VitaDRIVE=("V")
        if os.path.exists("W:\SceIoTrash"):
            VitaDRIVE=("W")
        if os.path.exists("X:\SceIoTrash"):
            VitaDRIVE=("X")
        if os.path.exists("Y:\SceIoTrash"):
            VitaDRIVE=("Y")
        if os.path.exists("Z:\SceIoTrash"):
            VitaDRIVE=("Z")
        if not VitaDRIVE==("Not Detected"):
            VitaPATH = (VitaDRIVE+":/picture/screenshot")
            last_two_files = find_last_two_files_created(VitaPATH)
            if Swapped==1:
                File2, File1 = last_two_files
            else:
                File1, File2 = last_two_files
            retry=1
            windowTOOLS.close()
            break
        
        if eventT == sg.WIN_CLOSED or eventT == 'Cancel':
            windowTOOLS.close()
            break
        if eventT == 'Continue':
            bypass=1
            retry=1
            windowTOOLS.close()
            break
            
def GenerateTHEME_image():
    global ThemeName
    global box_coordinates
    global txt_coordinates
    global GEN_continue
    global ThemePATH
    slideBOX='#000000'
    slideBOXr=0
    slideBOXg=0
    slideBOXb=0
    slideTXT='#FFFFFF'
    slideTXTr=255
    slideTXTg=255
    slideTXTb=255
    fontSZE=9    
    cm1=0
    ThemeNameSize=(len(ThemeName))
    ThemeNameGT=ThemeName
    
    ThemeTHUMB=('Created Themes/'+ThemeName+'/preview_thumbnail.png')
    if os.path.isfile(ThemeTHUMB):
        File1=(ThemeTHUMB)
        File1=File1.replace('/','\\')
        cmdline1 = ('copy /y "{}" "assets/preview/TEMP/preview.png"').format(File1)
        os.system(cmdline1)
    else:
        File1=('generated')
        cmdline1=('assets\convert "assets/preview/TEMP/Page1.png" "assets/preview/TEMP/Page2.png" +append assets/preview/TEMP/preview-a.png')
        cmdline2=('assets\convert "assets/preview/TEMP/Page3.png" "assets/preview/TEMP/Page4.png" +append assets/preview/TEMP/preview-b.png')
        cmdline3=('assets\convert "assets/preview/TEMP/preview-a.png" "assets/preview/TEMP/preview-b.png" -append "assets/preview/TEMP/preview-c.png"')
        cmdline4=('call assets\scale.bat -source "assets/preview/TEMP/preview-c.png" -target "assets/preview/TEMP/preview.png" -max-height 128 -max-width 226 -keep-ratio no -force yes')
        cmdline5=('assets\pngquant.exe -f "assets/preview/TEMP/preview.png" -o "assets/preview/TEMP/preview.png"')

        verified=1
        if not Path('assets/preview/TEMP/Page1.png').is_file(): verified=0
        if not Path('assets/preview/TEMP/Page2.png').is_file(): verified=0
        if not Path('assets/preview/TEMP/Page3.png').is_file(): verified=0
        if not Path('assets/preview/TEMP/Page4.png').is_file(): verified=0
        if verified==1:
            os.system(cmdline1)
            os.system(cmdline2)
            os.system(cmdline3)
            os.system(cmdline4)
            os.system(cmdline5)
        
        if ThemeNameSize<=9: fontSZE=23
        if ThemeNameSize>9 and ThemeNameSize<12: fontSZE=20
        if ThemeNameSize>11 and ThemeNameSize<=14: fontSZE=18
        if ThemeNameSize>=15 and ThemeNameSize<17: fontSZE=14
        if ThemeNameSize>16 and ThemeNameSize<21: fontSZE=12
        if ThemeNameSize>20 and ThemeNameSize<25: fontSZE=11
        if ThemeNameSize>24 and ThemeNameSize<31: fontSZE=10

    layoutGT_1 = [
        [sg.Slider(range=(0,96),orientation='v',default_value=48,s=(6,15),k='-slideV-',enable_events=True)]
        ]

    layoutGT_2 = [
        [sg.Text("")],
        c([sg.Text('Thumbnail image preview',font=("Helvetica", 14),text_color='yellow')]),
        c([(sg.Graph((226,128), (0,0), (226,128), key='LOGO_Preview'))]),
        c([sg.Slider(range=(0,226),orientation='h',default_value=113,s=(20,15),k='-slideH-',enable_events=True)]),
        [sg.Text("")],
        ]

    layoutGT_3 = [
        [sg.Text("")],
        c([sg.Checkbox('CUSTOM TITLEBAR', default=True, key='-titlebarTXT-', enable_events=True,)]),
        [sg.HorizontalSeparator()],
        c([sg.Input(ThemeNameGT,s=20,k='tname'),sg.Stretch(),sg.Text("Size : "),sg.Slider(range=(9,30),orientation='h',default_value=fontSZE,s=(6,15),k='-fntsize-',enable_events=True)]),
        [sg.Text("R :"),sg.Slider(range=(0,255), orientation='h',default_value=slideBOXr, s=(6,15), k='-slide1-',enable_events=True), sg.Text("G :"),sg.Slider(range=(0,255), orientation='h',default_value=slideBOXg, s=(6,15), k='-slide2-',enable_events=True),sg.Text("B :"),sg.Slider(range=(0,255), orientation='h',default_value=slideBOXb, s=(6,15), k='-slide3-',enable_events=True)],
        c([sg.Button("TXT_BLACK",s=1,button_color=('Black','Black')),sg.Button("TXT_RED",s=1,button_color=('Red','Red')),sg.Button("TXT_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("TXT_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("TXT_GREEN",s=1,button_color=('Green','Green')),sg.Button("TXT_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("TXT_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("TXT_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("TXT_PINK",s=1,button_color=('Pink','Pink')),sg.Button("TXT_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        c([sg.Checkbox('USE COLOR BAR', default=True, key='-titlebarCOL-', enable_events=True,)]),
        [sg.HorizontalSeparator()],
        [sg.Text("R :"),sg.Slider(range=(0,255), orientation='h',default_value=slideTXTr, s=(6,15), k='-slidea-',enable_events=True), sg.Text("G :"),sg.Slider(range=(0,255), orientation='h',default_value=slideTXTg, s=(6,15), k='-slideb-',enable_events=True),sg.Text("B :"),sg.Slider(range=(0,255), orientation='h',default_value=slideTXTb, s=(6,15), k='-slidec-',enable_events=True)],
        c([sg.Button("BAR_BLACK",s=1,button_color=('Black','Black')),sg.Button("BAR_RED",s=1,button_color=('Red','Red')),sg.Button("BAR_ORANGE",s=1,button_color=('Orange','Orange')),sg.Button("BAR_YELLOW",s=1,button_color=('Yellow','Yellow')),
        sg.Button("BAR_GREEN",s=1,button_color=('Green','Green')),sg.Button("BAR_CYAN",s=1,button_color=('Cyan','Cyan')), sg.Button("BAR_BLUE",s=1,button_color=('Blue','Blue')),sg.Button("BAR_PURPLE",s=1,button_color=('Purple','Purple')),
        sg.Button("BAR_PINK",s=1,button_color=('Pink','Pink')),sg.Button("BAR_WHITE",s=1,button_color=('White','White')),]),
        [sg.Text("")],
        ]

    layoutGT_4 = [
        c([sg.Input(key='-LOGO-',default_text="x",visible=False),sg.FileBrowse("Browse for custom image",initial_folder="assets/preview/TEMP",file_types=(('Images', '*.png *.jpg'),('ALL','*.* *'))),sg.Button(" Use Auto Generated "),sg.Button("Capture mask",k='SCR_CAP')]),
        ]

    layoutGT_5 = [
        [sg.Text("")],
        c([sg.Button("- START -",button_color=('Yellow','Black'),s=15),sg.Text("  "),sg.Button("Cancel",s=15)]),
        [sg.Text("")],
        ]

    layoutGTfull = [[sg.Column(layoutGT_1),sg.Column(layoutGT_2),sg.Column(layoutGT_3)],
        [sg.HorizontalSeparator()],
        c([sg.Column(layoutGT_4)]),
        [sg.HorizontalSeparator()],
        c([sg.Column(layoutGT_5)]),]
        
    layoutGTx = [[sg.Column(layoutGTfull)]]
    windowGT = sg.Window('Generate Theme Image', layoutGTx, transparent_color='#000001', no_titlebar=True, keep_on_top=True, grab_anywhere=True, background_color='#015BBB',margins=(0,0),finalize=True)
    window.hide()
    SCREEN = 'UPDADED'
    graph = windowGT['LOGO_Preview']
    
    if not File1==('generated'):
        windowGT['-titlebarTXT-'].update(False)
        
    while True:
        eventGT, valuesGT = windowGT.read(5)

        if eventGT == 'BAR_BLACK':
            windowGT['-slidea-'].update(0)
            windowGT['-slideb-'].update(0)
            windowGT['-slidec-'].update(0)
            BARslide = (0,0,0)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'
        if eventGT == 'BAR_RED':
            windowGT['-slidea-'].update(255)
            windowGT['-slideb-'].update(0)
            windowGT['-slidec-'].update(0)
            BARslide = (255,0,0)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'
        if eventGT == 'BAR_ORANGE':
            windowGT['-slidea-'].update(255)
            windowGT['-slideb-'].update(125)
            windowGT['-slidec-'].update(0)
            BARslide = (255,125,0)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_YELLOW':
            windowGT['-slidea-'].update(255)
            windowGT['-slideb-'].update(255)
            windowGT['-slidec-'].update(0)
            BARslide = (255,255,0)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_GREEN':
            windowGT['-slidea-'].update(0)
            windowGT['-slideb-'].update(125)
            windowGT['-slidec-'].update(0)        
            BARslide = (0,125,0)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_CYAN':
            windowGT['-slidea-'].update(0)
            windowGT['-slideb-'].update(255)
            windowGT['-slidec-'].update(255)
            BARslide = (0,255,255)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_BLUE':
            windowGT['-slidea-'].update(0)
            windowGT['-slideb-'].update(0)
            windowGT['-slidec-'].update(255)
            BARslide = (0,0,255)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_PURPLE':
            windowGT['-slidea-'].update(125)
            windowGT['-slideb-'].update(0)
            windowGT['-slidec-'].update(125)
            BARslide = (125,0,125)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_PINK':
            windowGT['-slidea-'].update(255)
            windowGT['-slideb-'].update(125)
            windowGT['-slidec-'].update(255)
            BARslide = (255,125,255)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'            
        if eventGT == 'BAR_WHITE':
            windowGT['-slidea-'].update(255)
            windowGT['-slideb-'].update(255)
            windowGT['-slidec-'].update(255)
            BARslide = (255,255,255)
            slideBOX = rgb_to_hex(BARslide)
            SCREEN = 'UPDADED'
            
        if eventGT == 'TXT_BLACK':
            windowGT['-slide1-'].update(0)
            windowGT['-slide2-'].update(0)
            windowGT['-slide3-'].update(0)
            TXTslide = (0,0,0)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_RED':
            windowGT['-slide1-'].update(255)
            windowGT['-slide2-'].update(0)
            windowGT['-slide3-'].update(0)
            TXTslide = (255,0,0)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_ORANGE':
            windowGT['-slide1-'].update(255)
            windowGT['-slide2-'].update(125)
            windowGT['-slide3-'].update(0)
            TXTslide = (255,125,0)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_YELLOW':
            windowGT['-slide1-'].update(255)
            windowGT['-slide2-'].update(255)
            windowGT['-slide3-'].update(0)
            TXTslide = (255,255,0)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_GREEN':
            windowGT['-slide1-'].update(0)
            windowGT['-slide2-'].update(125)
            windowGT['-slide3-'].update(0)        
            TXTslide = (0,125,0)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_CYAN':
            windowGT['-slide1-'].update(0)
            windowGT['-slide2-'].update(255)
            windowGT['-slide3-'].update(255)
            TXTslide = (0,255,255)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_BLUE':
            windowGT['-slide1-'].update(0)
            windowGT['-slide2-'].update(0)
            windowGT['-slide3-'].update(255)
            TXTslide = (0,0,255)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_PURPLE':
            windowGT['-slide1-'].update(125)
            windowGT['-slide2-'].update(0)
            windowGT['-slide3-'].update(125)
            TXTslide = (125,0,125)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_PINK':
            windowGT['-slide1-'].update(255)
            windowGT['-slide2-'].update(125)
            windowGT['-slide3-'].update(255)
            TXTslide = (255,125,255)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
        if eventGT == 'TXT_WHITE':
            windowGT['-slide1-'].update(255)
            windowGT['-slide2-'].update(255)
            windowGT['-slide3-'].update(255)
            TXTslide = (255,255,255)
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'

        if eventGT == '-slide1-' or eventGT == '-slide2-' or eventGT == '-slide3-' or eventGT == '-slidea-' or eventGT == '-slideb-' or eventGT == '-slidec-':
            slideBOXr = valuesGT['-slidea-']
            slideBOXg = valuesGT['-slideb-']
            slideBOXb = valuesGT['-slidec-']
            slideTXTr = valuesGT['-slide1-']
            slideTXTg = valuesGT['-slide2-']
            slideTXTb = valuesGT['-slide3-']
            slideBOXr = int(slideBOXr)
            slideBOXg = int(slideBOXg)
            slideBOXb = int(slideBOXb)
            BOXslide = slideBOXr,slideBOXg,slideBOXb
            slideBOX = rgb_to_hex(BOXslide)
            slideTXTr = int(slideTXTr)
            slideTXTg = int(slideTXTg)
            slideTXTb = int(slideTXTb)
            TXTslide = slideTXTr,slideTXTg,slideTXTb
            slideTXT = rgb_to_hex(TXTslide)
            SCREEN = 'UPDADED'
            
        if eventGT == '-slideV-' or eventGT == '-slideH-' or eventGT == '-fntsize-':
            slideV= valuesGT['-slideV-']
            slideH= valuesGT['-slideH-']
            fontSZE= valuesGT['-fntsize-']
            fontSZE = int(fontSZE)
            box_coordinates = ((0,slideV),(226,slideV+32))
            txt_coordinates = (slideH,slideV+16) 
            SCREEN = 'UPDADED'

        if SCREEN=='UPDADED':
            windowGT['LOGO_Preview'].erase()
            if Path('assets/preview/TEMP/preview.png').is_file():
                windowGT['LOGO_Preview'].draw_image(filename='assets/preview/TEMP/preview.png',location=(0,128))
            if valuesGT['-titlebarTXT-'] == True:
                if valuesGT['-titlebarCOL-'] == True:
                    windowGT['LOGO_Preview'].draw_rectangle(*box_coordinates,fill_color=(slideBOX))
                windowGT['LOGO_Preview'].draw_text(ThemeNameGT,color=slideTXT,font=('Helvetica', fontSZE),location=txt_coordinates)
            SCREEN = "0"
                
        if not valuesGT['tname']==ThemeNameGT:
            ThemeNameGT = valuesGT['tname']
            ThemeNameSizeGT=(len(ThemeNameGT))
            if ThemeNameSizeGT<=9: fontSZE=23
            if ThemeNameSizeGT>9 and ThemeNameSizeGT<12: fontSZE=20
            if ThemeNameSizeGT>11 and ThemeNameSizeGT<=14: fontSZE=18
            if ThemeNameSizeGT>=15 and ThemeNameSizeGT<17: fontSZE=14
            if ThemeNameSizeGT>16 and ThemeNameSizeGT<21: fontSZE=12
            if ThemeNameSizeGT>20 and ThemeNameSizeGT<25: fontSZE=11
            if ThemeNameSizeGT>24 and ThemeNameSizeGT<31: fontSZE=10
            windowGT['-fntsize-'].update(fontSZE)
            SCREEN = "UPDADED"
        
        if eventGT == ('-titlebarCOL-') or eventGT == ('-titlebarTXT-'):
            SCREEN = 'UPDADED'

        if not valuesGT['-LOGO-'] == "x":
            LOGO = valuesGT['-LOGO-']
            windowGT['-LOGO-'].update("x")
            cmdlineA=('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/preview.png" -max-height 128 -max-width 226 -keep-ratio no -force yes').format(LOGO)
            cmdlineB=('assets\pngquant.exe -f "assets/preview/TEMP/preview.png" -o "assets/preview/TEMP/preview.png"')
            os.system(cmdlineA)
            os.system(cmdlineB)
            SCREEN = 'UPDADED'
        
        if eventGT == "SCR_CAP":
            if cm1==0:
                cm1=1
                windowGT['-titlebarTXT-'].update(False)
                windowGT['SCR_CAP'].update (text='Save snapshot',button_color=('Black','DarkOrange'))
                LOGO = "assets\IconBuilder\Colors\Snapshot.png"
                cmdlineA=('call assets\scale.bat -source {} -target "assets/preview/TEMP/preview.png" -max-height 128 -max-width 226 -keep-ratio no -force yes').format(LOGO)
                cmdlineB=('assets\pngquant.exe -f "assets/preview/TEMP/preview.png" -o "assets/preview/TEMP/preview.png"')
                os.system(cmdlineA)
                os.system(cmdlineB)
                SCREEN = 'UPDADED'
            else:
                cm1=0
                bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
                ImageGrab.grab(bbox=bbox).save('assets/preview/TEMP/preview.png')
                windowGT['SCR_CAP'].update (text='Capture mask',button_color=default_button)
                SCREEN = 'UPDADED'

        if eventGT == " Use Auto Generated ":
            cmdline1=('assets\convert "assets/preview/TEMP/Page1.png" "assets/preview/TEMP/Page2.png" +append assets/preview/TEMP/preview-a.png')
            cmdline2=('assets\convert "assets/preview/TEMP/Page3.png" "assets/preview/TEMP/Page4.png" +append assets/preview/TEMP/preview-b.png')
            cmdline3=('assets\convert "assets/preview/TEMP/preview-a.png" "assets/preview/TEMP/preview-b.png" -append "assets/preview/TEMP/preview-c.png"')
            cmdline4=('call assets\scale.bat -source "assets/preview/TEMP/preview-c.png" -target "assets/preview/TEMP/preview.png" -max-height 128 -max-width 226 -keep-ratio no -force yes')
            cmdline5=('assets\pngquant.exe -f "assets/preview/TEMP/preview.png" -o "assets/preview/TEMP/preview.png"')

            verified=1
            if not Path('assets/preview/TEMP/Page1.png').is_file(): verified=0
            if not Path('assets/preview/TEMP/Page2.png').is_file(): verified=0
            if not Path('assets/preview/TEMP/Page3.png').is_file(): verified=0
            if not Path('assets/preview/TEMP/Page4.png').is_file(): verified=0
            if verified==1:
                os.system(cmdline1)
                os.system(cmdline2)
                os.system(cmdline3)
                os.system(cmdline4)
                os.system(cmdline5)
            SCREEN = 'UPDADED'

        if eventGT == sg.WIN_CLOSED or eventGT == 'Cancel':
            windowGT.close()
            window.UnHide()
            break

        if eventGT == "- START -":
            if not os.path.exists('Created Themes'):
                os.makedirs('Created Themes')
            ThemePATH=('Created Themes/'+ThemeName)
            if not os.path.exists(ThemePATH):
                os.makedirs(ThemePATH)
            ThemePATH=(ThemePATH+'/')
            graph = windowGT['LOGO_Preview']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/preview/TEMP/preview_thumbnail.png')
            cmdline1 = ('assets\pngquant.exe -f "assets/preview/TEMP/preview_thumbnail.png" -o "{}preview_thumbnail.png"').format(ThemePATH)
            os.system(cmdline1)
            GEN_continue=1
            windowGT.close()
            window.UnHide()
            break

def GenerateTHEME():
    global event
    
    layoutGENERATE = [
        [sg.Text("")],
        c([sg.Text("You are about to overwrite files in the current theme",s=50,justification='c')]),
        [sg.Text("")],
        c([sg.Button("Continue",s=12),sg.Text("",s=2),sg.Button("Cancel",s=12)]),
        [sg.Text("")],
        ]
    layoutGENERATEx = [[sg.Column(layoutGENERATE)]]
    
    if ThemeExists==1:
        WindowGENERATE = sg.Window("Are you sure?", layoutGENERATEx, grab_anywhere=True, keep_on_top=True,no_titlebar=True,background_color='Red',margins=(0,0))
        eventGEN, valuesGEN = WindowGENERATE.read()
        while True:
            if eventGEN=='Continue':
                event = '  - GENERATE -  '
                break
            if eventGEN=='Cancel':
                break
        WindowGENERATE.close()
    else:
        event = '  - GENERATE -  '
        
def find_last_two_files_created(VitaPATH):
    # Get all files in the directory and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(VitaPATH):
        for file in files:
            filepath = os.path.join(root, file)
            all_files.append(filepath)

    # Sort the files by creation time
    all_files.sort(key=lambda x: os.path.getctime(x))

    # Get the last two files created
    last_two_files = all_files[-2:]

    return last_two_files        
        
if 1==1:

    layoutT1 = [
        [sg.Text("Theme name :",s=12,justification='r')],
        [sg.Text("Version :",s=12,justification='r')],
        [sg.Text("Creator :",s=12,justification='r')],
        ]

    layoutT2 = [
        [sg.Text(ThemeName,k='Theme_Name'),sg.Text('WARNING : A THEME WITH THIS NAME ALREADY EXISTS.!',text_color='Red',k='Warn',visible=False)],
        [sg.Text(ThemeVers,k='Theme_Version')],
        [sg.Text(Creator,k='Theme_Creator',s=20),sg.Button('Change details',s=15),sg.Button('Export',s=7,visible=False,k='-Export-')],
        ]

    layoutT3 = [
        [sg.Text("")]
        ]

    layoutT4 = [
        [sg.Text("Lockscreen Clock Position :",s=25,justification='r'),sg.InputCombo(['Top Left', 'Bottom Left', 'Bottom Right'], size=(16, 0),key='-CLOPOS-',default_value=CLOPOS)],
        [sg.Text("Clock Color :",s=25,justification='r'),sg.Button("Change",s=15,k='CLOCKCOL')],
        [sg.Text("Titlebar Colors :",s=25,justification='r'),sg.Button("Change",s=15,k='TBTc')],
        ]

    layoutM1 = [
        [sg.Text("")],
        [sg.Text("Lockscreen :",s=12,justification='r'),sg.Input(key='LS',default_text=LS),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text("",s=1),sg.Button('Waves',s=8)],
        [sg.Text("Page 1 :",s=12,justification='r'),sg.Input(key='PG1',default_text=PG1),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG1w',default_value=PG1w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG1txtc,k='PG1tc'),sg.Text(" ")],
        [sg.Text("Page 2 :",s=12,justification='r'),sg.Input(key='PG2',default_text=PG2),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG2w',default_value=PG2w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG2txtc,k='PG2tc'),sg.Text(" ")],
        [sg.Text("Page 3 :",s=12,justification='r'),sg.Input(key='PG3',default_text=PG3),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG3w',default_value=PG3w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG3txtc,k='PG3tc'),sg.Text(" ")],
        [sg.Text("Page 4 :",s=12,justification='r'),sg.Input(key='PG4',default_text=PG4),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG4w',default_value=PG4w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG4txtc,k='PG4tc'),sg.Text(" ")],
        [sg.Text("Page 5 :",s=12,justification='r'),sg.Input(key='PG5',default_text=PG5),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG5w',default_value=PG5w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG5txtc,k='PG5tc'),sg.Text(" ")],
        [sg.Text("Page 6 :",s=12,justification='r'),sg.Input(key='PG6',default_text=PG6),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG6w',default_value=PG6w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG6txtc,k='PG6tc'),sg.Text(" ")],
        [sg.Text("Page 7 :",s=12,justification='r'),sg.Input(key='PG7',default_text=PG7),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG7w',default_value=PG7w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG7txtc,k='PG7tc'),sg.Text(" ")],
        [sg.Text("Page 8 :",s=12,justification='r'),sg.Input(key='PG8',default_text=PG8),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG8w',default_value=PG8w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG8txtc,k='PG8tc'),sg.Text(" ")],
        [sg.Text("Page 9 :",s=12,justification='r'),sg.Input(key='PG9',default_text=PG9),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG9w',default_value=PG9w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG9txtc,k='PG9tc'),sg.Text(" ")],
        [sg.Text("Page 10 :",s=12,justification='r'),sg.Input(key='PG10',default_text=PG10),sg.FileBrowse(file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Text(" Wave :"),sg.InputCombo([i for i in range(0, 31)], size=(3, 10),key='PG10w',default_value=PG10w),sg.Text("Text Color :"),sg.Button("  ",button_color=PG10txtc,k='PG10tc'),sg.Text(" ")],
        [sg.Text("")],
        [sg.Text("Icon Set :",s=12,justification='r'),sg.Input(k='ICOSET',default_text=ICOSET),sg.FolderBrowse(initial_folder='IconSet/')],
        [sg.Text("",s=12),sg.Button("Create NEW IconSet",s=18),sg.Button("Use DEFAULT IconSet",s=19)],
        
        [sg.Text("")],
        ]

    layoutM2 = [
        c([(sg.Graph((390,220), (0,0), (390,220), key='-Image_LS_Preview-'))]),
        [sg.HorizontalSeparator()],
        c([(sg.Graph((390,220), (0,0), (390,220), key='-Image_LA_Preview-'))]),
        [sg.Text("Preview :",s=8,justification='c'),sg.Button('1',button_color=('yellow','grey'),k='V1'),sg.Button('2',button_color=('yellow','grey'),k='V2'),sg.Button('3',button_color=('yellow','grey'),k='V3'),sg.Button('4',button_color=('yellow','grey'),k='V4'),sg.Button('5',button_color=('yellow','grey'),k='V5'),sg.Button('6',button_color=('yellow','grey'),k='V6'),sg.Button('7',button_color=('yellow','grey'),k='V7'),sg.Button('8',button_color=('yellow','grey'),k='V8'),sg.Button('9',button_color=('yellow','grey'),k='V9'),sg.Button('10',button_color=('yellow','grey'),k='V10')],
        [sg.Text("Notifications :",s=12),sg.Button("Show / Hide preview"),sg.Button("Change",k='EDIT_NOTE',s=8)]
        ]

    layout = [
        [sg.Column(layoutT1), sg.Column(layoutT2), sg.Column(layoutT3), sg.Stretch(),sg.Column(layoutT4)],
        [sg.HorizontalSeparator()],
        [sg.Column(layoutM1), sg.VerticalSeparator(), sg.Column(layoutM2)],# sg.VerticalSeparator()],
        [sg.HorizontalSeparator()],
        [sg.Text("")],
        [sg.Text("Music :",s=12,justification='r'),sg.Input(key='BGM',default_text=BGM),sg.FileBrowse(file_types=(('Audio', '*.wav *.mp3 *.at9'),('ALL','*.* *'))),sg.Button('Use DEFAULT music'),sg.Stretch(),sg.Button('  - GENERATE THEME -  ',button_color=('Yellow','Black')),sg.Text("   ")],
        [sg.Text("")],
        ]
        
    window = sg.Window('VITA THEME BUILDER - by anthj', layout, finalize=True)
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
    
    # RECORD CURRENT VALUES FOR CHANGES
    LS_old = (LS)
    CLOPOS_old = (CLOPOS)
    COLOR_BAR_old = (TBC)
    COLOR_TXT_old = (TBTC)
    ICOSET_old = (ICOSET)
    BGM_old = (BGM)
    PG1_old = (PG1)
    PG2_old = (PG2)
    PG3_old = (PG3)
    PG4_old = (PG4)
    PG5_old = (PG5)
    PG6_old = (PG6)
    PG7_old = (PG7)
    PG8_old = (PG8)
    PG9_old = (PG9)
    PG10_old = (PG10)
    PG1w_old = (PG1w)
    PG2w_old = (PG2w)
    PG3w_old = (PG3w)
    PG4w_old = (PG4w)
    PG5w_old = (PG5w)
    PG6w_old = (PG6w)
    PG7w_old = (PG7w)
    PG8w_old = (PG8w)
    PG9w_old = (PG9w)
    PG10w_old = (PG10w)
    
    while True:
        event, values = window.read(10)
        if exportable == 1: window['-Export-'].update(visible=True)

        # CLOSE APP OR ASK FOR THEME NAME
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        if ThemeName == '-CLOSE-APP-':
            window.close()
            break
        if ThemeName == ' ':
            window.hide()
            EDIT_THEME()
        else: window.UnHide()
        if ThemeName == '':
            window.hide()
            EDIT_THEME()
        else: window.UnHide()
        if Creator == '':
            window.hide()
            EDIT_THEME()
        else: window.UnHide()
            # THE MAIN WINDOW - LOCKSCREEN PREVIEW
            
        if SCREEN == ('UPDADED'):
            window['-Image_LS_Preview-'].erase()
            Image_LS_Preview='assets/preview/TEMP/Lockscreen.png'
            if not Path(Image_LS_Preview).is_file():
                Image_LS_Preview = "assets/preview/default/defaultLS.png"
            window['-Image_LS_Preview-'].draw_image(filename=Image_LS_Preview, location=(0,208))
            if values['-CLOPOS-'] == 'Bottom Left':
                window['-Image_LS_Preview-'].draw_text("January 1 (Monday)",font=('Helvetica', 11), color=CLOCOL, location=(95,69))     #0 Bottom Left
                window['-Image_LS_Preview-'].draw_text("12:00",font=('Helvetica', 41), color=CLOCOL, location=(99,39))                  #0 Bottom Left
            if values['-CLOPOS-'] == 'Top Left':
                window['-Image_LS_Preview-'].draw_text("January 1 (Monday)",font=('Helvetica', 11), color=CLOCOL, location=(95,183))    #1 Top Left
                window['-Image_LS_Preview-'].draw_text("12:00",font=('Helvetica', 41), color=CLOCOL, location=(99,150))                 #1 Top Left
            if values['-CLOPOS-'] == 'Bottom Right':
                window['-Image_LS_Preview-'].draw_text("January 1 (Monday)",font=('Helvetica', 11), color=CLOCOL, location=(300,69))    #2 Bottom Right
                window['-Image_LS_Preview-'].draw_text("12:00",font=('Helvetica', 41), color=CLOCOL, location=(292,39))                 #2 Bottom Right
            window['-Image_LS_Preview-'].draw_rectangle((0,208),(390,220),fill_color=TBC, line_color=TBC)
            window['-Image_LS_Preview-'].draw_image(filename=Image_LS_Overlay, location=(0,220))
            window['-Image_LS_Preview-'].draw_text("o))                                                           []                                               12:00",font=('Helvetica', 7), color=TBTC, location=(184,212))
            
            # THE MAIN WINDOW - LIVEAREA PREVIEW
            
            window['-Image_LA_Preview-'].erase()
            if LA_View == 1:
                Image_LA_Preview='assets/preview/TEMP/Page1.png'
                Preview_TXTColor=PG1txtc
            if LA_View == 2:
                Image_LA_Preview='assets/preview/TEMP/Page2.png'
                Preview_TXTColor=PG2txtc
            if LA_View == 3:
                Image_LA_Preview='assets/preview/TEMP/Page3.png'
                Preview_TXTColor=PG3txtc
            if LA_View == 4:
                Image_LA_Preview='assets/preview/TEMP/Page4.png'
                Preview_TXTColor=PG4txtc
            if LA_View == 5:
                Image_LA_Preview='assets/preview/TEMP/Page5.png'
                Preview_TXTColor=PG5txtc
            if LA_View == 6:
                Image_LA_Preview='assets/preview/TEMP/Page6.png'
                Preview_TXTColor=PG6txtc
            if LA_View == 7:
                Image_LA_Preview='assets/preview/TEMP/Page7.png'
                Preview_TXTColor=PG7txtc
            if LA_View == 8:
                Image_LA_Preview='assets/preview/TEMP/Page8.png'
                Preview_TXTColor=PG8txtc
            if LA_View == 9:
                Image_LA_Preview='assets/preview/TEMP/Page9.png'
                Preview_TXTColor=PG9txtc
            if LA_View == 10:
                Image_LA_Preview='assets/preview/TEMP/Page10.png'
                Preview_TXTColor=PG10txtc
                        
            if not Path(Image_LA_Preview).is_file():
                Image_LA_Preview = "assets/preview/default/defaultLA.png"
            window['-Image_LA_Preview-'].draw_image(filename=Image_LA_Preview, location=(0,220))
            window['-Image_LA_Preview-'].draw_rectangle((0,208),(390,220),fill_color=TBC, line_color=TBC)
            window['-Image_LA_Preview-'].draw_text("o))                                                            []                                            12:00    ",font=('Helvetica', 7), color=TBTC, location=(184,213))
            if Path(Image_NoteNOx).is_file():
                window['-Image_LA_Preview-'].draw_image(filename=Image_NoteNOx, location=(350,220))
            else:
                window['-Image_LA_Preview-'].draw_image(filename=Image_NoteNO, location=(350,220))
            window['-Image_LA_Preview-'].draw_image(filename=Image_Icon1, location=(60,160))
            window['-Image_LA_Preview-'].draw_image(filename=Image_Icon2, location=(135,160))
            window['-Image_LA_Preview-'].draw_image(filename=Image_Icon3, location=(210,160))
            window['-Image_LA_Preview-'].draw_image(filename=Image_Icon4, location=(285,160))
            window['-Image_LA_Preview-'].draw_text("Browser         Settings          Calendar          Photos",font=('Helvetica', 9),color=(Preview_TXTColor),location=(204,87))
            window['-Image_LA_Preview-'].draw_image(filename=Image_curs, location=(0,147))
            window['-Image_LA_Preview-'].draw_image(filename=Image_base, location=(0,127))
            window['-Image_LA_Preview-'].draw_image(filename=Image_base, location=(0,107))
            window['-Image_LA_Preview-'].draw_image(filename=Image_base, location=(0,87))
            if NOT_View == 1:
                if Path(Image_NoteNEWx).is_file():
                    window['-Image_LA_Preview-'].draw_image(filename=Image_NoteNEWx, location=(350,220))
                else:
                    window['-Image_LA_Preview-'].draw_image(filename=Image_NoteNEW, location=(350,220))
                window['-Image_LA_Preview-'].draw_text("2",font=('Helvetica', 14),color=('White'),location=(375,206))
                window['-Image_LS_Preview-'].draw_rectangle((25,156),(278,185),fill_color=NOT_BOX_BOX_COL,line_color=NOT_BOX_FRA_COL)
                window['-Image_LS_Preview-'].draw_text("[[]]   This is a sample notification",font=('Helvetica', 8),color=(NOT_TXTc),location=(110,171))
            SCREEN = 'DONE'

        # CHECKING FOR CHANGES AND BUTTON PRESSES
        
        if event == 'Change details':
            firstrun=0
            exportable=0
            window['-Export-'].update(visible=False)
            window.hide()
            EDIT_THEME()

        if event == 'Waves':
            os.system("assets\waves.png")
        
        if event == '  - GENERATE THEME -  ':
            graph = window['-Image_LS_Preview-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/preview/TEMP/preview_lockscreen.png')
            graph = window['-Image_LA_Preview-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/preview/TEMP/preview_page.png')
            GenerateTHEME()

        if event == '-Export-' or retry == 1:
            retry=0
            MoreTOOLS_CHECK()

        if event == '  - GENERATE -  ':
            GEN_continue=0
            window.hide()
            GenerateTHEME_image()
            if GEN_continue==1:
                PREV_TXT=9
                CurrentProcess=('Starting . . .')
                ThemeNameSize=(len(ThemeName))

                layoutPG = [
                    [sg.Text('')],
                    c([(sg.Graph((226,128), (0,0), (226,128), key='-PREVIEW-'))]),
                    [sg.Text('')],
                    [sg.HorizontalSeparator()],
                    c([sg.Text(CurrentProcess,k='CurrentProcess',s=40)]),
                    c([sg.ProgressBar(17,orientation='h', bar_color=('Yellow','Grey'),size=(30, 20),key='-progressbar-')]),
                    [sg.HorizontalSeparator()],
                    [sg.Text('')],
                    c([sg.Text("Your theme files have been created in the folder :",text_color='#001D3C',k='T1'),sg.Text(ThemePATH,text_color='#001D3C',k='T2')]),
                    c([sg.Text("you now need to copy this folder to your Vita into :",text_color='#001D3C',k='T3'),sg.Text("ux0:/CustomTheme/"+ThemeName,text_color='#001D3C',k='T4')]),
                    c([sg.Text('',k='T5')]),
                    [sg.Text('    To install your theme :',k='T6',text_color='#001D3C')],
                    [sg.Text("",s=8),sg.Text("- open the 'Custom Themes Manager' app'",text_color='#001D3C',k='T7')],
                    [sg.Text("",s=8),sg.Text("- select 'Install a Custom Theme from the local folder'",text_color='#001D3C',k='T8')],
                    [sg.Text("",s=8),sg.Text('- highlight your theme and press X, then press START to add your theme    ',k='T9',text_color='#001D3C')],
                    [sg.Text("",s=8),sg.Text('- select Apply an installed theme and select your theme',k='T10',text_color='#001D3C')],
                    c([sg.Text('')]),
                    c([sg.Button(' - OK - ',s=20,visible=False,k='AllDone')])
                    ]
                
                layoutPGx = [[sg.Column(layoutPG)]]
                
                windowPG = sg.Window("Progress Bar", layoutPGx,keep_on_top=True,no_titlebar=True,grab_anywhere=True,background_color='#015BBB',margins=(0,0),modal=False)
                eventPG, valuesPG = windowPG.read(10)
                if Path('assets/preview/TEMP/preview_thumbnail.png').is_file():
                    windowPG['-PREVIEW-'].draw_image(filename='assets/preview/TEMP/preview_thumbnail.png',location=(0,128))
                cmdline1 = ('call assets\scale.bat -source "assets/preview/TEMP/preview_lockscreen.png" -target "{}preview_lockscreen.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(ThemePATH,ThemePATH)
                cmdline2 = ('call assets\scale.bat -source "assets/preview/TEMP/preview_page.png" -target "{}preview_page.png" -max-height 272 -max-width 480 -keep-ratio no -force yes').format(ThemePATH,ThemePATH)
                os.system(cmdline1)
                os.system(cmdline2)
                
                windowPG['-progressbar-'].update(current_count=0)
                
                if "STAGE1"=="STAGE1":      # Create folders and generate XML file
                    windowPG['CurrentProcess'].update('Starting . .')
                    THEME_XML=(ThemePATH+'theme.xml')
                    THEME_INI=(ThemePATH+'theme.ini')

                    MusicType = values['BGM']
                    MusicName = MusicType[:-3]
                    MusicType = MusicType.replace(MusicName, "")
                    MusicType = MusicType.lower()
                    
                    windowPG['-progressbar-'].update(current_count=1)
                    windowPG['CurrentProcess'].update('Generating theme.xml . .')
                    XML_CLOCOL=CLOCOL.replace('#','')
                    if CLOPOS=='Bottom Left':
                        XML_CLOPOS=CLOPOS.replace('Bottom Left','0')
                    if CLOPOS=='Top Left':
                        XML_CLOPOS=CLOPOS.replace('Top Left','1')
                    if CLOPOS=='Bottom Right':
                        XML_CLOPOS=CLOPOS.replace('Bottom Right','2')
                    XML_NOT_BOXc=NOT_BOXc.replace('#','')
                    XML_NOT_TXTc=NOT_TXTc.replace('#','')
                    XML_TBC=TBC.replace('#','')
                    XML_TBTC=TBTC.replace('#','')
                    XML_PG1txtc=PG1txtc.replace('#','')
                    XML_PG2txtc=PG2txtc.replace('#','')
                    XML_PG3txtc=PG3txtc.replace('#','')
                    XML_PG4txtc=PG4txtc.replace('#','')
                    XML_PG5txtc=PG5txtc.replace('#','')
                    XML_PG6txtc=PG6txtc.replace('#','')
                    XML_PG7txtc=PG7txtc.replace('#','')
                    XML_PG8txtc=PG8txtc.replace('#','')
                    XML_PG9txtc=PG9txtc.replace('#','')
                    XML_PG10txtc=PG10txtc.replace('#','')
                    with open(THEME_XML, "w") as f:
                        print('<?THIS THEME WAS GENERATED USING THE VITA THEME BUILDER by ANTHJ>',file=f)
                    with open(THEME_XML, "a") as f: 
                        print('<?xml version="1.0" encoding="UTF-8"?><theme format-ver="01.00" package="0">',file=f)

                        print('<InfomationProperty>',file=f)
                        print(' <m_contentVer>'+ThemeVers+'</m_contentVer>',file=f)
                        print(' <m_homePreviewFilePath>preview_page.png</m_homePreviewFilePath>',file=f)
                        print(' <m_packageImageFilePath>preview_thumbnail.png</m_packageImageFilePath>',file=f)
                        print(' <m_provider>',file=f)
                        print('     <m_default>'+Creator+'</m_default>',file=f)
                        print('     <m_param></m_param>',file=f)
                        print(' </m_provider>',file=f)
                        print(' <m_startPreviewFilePath>preview_lockscreen.png</m_startPreviewFilePath>',file=f)
                        print(' <m_title>',file=f)
                        print('     <m_default>'+ThemeName+'</m_default>',file=f)
                        print('     <m_param>',file=f)
                        print('         <m_da>'+ThemeName+'</m_da>',file=f)
                        print('         <m_de>'+ThemeName+'</m_de>',file=f)
                        print('         <m_es>'+ThemeName+'</m_es>',file=f)
                        print('         <m_fi>'+ThemeName+'</m_fi>',file=f)
                        print('         <m_fr>'+ThemeName+'</m_fr>',file=f)
                        print('         <m_it>'+ThemeName+'</m_it>',file=f)
                        print('         <m_nl>'+ThemeName+'</m_nl>',file=f)
                        print('         <m_no>'+ThemeName+'</m_no>',file=f)
                        print('         <m_pl>'+ThemeName+'</m_pl>',file=f)
                        print('         <m_pt>'+ThemeName+'</m_pt>',file=f)
                        print('         <m_ru>'+ThemeName+'</m_ru>',file=f)
                        print('         <m_sv>'+ThemeName+'</m_sv>',file=f)
                        print('     </m_param>',file=f)
                        print(' </m_title>',file=f)
                        print('</InfomationProperty>',file=f)
                        
                        print('<StartScreenProperty>',file=f)
                        print(' <m_dateColor>ff'+XML_CLOCOL+'</m_dateColor>',file=f)
                        print(' <m_dateLayout>'+XML_CLOPOS+'</m_dateLayout>',file=f)
                        print(' <m_filePath>lockscreen.png</m_filePath>',file=f)
                        print(' <m_notifyBgColor>ff'+XML_NOT_BOXc+'</m_notifyBgColor>',file=f)
                        print(' <m_notifyBorderColor>ffcccccc</m_notifyBorderColor>',file=f)
                        print(' <m_notifyFontColor>ff'+XML_NOT_TXTc+'</m_notifyFontColor>',file=f)
                        print('</StartScreenProperty>',file=f)
                        
                        print('<InfomationBarProperty>',file=f)
                        print(' <m_barColor>ff'+XML_TBC+'</m_barColor>',file=f)
                        print(' <m_indicatorColor>ff'+XML_TBTC+'</m_indicatorColor> ',file=f)
                        print(' <m_noticeFontColor>ffffffff</m_noticeFontColor>',file=f)
                        print(' <m_noticeGlowColor>ffca0000</m_noticeGlowColor>',file=f)
                        print(' <m_noNoticeFilePath>notices.png</m_noNoticeFilePath>',file=f)
                        print(' <m_newNoticeFilePath>notice.png</m_newNoticeFilePath>',file=f)
                        print('</InfomationBarProperty>',file=f)

                        print('<HomeProperty>',file=f)
                        print(' <m_bgParam>',file=f)
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg1t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg1.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG1w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG1txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg2t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg2.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG2w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG2txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg3t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg3.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG3w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG3txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg4t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg4.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG4w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG4txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg5t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg5.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG5w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG5txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg6t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg6.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG6w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG6txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg7t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg7.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG7w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG7txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg8t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg8.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG8w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG8txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg9t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg9.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG9w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG9txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        
                        print('     <BackgroundParam>',file=f)
                        print('         <m_thumbnailFilePath>bg10t.png</m_thumbnailFilePath>',file=f)
                        print('         <m_imageFilePath>bg10.png</m_imageFilePath>',file=f)
                        print('         <m_waveType>'+str(PG10w)+'</m_waveType>',file=f)
                        print('         <m_fontColor>ff'+XML_PG10txtc+'</m_fontColor>',file=f)
                        print('         <m_fontShadow>1</m_fontShadow>',file=f)
                        print('     </BackgroundParam>',file=f)
                        print(' </m_bgParam>',file=f)
                        
                        print(' <m_basePageFilePath>basePage.png</m_basePageFilePath>',file=f)
                        print(' <m_curPageFilePath>curPage.png</m_curPageFilePath>',file=f)
                        print(' <m_bgmFilePath>bgm.at9</m_bgmFilePath>',file=f)
                        print(' <m_browser>',file=f)
                        print('     <m_iconFilePath>icon_web.png</m_iconFilePath>',file=f)
                        print(' </m_browser>',file=f)
                        print('`<m_calendar>',file=f)
                        print('     <m_iconFilePath>icon_calendar.png</m_iconFilePath>',file=f)
                        print(' </m_calendar>',file=f)
                        print(' <m_camera>',file=f)
                        print('     <m_iconFilePath>icon_photos.png</m_iconFilePath>',file=f)
                        print(' </m_camera>',file=f)
                        print(' <m_email>',file=f)
                        print('     <m_iconFilePath>icon_mail.png</m_iconFilePath>',file=f)
                        print(' </m_email>',file=f)
                        print(' <m_friend>',file=f)
                        print('     <m_iconFilePath>icon_friends.png</m_iconFilePath>',file=f)
                        print(' </m_friend>',file=f)
                        print(' <m_hostCollabo>',file=f)
                        print('     <m_iconFilePath>icon_cma.png</m_iconFilePath>',file=f)
                        print(' </m_hostCollabo>',file=f)
                        print(' <m_message>',file=f)
                        print('     <m_iconFilePath>icon_messages.png</m_iconFilePath>',file=f)
                        print(' </m_message>',file=f)
                        print(' <m_music>',file=f)
                        print('     <m_iconFilePath>icon_music.png</m_iconFilePath>',file=f)
                        print(' </m_music>',file=f)
                        print(' <m_near>',file=f)
                        print('     <m_iconFilePath>icon_near.png</m_iconFilePath>',file=f)
                        print(' </m_near>',file=f)
                        print(' <m_parental>',file=f)
                        print('     <m_iconFilePath>icon_parental.png</m_iconFilePath>',file=f)
                        print(' </m_parental>',file=f)
                        print(' <m_party>',file=f)
                        print('     <m_iconFilePath>icon_party.png</m_iconFilePath>',file=f)
                        print(' </m_party>',file=f)
                        print(' <m_ps3Link>',file=f)
                        print('     <m_iconFilePath>icon_ps3link.png</m_iconFilePath>',file=f)
                        print(' </m_ps3Link>',file=f)
                        print(' <m_ps4Link>',file=f)
                        print('     <m_iconFilePath>icon_ps4link.png</m_iconFilePath>',file=f)
                        print(' </m_ps4Link>',file=f)
                        print(' <m_power>',file=f)
                        print('     <m_iconFilePath>icon_power.png</m_iconFilePath>',file=f)
                        print(' </m_power>',file=f)
                        print(' <m_settings>',file=f)
                        print('     <m_iconFilePath>icon_settings.png</m_iconFilePath>',file=f)
                        print(' </m_settings>',file=f)
                        print(' <m_trophy>',file=f)
                        print('     <m_iconFilePath>icon_trophies.png</m_iconFilePath>',file=f)
                        print(' </m_trophy>',file=f)
                        print(' <m_video>',file=f)
                        print('     <m_iconFilePath>icon_videos.png</m_iconFilePath>',file=f)
                        print(' </m_video>',file=f)
                        print('</HomeProperty>',file=f)
                        print('</theme>',file=f)

                        windowPG['-progressbar-'].update(current_count=2)
                
                if "STAGE2"=="STAGE2":      # Convert Lockscreen and pages
                    
                    windowPG['CurrentProcess'].update('Converting image lockscreen . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}lockscreen.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(LS_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}lockscreen.png" -o "{}lockscreen.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    windowPG['-progressbar-'].update(current_count=3)
                    
                    windowPG['CurrentProcess'].update('Converting image 1 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg1.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG1_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg1.png" -o "{}bg1.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg1t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG1_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg1t.png" -o "{}bg1t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=4)
                    
                    windowPG['CurrentProcess'].update('Converting image 2 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg2.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG2_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg2.png" -o "{}bg2.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg2t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG2_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg2t.png" -o "{}bg2t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=5)
                    
                    windowPG['CurrentProcess'].update('Converting image 3 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg3.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG3_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg3.png" -o "{}bg3.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg3t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG3_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg3t.png" -o "{}bg3t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=6)
                    
                    windowPG['CurrentProcess'].update('Converting image 4 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg4.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG4_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg4.png" -o "{}bg4.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg4t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG4_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg4t.png" -o "{}bg4t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=7)
                    
                    windowPG['CurrentProcess'].update('Converting image 5 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg5.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG5_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg5.png" -o "{}bg5.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg5t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG5_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg5t.png" -o "{}bg5t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=8)
                    
                    windowPG['CurrentProcess'].update('Converting image 6 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg6.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG6_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg6.png" -o "{}bg6.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg6t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG6_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg6t.png" -o "{}bg6t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=9)
                    
                    windowPG['CurrentProcess'].update('Converting image 7 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg7.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG7_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg7.png" -o "{}bg7.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg7t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG7_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg7t.png" -o "{}bg7t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=10)
                    
                    windowPG['CurrentProcess'].update('Converting image 8 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg8.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG8_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg8.png" -o "{}bg8.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg8t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG8_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg8t.png" -o "{}bg8t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=11)
                    
                    windowPG['CurrentProcess'].update('Converting image 9 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg9.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG9_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg9.png" -o "{}bg9.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg9t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG9_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg9t.png" -o "{}bg9t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=12)
                    
                    windowPG['CurrentProcess'].update('Converting image 10 . .')
                    cmdline1 = ('call assets\scale.bat -source "{}" -target "{}bg10.png" -max-height 512 -max-width 960 -keep-ratio no -force yes').format(PG10_old,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}bg10.png" -o "{}bg10.png"').format(ThemePATH,ThemePATH)
                    cmdline3 = ('call assets\scale.bat -source "{}" -target "{}bg10t.png" -max-height 192 -max-width 360 -keep-ratio no -force yes').format(PG10_old,ThemePATH)
                    cmdline4 = ('assets\pngquant.exe -f "{}bg10t.png" -o "{}bg10t.png"').format(ThemePATH,ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=13)
                    windowPG['CurrentProcess'].update('Converting image notifications. .')
                    if NOTI_inew == "assets\preview\TEMP\ICONnew.png":
                        NOTI_inew = "assets\preview\TEMP\LAnotenew_def.png"
                    if NOTI_inon == "assets\preview\TEMP\ICONno.png":
                        NOTI_inon = "assets\preview\TEMP\LAnoteno_def.png"
                    cmdline1 = ('assets\pngquant.exe -f "{}" -o "{}notices.png"').format(NOTI_inon,ThemePATH)
                    cmdline2 = ('assets\pngquant.exe -f "{}" -o "{}notice.png"').format(NOTI_inew,ThemePATH)
                    cmdline3 = ('copy "assets\preview\default\\base.png" "{}basePage.png"').format(ThemePATH)
                    cmdline4 = ('copy "assets\preview\default\curs.png" "{}curPage.png"').format(ThemePATH)
                    os.system(cmdline1)
                    os.system(cmdline2)
                    os.system(cmdline3)
                    os.system(cmdline4)
                    windowPG['-progressbar-'].update(current_count=14)
                    
                    windowPG['CurrentProcess'].update('Copying Iconset . .')
                    if ICOSET_old=='Default':
                        ICONS_USED='assets\IconBuilder\Overlays\Default'
                    else:
                        ICONS_USED=ICOSET_old
                    cmdline1 = ('copy "{}\icon_*.png" "{}"').format(ICONS_USED,ThemePATH)
                    os.system(cmdline1)
                    windowPG['CurrentProcess'].update('Processing BGM . .')
                    windowPG['-progressbar-'].update(current_count=15)
                    
                if "STAGE3"=="STAGE3":      # Process BG Music
                    
                    if MusicType=="at9":
                        BGM=BGM.replace('/','\\')
                        cmdline1 = ('copy /y "{}" "{}bgm.at9"').format(BGM,ThemePATH)
                        os.system(cmdline1)
                        windowPG['-progressbar-'].update(current_count=16)
                        
                    if MusicType=="wav":
                        BGM=BGM.replace('/','\\')
                        cmdline1 = ('assets\\at9tool.exe -e -br 144 -wholeloop "{}" "{}bgm.at9"').format(BGM,ThemePATH)
                        os.system(cmdline1)
                        windowPG['-progressbar-'].update(current_count=16)
                        
                    if MusicType=="mp3":
                        BGM=BGM.replace('/','\\')
                        cmdline1 = ('copy /y "{}" "assets/preview/TEMP/bgm.mp3"').format(BGM,ThemePATH)
                        os.system(cmdline1)
                        cmdline1 = ('assets\\ffmpeg.exe -i "assets/preview/TEMP/bgm.mp3" assets/preview/TEMP/bgm.wav -y')
                        cmdline2 = ('assets\\at9tool.exe -e -br 144 -wholeloop "assets/preview/TEMP/bgm.wav" "{}bgm.at9"').format(ThemePATH)
                        os.system(cmdline1)
                        windowPG['-progressbar-'].update(current_count=16)
                        os.system(cmdline2)

                    if MusicType=="ult":
                        cmdline1 = ('copy /y "{}" "{}bgm.at9"').format(ORIG_BGM,ThemePATH)
                        print(ORIG_BGM)
                        os.system(cmdline1)

                ThemeBUILD = sg.UserSettings(path=SETTINGS_PATH, filename=THEME_INI, use_config_file=True)

                ThemeBUILD["THEME"]["Name"] = ThemeName
                ThemeBUILD["THEME"]["Version"] = ThemeVers
                ThemeBUILD["THEME"]["Creator"] = Creator
                ThemeBUILD["CLOCK"]["Color"] = XML_CLOCOL
                ThemeBUILD["CLOCK"]["Position"] = XML_CLOPOS
                ThemeBUILD["NOTIFICATION"]["Box Color"] = XML_NOT_BOXc
                ThemeBUILD["NOTIFICATION"]["Text Color"] = XML_NOT_TXTc
                ThemeBUILD["INFOBAR"]["Bar Color"] = XML_TBC
                ThemeBUILD["INFOBAR"]["Text Color"] = XML_TBTC
                ThemeBUILD["WAVE PATTERNS"]["Page 1"] = PG1w
                ThemeBUILD["WAVE PATTERNS"]["Page 2"] = PG2w
                ThemeBUILD["WAVE PATTERNS"]["Page 3"] = PG3w
                ThemeBUILD["WAVE PATTERNS"]["Page 4"] = PG4w
                ThemeBUILD["WAVE PATTERNS"]["Page 5"] = PG5w
                ThemeBUILD["WAVE PATTERNS"]["Page 6"] = PG6w
                ThemeBUILD["WAVE PATTERNS"]["Page 7"] = PG7w
                ThemeBUILD["WAVE PATTERNS"]["Page 8"] = PG8w
                ThemeBUILD["WAVE PATTERNS"]["Page 9"] = PG9w
                ThemeBUILD["WAVE PATTERNS"]["Page 10"] = PG10w
                ThemeBUILD["PAGE TEXT COLORS"]["Page 1"] = XML_PG1txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 2"] = XML_PG2txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 3"] = XML_PG3txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 4"] = XML_PG4txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 5"] = XML_PG5txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 6"] = XML_PG6txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 7"] = XML_PG7txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 8"] = XML_PG8txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 9"] = XML_PG9txtc
                ThemeBUILD["PAGE TEXT COLORS"]["Page 10"] = XML_PG10txtc
                
                windowPG['-progressbar-'].update(current_count=17)
                windowPG['CurrentProcess'].update('Process complete!')
                windowPG['AllDone'].update(visible=True)
                windowPG['T1'].update(text_color='white')
                windowPG['T2'].update(text_color='yellow')
                windowPG['T3'].update(text_color='white')
                windowPG['T4'].update(text_color='yellow')
                windowPG['T5'].update(text_color='white')
                windowPG['T6'].update(text_color='white')
                windowPG['T7'].update(text_color='white')
                windowPG['T8'].update(text_color='white')
                windowPG['T9'].update(text_color='white')
                windowPG['T10'].update(text_color='white')
                windowPG['-progressbar-'].update(bar_color=('Green','Green'))
                
                while True:
                    eventPG, valuesPG = windowPG.read(10)
                    if eventPG == 'AllDone':
                        break
                        windowPG.close()
                ThemeExists=1
                exportable=1
                windowPG.close()
                window.UnHide()
                
        if event == 'CLOCKCOL':
            CLOCK_COLOR()

        if event == 'Use DEFAULT music':
            BGM = 'Default'
            window['BGM'].update(BGM)
            SCREEN = ('UPDADED')

        if event == 'Use DEFAULT IconSet':
            ICOSET = 'Default'
            window['ICOSET'].update(ICOSET)
            SCREEN = ('UPDADED')

        if event == 'Create NEW IconSet':
            with open("assets/tntmp", "w") as f:
                f.write(ThemeName)
            process = subprocess.Popen('IconBUILDER.exe')

        if not values['ICOSET'] == ICOSET_old:
            if values['ICOSET'] == 'Default':
                convI_0 = ('del assets\preview\TEMP\icon_*.png')
                os.system(convI_0)
                
            Preview_I1 = values['ICOSET']+("/icon_web.png")
            Preview_I2 = values['ICOSET']+("/icon_settings.png")
            Preview_I3 = values['ICOSET']+("/icon_calendar.png")
            Preview_I4 = values['ICOSET']+("/icon_photos.png")
            
            if Path(Preview_I1).is_file():
                convI_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\icon_web.png" -max-height 64 -max-width 64 -keep-ratio no -force yes').format(Preview_I1)
                convI_1b = ('assets\convert "assets\preview\TEMP\icon_web.png" "assets\mask_ico.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\icon_web.png')
                convI_1c = ('assets\pngquant.exe -f "assets\preview\TEMP\icon_web.png" -o "assets\preview\TEMP\icon_web.png"')
                os.system(convI_1a)
                os.system(convI_1b)
                os.system(convI_1c)
                
                Image_Icon1 = "assets\preview\TEMP\icon_web.png"
            else:
                Image_Icon1 = "assets/preview/default/icon_web.png"
                
            if Path(Preview_I2).is_file():
                convI_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\icon_settings.png" -max-height 64 -max-width 64 -keep-ratio no -force yes').format(Preview_I2)
                convI_1b = ('assets\convert "assets\preview\TEMP\icon_settings.png" "assets\mask_ico.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\icon_settings.png')
                convI_1c = ('assets\pngquant.exe -f "assets\preview\TEMP\icon_settings.png" -o "assets\preview\TEMP\icon_settings.png"')
                os.system(convI_1a)
                os.system(convI_1b)
                os.system(convI_1c)

                Image_Icon2 = "assets\preview\TEMP\icon_settings.png"
            else:
                Image_Icon2 = "assets/preview/default/icon_settings.png"
                
            if Path(Preview_I3).is_file():
                convI_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\icon_calendar.png" -max-height 64 -max-width 64 -keep-ratio no -force yes').format(Preview_I3)
                convI_1b = ('assets\convert "assets\preview\TEMP\icon_calendar.png" "assets\mask_ico.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\icon_calendar.png')
                convI_1c = ('assets\pngquant.exe -f "assets\preview\TEMP\icon_calendar.png" -o "assets\preview\TEMP\icon_calendar.png"')
                os.system(convI_1a)
                os.system(convI_1b)
                os.system(convI_1c)

                Image_Icon3 = "assets\preview\TEMP\icon_calendar.png"
            else:
                Image_Icon3 = "assets/preview/default/icon_calendar.png"
                
            if Path(Preview_I4).is_file():
                convI_1a = ('call assets\scale.bat -source "{}" -target "assets\preview\TEMP\icon_photos.png" -max-height 64 -max-width 64 -keep-ratio no -force yes').format(Preview_I4)
                convI_1b = ('assets\convert "assets\preview\TEMP\icon_photos.png" "assets\mask_ico.png" -alpha off -compose CopyOpacity -composite assets\preview\TEMP\icon_photos.png')
                convI_1c = ('assets\pngquant.exe -f "assets\preview\TEMP\icon_photos.png" -o "assets\preview\TEMP\icon_photos.png"')
                os.system(convI_1a)
                os.system(convI_1b)
                os.system(convI_1c)

                Image_Icon4 = "assets\preview\TEMP\icon_photos.png"
            else:
                Image_Icon4 = "assets/preview/default/icon_photos.png"

            ICOSET_old = values['ICOSET']
            SCREEN = ('UPDADED')

        if event == 'Show / Hide preview':
            if NOT_View == 0:
                NOT_View = 1
            else:
                NOT_View = 0
            SCREEN = ('UPDADED')

        if event == 'EDIT_NOTE':
            NOTIFICATION_EDIT()
            SCREEN = ('UPDADED')

        if event == 'TBTc':
            BAR_COLOR()
            
        if event == 'PG1tc':
            PAGE_TEXT = 1
            PAGE_TEXT_COLOR()            
        if event == 'PG2tc':
            PAGE_TEXT = 2
            PAGE_TEXT_COLOR()          
        if event == 'PG3tc':
            PAGE_TEXT = 3
            PAGE_TEXT_COLOR()        
        if event == 'PG4tc':
            PAGE_TEXT = 4
            PAGE_TEXT_COLOR()        
        if event == 'PG5tc':
            PAGE_TEXT = 5
            PAGE_TEXT_COLOR()        
        if event == 'PG6tc':
            PAGE_TEXT = 6
            PAGE_TEXT_COLOR()        
        if event == 'PG7tc':
            PAGE_TEXT = 7
            PAGE_TEXT_COLOR()        
        if event == 'PG8tc':
            PAGE_TEXT = 8
            PAGE_TEXT_COLOR()        
        if event == 'PG9tc':
            PAGE_TEXT = 9
            PAGE_TEXT_COLOR()        
        if event == 'PG10tc':
            PAGE_TEXT = 10
            PAGE_TEXT_COLOR()
              
        if not TBC == COLOR_BAR_old:
            COLOR_BAR_old = TBC
            SCREEN = ('UPDADED')
        if not TBTC == COLOR_TXT_old:
            COLOR_TXT_old = TBTC
            SCREEN = ('UPDADED')
        
        if not values['-CLOPOS-'] == CLOPOS_old:
            CLOPOS_old = values['-CLOPOS-']
            CLOPOS = values['-CLOPOS-']
            SCREEN = ('UPDADED')
        
        if not values['LS'] == LS_old:
            NEW_image = values['LS']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Lockscreen.png" -max-height 208 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Lockscreen.png" -o "assets/preview/TEMP/Lockscreen.png"')
            os.system(cmdA)
            os.system(cmdB)
            LS_old = values['LS']
            SCREEN = ('UPDADED')
        if not values['PG1'] == PG1_old:
            NEW_image = values['PG1']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page1.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page1.png" -o "assets/preview/TEMP/Page1.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG1_old = values['PG1']
            LA_View = 1
            window['V1'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG2'] == PG2_old:
            NEW_image = values['PG2']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page2.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page2.png" -o "assets/preview/TEMP/Page2.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG2_old = values['PG2']
            LA_View = 2
            window['V2'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG3'] == PG3_old:
            NEW_image = values['PG3']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page3.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page3.png" -o "assets/preview/TEMP/Page3.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG3_old = values['PG3']
            LA_View = 3
            window['V3'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG4'] == PG4_old:
            NEW_image = values['PG4']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page4.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page4.png" -o "assets/preview/TEMP/Page4.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG4_old = values['PG4']
            LA_View = 4
            window['V4'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG5'] == PG5_old:
            NEW_image = values['PG5']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page5.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page5.png" -o "assets/preview/TEMP/Page5.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG5_old = values['PG5']
            LA_View = 5
            window['V5'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG6'] == PG6_old:
            NEW_image = values['PG6']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page6.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page6.png" -o "assets/preview/TEMP/Page6.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG6_old = values['PG6']
            LA_View = 6
            window['V6'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG7'] == PG7_old:
            NEW_image = values['PG7']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page7.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page7.png" -o "assets/preview/TEMP/Page7.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG7_old = values['PG7']
            LA_View = 7
            window['V7'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG8'] == PG8_old:
            NEW_image = values['PG8']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page8.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page8.png" -o "assets/preview/TEMP/Page8.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG8_old = values['PG8']
            LA_View = 8
            window['V8'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG9'] == PG9_old:
            NEW_image = values['PG9']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page9.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page9.png" -o "assets/preview/TEMP/Page9.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG9_old = values['PG9']
            LA_View = 9
            window['V9'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')
        if not values['PG10'] == PG10_old:
            NEW_image = values['PG10']
            cmdA = ('call assets\scale.bat -source "{}" -target "assets/preview/TEMP/Page10.png" -max-height 220 -max-width 390 -keep-ratio no -force yes').format(NEW_image)
            cmdB = ('assets\pngquant.exe -f "assets/preview/TEMP/Page10.png" -o "assets/preview/TEMP/Page10.png"')
            os.system(cmdA)
            os.system(cmdB)
            PG10_old = values['PG10']
            LA_View = 10
            window['V10'].update(button_color=('yellow','#015BBB'))
            SCREEN = ('UPDADED')

        if not values['PG1w'] == PG1w_old:
            PG1w_old = values['PG1w']
            PG1w = values['PG1w']
        if not values['PG2w'] == PG2w_old:
            PG2w_old = values['PG2w']
            PG2w = values['PG2w']
        if not values['PG3w'] == PG3w_old:
            PG3w_old = values['PG3w']
            PG3w = values['PG3w']
        if not values['PG4w'] == PG4w_old:
            PG4w_old = values['PG4w']
            PG4w = values['PG4w']
        if not values['PG5w'] == PG5w_old:
            PG5w_old = values['PG5w']
            PG5w = values['PG5w']
        if not values['PG6w'] == PG6w_old:
            PG6w_old = values['PG6w']
            PG6w = values['PG6w']
        if not values['PG7w'] == PG7w_old:
            PG7w_old = values['PG7w']
            PG7w = values['PG7w']
        if not values['PG8w'] == PG8w_old:
            PG8w_old = values['PG8w']
            PG8w = values['PG8w']
        if not values['PG9w'] == PG9w_old:
            PG9w_old = values['PG9w']
            PG9w = values['PG9w']
        if not values['PG10w'] == PG10w_old:
            PG10w_old = values['PG10w']
            PG10w = values['PG10w']
            
        if not values['BGM'] == BGM_old:
            BGM_old = values['BGM']
            BGM = values['BGM']
        
        if event == 'V1':
            LA_View = 1
            SCREEN = ('UPDADED')
        if event == 'V2':
            LA_View = 2
            SCREEN = ('UPDADED')
        if event == 'V3':
            LA_View = 3
            SCREEN = ('UPDADED')
        if event == 'V4':
            LA_View = 4
            SCREEN = ('UPDADED')
        if event == 'V5':
            LA_View = 5
            SCREEN = ('UPDADED')
        if event == 'V6':
            LA_View = 6
            SCREEN = ('UPDADED')
        if event == 'V7':
            LA_View = 7
            SCREEN = ('UPDADED')
        if event == 'V8':
            LA_View = 8
            SCREEN = ('UPDADED')
        if event == 'V9':
            LA_View = 9
            SCREEN = ('UPDADED')
        if event == 'V10':
            LA_View = 10
            SCREEN = ('UPDADED')