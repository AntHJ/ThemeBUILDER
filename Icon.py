############################################
## VITA ICON GENERATOR - CREATED BY ANTHJ ##
############################################

from pathlib import Path
import PySimpleGUI as sg
from PIL import Image, ImageGrab
import os
import ctypes

sg.theme('PythonPlus')
ThemeName=""
default_button = sg.theme_button_color()
ctypes.windll.shcore.SetProcessDpiAwareness(True)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

# LOAD PREVIOUS SETTINGS AND DELETE PREVIOUS FILES
SETTINGS_PATH = Path.cwd()
settings = sg.UserSettings(
path=SETTINGS_PATH, filename="assets\default.ini", use_config_file=True)
filecheck = settings["ICON_GENERATOR"]["filecheck"]
TEMPfolder = 'assets\IconBuilder\TEMP'
for filename in os.listdir(TEMPfolder):
    file_path = os.path.join(TEMPfolder, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

if os.path.isfile("assets/tntmp"):
    with open("assets/tntmp", "r") as f:
        ThemeName = f.read()
    os.remove("assets/tntmp")
        
SnapCount=0
CloneAll=0

if filecheck == 'OK':
    icon1col = settings["ICON_GENERATOR"]["Icon1Color"]
    icon2col = settings["ICON_GENERATOR"]["Icon2Color"]
    icon3col = settings["ICON_GENERATOR"]["Icon3Color"]
    icon4col = settings["ICON_GENERATOR"]["Icon4Color"]
    icon5col = settings["ICON_GENERATOR"]["Icon5Color"]
    icon6col = settings["ICON_GENERATOR"]["Icon6Color"]
    icon7col = settings["ICON_GENERATOR"]["Icon7Color"]
    icon8col = settings["ICON_GENERATOR"]["Icon8Color"]
    icon9col = settings["ICON_GENERATOR"]["Icon9Color"]
    icon10col = settings["ICON_GENERATOR"]["Icon10Color"]
    icon11col = settings["ICON_GENERATOR"]["Icon11Color"]
    icon12col = settings["ICON_GENERATOR"]["Icon12Color"]
    icon13col = settings["ICON_GENERATOR"]["Icon13Color"]
    icon14col = settings["ICON_GENERATOR"]["Icon14Color"]
    icon15col = settings["ICON_GENERATOR"]["Icon15Color"]
    icon16col = settings["ICON_GENERATOR"]["Icon16Color"]
    icon17col = settings["ICON_GENERATOR"]["Icon17Color"]
    icon1bgc = settings["ICON_GENERATOR"]["Icon1Background"]
    icon2bgc = settings["ICON_GENERATOR"]["Icon2Background"]
    icon3bgc = settings["ICON_GENERATOR"]["Icon3Background"]
    icon4bgc = settings["ICON_GENERATOR"]["Icon4Background"]
    icon5bgc = settings["ICON_GENERATOR"]["Icon5Background"]
    icon6bgc = settings["ICON_GENERATOR"]["Icon6Background"]
    icon7bgc = settings["ICON_GENERATOR"]["Icon7Background"]
    icon8bgc = settings["ICON_GENERATOR"]["Icon8Background"]
    icon9bgc = settings["ICON_GENERATOR"]["Icon9Background"]
    icon10bgc = settings["ICON_GENERATOR"]["Icon10Background"]
    icon11bgc = settings["ICON_GENERATOR"]["Icon11Background"]
    icon12bgc = settings["ICON_GENERATOR"]["Icon12Background"]
    icon13bgc = settings["ICON_GENERATOR"]["Icon13Background"]
    icon14bgc = settings["ICON_GENERATOR"]["Icon14Background"]
    icon15bgc = settings["ICON_GENERATOR"]["Icon15Background"]
    icon16bgc = settings["ICON_GENERATOR"]["Icon16Background"]
    icon17bgc = settings["ICON_GENERATOR"]["Icon17Background"]
    custom1 = settings["ICON_GENERATOR"]["Icon1CustomBackground"]
    custom2 = settings["ICON_GENERATOR"]["Icon2CustomBackground"]
    custom3 = settings["ICON_GENERATOR"]["Icon3CustomBackground"]
    custom4 = settings["ICON_GENERATOR"]["Icon4CustomBackground"]
    custom5 = settings["ICON_GENERATOR"]["Icon5CustomBackground"]
    custom6 = settings["ICON_GENERATOR"]["Icon6CustomBackground"]
    custom7 = settings["ICON_GENERATOR"]["Icon7CustomBackground"]
    custom8 = settings["ICON_GENERATOR"]["Icon8CustomBackground"]
    custom9 = settings["ICON_GENERATOR"]["Icon9CustomBackground"]
    custom10 = settings["ICON_GENERATOR"]["Icon10CustomBackground"]
    custom11 = settings["ICON_GENERATOR"]["Icon11CustomBackground"]
    custom12 = settings["ICON_GENERATOR"]["Icon12CustomBackground"]
    custom13 = settings["ICON_GENERATOR"]["Icon13CustomBackground"]
    custom14 = settings["ICON_GENERATOR"]["Icon14CustomBackground"]
    custom15 = settings["ICON_GENERATOR"]["Icon15CustomBackground"]
    custom16 = settings["ICON_GENERATOR"]["Icon16CustomBackground"]
    custom17 = settings["ICON_GENERATOR"]["Icon17CustomBackground"]    
else:
    icon1col = 'White'
    icon2col = 'White'
    icon3col = 'White'
    icon4col = 'White'
    icon5col = 'White'
    icon6col = 'White'
    icon7col = 'White'
    icon8col = 'White'
    icon9col = 'White'
    icon10col = 'White'
    icon11col = 'White'
    icon12col = 'White'
    icon13col = 'White'
    icon14col = 'White'
    icon15col = 'White'
    icon16col = 'White'
    icon17col = 'White'
    icon1bgc = 'None.'
    icon2bgc = 'None.'
    icon3bgc = 'None.'
    icon4bgc = 'None.'
    icon5bgc = 'None.'
    icon6bgc = 'None.'
    icon7bgc = 'None.'
    icon8bgc = 'None.'
    icon9bgc = 'None.'
    icon10bgc = 'None.'
    icon11bgc = 'None.'
    icon12bgc = 'None.'
    icon13bgc = 'None.'
    icon14bgc = 'None.'
    icon15bgc = 'None.'
    icon16bgc = 'None.'
    icon17bgc = 'None.'
    custom1 = ''
    custom2 = ''
    custom3 = ''
    custom4 = ''
    custom5 = ''
    custom6 = ''
    custom7 = ''
    custom8 = ''
    custom9 = ''
    custom10 = ''
    custom11 = ''
    custom12 = ''
    custom13 = ''
    custom14 = ''
    custom15 = ''
    custom16 = ''
    custom17 = ''
        
def c(elems):
    return [sg.Stretch(), *elems, sg.Stretch()]

# SETUP LAYOUTS FOR ICONS

layoutR1c1 = [      # ROW 1 COLUMN 1
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon1-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon1col,key='-icon1C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon1bgc,key='-icon1B-')],
    c([sg.InputText(k='custom1',default_text=custom1,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap1')])
    ]    
layoutR1c2 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon2-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon2col,key='-icon2C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon2bgc,key='-icon2B-')],
    c([sg.InputText(k='custom2',default_text=custom2,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap2')])
    ]
layoutR1c3 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon3-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon3col,key='-icon3C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon3bgc,key='-icon3B-')],
    c([sg.InputText(k='custom3',default_text=custom3,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap3')])
    ]    
layoutR1c4 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon4-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon4col,key='-icon4C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon4bgc,key='-icon4B-')],
    c([sg.InputText(k='custom4',default_text=custom4,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap4')])
    ]
layoutR1c5 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon5-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon5col,key='-icon5C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon5bgc,key='-icon5B-')],
    c([sg.InputText(k='custom5',default_text=custom5,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap5')])
    ]
layoutR1c6 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon6-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon6col,key='-icon6C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon6bgc,key='-icon6B-')],
    c([sg.InputText(k='custom6',default_text=custom6,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap6')])
    ]
layoutR2c1 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon7-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon7col,key='-icon7C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon7bgc,key='-icon7B-')],
    c([sg.InputText(k='custom7',default_text=custom7,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap7')])
    ]
layoutR2c2 = [    
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon8-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon8col,key='-icon8C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon8bgc,key='-icon8B-')],
    c([sg.InputText(k='custom8',default_text=custom8,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap8')])
    ]
layoutR2c3 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon9-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon9col,key='-icon9C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon9bgc,key='-icon9B-')],
    c([sg.InputText(k='custom9',default_text=custom9,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap9')])
    ]
layoutR2c4 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon10-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon10col,key='-icon10C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon10bgc,key='-icon10B-')],
    c([sg.InputText(k='custom10',default_text=custom10,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap10')])
    ]
layoutR2c5 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon11-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon11col,key='-icon11C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon11bgc,key='-icon11B-')],
    c([sg.InputText(k='custom11',default_text=custom11,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap11')])
    ]
layoutR3c1 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon12-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon12col,key='-icon12C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon12bgc,key='-icon12B-')],
    c([sg.InputText(k='custom12',default_text=custom12,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap12')])
    ]
layoutR3c2 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon13-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon13col,key='-icon13C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon13bgc,key='-icon13B-')],
    c([sg.InputText(k='custom13',default_text=custom13,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap13')])
    ]
layoutR3c3 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon14-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon14col,key='-icon14C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon14bgc,key='-icon14B-')],
    c([sg.InputText(k='custom14',default_text=custom14,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap14')])
    ]
layoutR3c4 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon15-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon15col,key='-icon15C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon15bgc,key='-icon15B-')],
    c([sg.InputText(k='custom15',default_text=custom15,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap15')])
    ]
layoutR3c5 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon16-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon16col,key='-icon16C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon16bgc,key='-icon16B-')],
    c([sg.InputText(k='custom16',default_text=custom16,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap16')])
    ]
layoutR3c6 = [
    c([(sg.Graph((128,128), (0,0), (128,128), key='-Icon17-'))]),
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow','Default'], size=(16, 99),default_value=icon17col,key='-icon17C-')],
    [sg.InputCombo(['None.','White','Black','Blue','Cyan','Dark-Blue','Dark-Cyan','Dark-Green','Dark-Grey','Dark-Red','Dark-Yellow','Green','Grey','Pink','Purple','Red','Yellow', 'Custom','Snapshot'], size=(16, 99),default_value=icon17bgc,key='-icon17B-')],
    c([sg.InputText(k='custom17',default_text=custom17,visible=False),sg.FileBrowse(button_text='Custom Image',s=13,file_types=(('Images', '*.png *.jpg *.gif *.bmp'),('ALL','*.* *'))),sg.Button("O",key='Snap17')])
    ]
    
layoutx = [
    [sg.Text('VITA ICON GENERATOR',font=('Arial', 18)),sg.Text('by ahjones',font=('Arial', 8)),sg.Stretch(),sg.Button('Minimise',s=11),sg.Button('- RESET ALL ICONS -',s=20,button_color=('White','Maroon')), sg.Button('-CLOSE-',s=11,button_color=('White','Black'))],
    [sg.HorizontalSeparator()],
    c([sg.Column(layoutR1c1), sg.Column(layoutR1c2), sg.Column(layoutR1c3), sg.Column(layoutR1c4), sg.Column(layoutR1c5), sg.Column(layoutR1c6)]),
    c([sg.Column(layoutR2c1), sg.Column(layoutR2c2), sg.Column(layoutR2c3), sg.Column(layoutR2c4), sg.Column(layoutR2c5)]),
    c([sg.Column(layoutR3c1), sg.Column(layoutR3c2), sg.Column(layoutR3c3), sg.Column(layoutR3c4), sg.Column(layoutR3c5), sg.Column(layoutR3c6)]),
    c([sg.ProgressBar(32,orientation='h', bar_color=('Yellow','#001D3C'),size=(50, 20),key='-progressbar-')]),
    [sg.HorizontalSeparator()],
    [sg.Button("Match all Icon colors\nwith the 1st icon",s=(20,2),button_color=('White','DeepPink4')),sg.Button("Match all Backgrounds\nwith the 1st icon",s=(20,2),button_color=('White','DeepPink4')),sg.Stretch(),sg.Button("Open capture mask for ALL",key='CutALL',s=25,button_color=('Yellow','#6f6f6f')),sg.Button("Capture all",key='SnapALL',s=12),sg.Stretch(),sg.Button("- CREATE ICON SET -",s=(23),button_color=('White','Black'))],
    ]
layout = [[sg.Column(layoutx)]]

def MINIMISED_VIEW():
    layoutMIN = [
        [sg.Text('ICON GENERATOR - MINIMISED',background_color='Maroon')],
        [sg.Button('Restore',s=15,k='OK')]
        ]

    layoutMINx = [[sg.Column(layoutMIN,background_color='Maroon',element_justification='center')]]
    windowMIN = sg.Window('Minimised', layoutMINx, grab_anywhere=True, no_titlebar=True, keep_on_top=True, finalize=True, background_color='Brown',margins=(0,0))

    while True:
        eventM, valuesM = windowMIN.read()
        if eventM == sg.WIN_CLOSED or eventM == 'Cancel':
            break
        if eventM == 'OK':
            windowMIN.close()
            break
            
window = sg.Window('VITA ICON GENERATOR', layout, transparent_color='#000001',no_titlebar=True, keep_on_top=True, grab_anywhere=True, background_color='#015BBB',margins=(0,0), finalize=True)
window['-progressbar-'].update(current_count=0)

if 1==1:    #   THIS IS JUST SO I COULD FOLD AWAY THIS PART OF THE SCRIPT
    custom1_old = (custom1)
    custom2_old = (custom2)
    custom3_old = (custom3)
    custom4_old = (custom4)
    custom5_old = (custom5)
    custom6_old = (custom6)
    custom7_old = (custom7)
    custom8_old = (custom8)
    custom9_old = (custom9)
    custom10_old = (custom10)
    custom11_old = (custom11)
    custom12_old = (custom12)
    custom13_old = (custom13)
    custom14_old = (custom14)
    custom15_old = (custom15)
    custom16_old = (custom16)
    custom17_old = (custom17)
    Icon1_old = ("")
    Icon2_old = ("")
    Icon3_old = ("")
    Icon4_old = ("")
    Icon5_old = ("")
    Icon6_old = ("")
    Icon7_old = ("")
    Icon8_old = ("")
    Icon9_old = ("")
    Icon10_old = ("")
    Icon11_old = ("")
    Icon12_old = ("")
    Icon13_old = ("")
    Icon14_old = ("")
    Icon15_old = ("")
    Icon16_old = ("")
    Icon17_old = ("")
    oldSnap=0

while True:
    event, values = window.read(timeout=1)
    window['-progressbar-'].update(current_count=0)
    old_icon_color = values['-icon1C-']
    
    if not values['custom1'] == custom1:    # CHECK TO SEE IF THE CUSTOM FILE HAS CHANGED THEN CREATE TEMP FILE
        custom1_old = values['custom1']
        custom1 = values['custom1']
        Icon1_old = ('UPDADED')
        window['-icon1B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom1)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_web.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=1)
    if not values['custom2'] == custom2:
        custom2_old = values['custom2']
        custom2 = values['custom2']
        Icon2_old = ('UPDADED')
        window['-icon2B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom2)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_trophies.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=2)
    if not values['custom3'] == custom3:
        custom3_old = values['custom3']
        custom3 = values['custom3']
        Icon3_old = ('UPDADED')
        window['-icon3B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom3)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_friends.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=3)
    if not values['custom4'] == custom4:
        custom4_old = values['custom4']
        custom4 = values['custom4']
        Icon4_old = ('UPDADED')
        window['-icon4B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom4)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_messages.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=4)
    if not values['custom5'] == custom5:
        custom5_old = values['custom5']
        custom5 = values['custom5']
        Icon5_old = ('UPDADED')
        window['-icon5B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom5)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_party.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=5)
    if not values['custom6'] == custom6:
        custom6_old = values['custom6']
        custom6 = values['custom6']
        Icon6_old = ('UPDADED')
        window['-icon6B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom6)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_ps4link.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=6)
    if not values['custom7'] == custom7:
        custom7_old = values['custom7']
        custom7 = values['custom7']
        Icon7_old = ('UPDADED')
        window['-icon7B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom7)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_parental.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=7)
    if not values['custom8'] == custom8:
        custom8_old = values['custom8']
        custom8 = values['custom8']
        Icon8_old = ('UPDADED')
        window['-icon8B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom8)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_music.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=8)
    if not values['custom9'] == custom9:
        custom9_old = values['custom9']
        custom9 = values['custom9']
        Icon9_old = ('UPDADED')
        window['-icon9B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom9)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_videos.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=9)
    if not values['custom10'] == custom10:
        custom10_old = values['custom10']
        custom10 = values['custom10']
        Icon10_old = ('UPDADED')
        window['-icon10B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom10)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_ps3link.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=10)
    if not values['custom11'] == custom11:
        custom11_old = values['custom11']
        custom11 = values['custom11']
        Icon11_old = ('UPDADED')
        window['-icon11B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom11)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_cma.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=11)
    if not values['custom12'] == custom12:
        custom12_old = values['custom12']
        custom12 = values['custom12']
        Icon12_old = ('UPDADED')
        window['-icon12B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom12)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_settings.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=12)
    if not values['custom13'] == custom13:
        custom13_old = values['custom13']
        custom13 = values['custom13']
        Icon13_old = ('UPDADED')
        window['-icon13B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom13)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_calendar.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=13)
    if not values['custom14'] == custom14:
        custom14_old = values['custom14']
        custom14 = values['custom14']
        Icon14_old = ('UPDADED')
        window['-icon14B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom14)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_mail.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=14)
    if not values['custom15'] == custom15:
        custom15_old = values['custom15']
        custom15 = values['custom15']
        Icon15_old = ('UPDADED')
        window['-icon15B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom15)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_near.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=15)
    if not values['custom16'] == custom16:
        custom16_old = values['custom16']
        custom16 = values['custom16']
        Icon16_old = ('UPDADED')
        window['-icon16B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom16)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_photos.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=16)
    if not values['custom17'] == custom17:
        custom17_old = values['custom17']
        custom17 = values['custom17']
        Icon17_old = ('UPDADED')
        window['-icon17B-'].update('Custom')
        cmdA = ('call assets\scale.bat -source "{}" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(custom17)
        cmdB = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp.png" -o "assets\IconBuilder\Overlays\Custom\icon_power.png"')
        os.system(cmdA)
        os.system(cmdB)
        if CloneAll==1: window['-progressbar-'].update(current_count=17)

    if event == sg.WIN_CLOSED or event == '-CLOSE-': # CHECK IF THE WINDOW WAS CLOSED
        break
    
    if event == 'Minimise':         # MINIMISE THE MAIN WINDOW
        window.hide()
        MINIMISED_VIEW()
        window.UnHide()

    if event == 'CutALL':       # MAKE ALL THE ICONS SEE THROUGH FOR THE SNAPSHOT FEATURE
            window['-icon1B-'].update('Snapshot')
            window['-icon2B-'].update('Snapshot')
            window['-icon3B-'].update('Snapshot')
            window['-icon4B-'].update('Snapshot')
            window['-icon5B-'].update('Snapshot')
            window['-icon6B-'].update('Snapshot')
            window['-icon7B-'].update('Snapshot')
            window['-icon8B-'].update('Snapshot')
            window['-icon9B-'].update('Snapshot')
            window['-icon10B-'].update('Snapshot')
            window['-icon11B-'].update('Snapshot')
            window['-icon12B-'].update('Snapshot')
            window['-icon13B-'].update('Snapshot')
            window['-icon14B-'].update('Snapshot')
            window['-icon15B-'].update('Snapshot')
            window['-icon16B-'].update('Snapshot')
            window['-icon17B-'].update('Snapshot')
            window['Snap1'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap2'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap3'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap4'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap5'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap6'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap7'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap8'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap9'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap10'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap11'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap12'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap13'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap14'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap15'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap16'].update(button_color=('Yellow','#6f6f6f'))
            window['Snap17'].update(button_color=('Yellow','#6f6f6f'))
    
    if event == 'SnapALL':      # TAKE A SNAPSHOT FOR ALL ICONS AT THE SAME TIME
            window['Snap1'].update(button_color=default_button)
            window['Snap2'].update(button_color=default_button)
            window['Snap3'].update(button_color=default_button)
            window['Snap4'].update(button_color=default_button)
            window['Snap5'].update(button_color=default_button)
            window['Snap6'].update(button_color=default_button)
            window['Snap7'].update(button_color=default_button)
            window['Snap8'].update(button_color=default_button)
            window['Snap9'].update(button_color=default_button)
            window['Snap10'].update(button_color=default_button)
            window['Snap11'].update(button_color=default_button)
            window['Snap12'].update(button_color=default_button)
            window['Snap13'].update(button_color=default_button)
            window['Snap14'].update(button_color=default_button)
            window['Snap15'].update(button_color=default_button)
            window['Snap16'].update(button_color=default_button)
            window['Snap17'].update(button_color=default_button)
            custom1_old = values['custom1']
            custom2_old = values['custom2']
            custom3_old = values['custom3']
            custom4_old = values['custom4']
            custom5_old = values['custom5']
            custom6_old = values['custom6']
            custom7_old = values['custom7']
            custom8_old = values['custom8']
            custom9_old = values['custom9']
            custom10_old = values['custom10']
            custom11_old = values['custom11']
            custom12_old = values['custom12']
            custom13_old = values['custom13']
            custom14_old = values['custom14']
            custom15_old = values['custom15']
            custom16_old = values['custom16']
            custom17_old = values['custom17']
            custom1 = values['custom1']
            custom2 = values['custom2']
            custom3 = values['custom3']
            custom4 = values['custom4']
            custom5 = values['custom5']
            custom6 = values['custom6']
            custom7 = values['custom7']
            custom8 = values['custom8']
            custom9 = values['custom9']
            custom10 = values['custom10']
            custom11 = values['custom11']
            custom12 = values['custom12']
            custom13 = values['custom13']
            custom14 = values['custom14']
            custom15 = values['custom15']
            custom16 = values['custom16']
            custom17 = values['custom17']
            Icon1_old = ('UPDADED')
            Icon2_old = ('UPDADED')
            Icon3_old = ('UPDADED')
            Icon4_old = ('UPDADED')
            Icon5_old = ('UPDADED')
            Icon6_old = ('UPDADED')
            Icon7_old = ('UPDADED')
            Icon8_old = ('UPDADED')
            Icon9_old = ('UPDADED')
            Icon10_old = ('UPDADED')
            Icon11_old = ('UPDADED')
            Icon12_old = ('UPDADED')
            Icon13_old = ('UPDADED')
            Icon14_old = ('UPDADED')
            Icon15_old = ('UPDADED')
            Icon16_old = ('UPDADED')
            Icon17_old = ('UPDADED')
            window['-icon1B-'].update('Custom')
            window['-icon2B-'].update('Custom')
            window['-icon3B-'].update('Custom')
            window['-icon4B-'].update('Custom')
            window['-icon5B-'].update('Custom')
            window['-icon6B-'].update('Custom')
            window['-icon7B-'].update('Custom')
            window['-icon8B-'].update('Custom')
            window['-icon9B-'].update('Custom')
            window['-icon10B-'].update('Custom')
            window['-icon11B-'].update('Custom')
            window['-icon12B-'].update('Custom')
            window['-icon13B-'].update('Custom')
            window['-icon14B-'].update('Custom')
            window['-icon15B-'].update('Custom')
            window['-icon16B-'].update('Custom')
            window['-icon17B-'].update('Custom')
            
            cur=1
            while cur<18:
                ICON_NUM = ("-Icon"+str(cur)+"-")
                graph = window[ICON_NUM]
                bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
                if cur==1: ImageGrab.grab(bbox=bbox).save('assets\IconBuilder\Overlays\Custom\icon_web.png')
                if cur==2: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_trophies.png')
                if cur==3: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_friends.png')
                if cur==4: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_messages.png')
                if cur==5: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_party.png')
                if cur==6: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_ps4link.png')
                if cur==7: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_parental.png')
                if cur==8: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_music.png')
                if cur==9: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_videos.png')
                if cur==10: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_ps3link.png')
                if cur==11: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_cma.png')
                if cur==12: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_settings.png')
                if cur==13: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_calendar.png')
                if cur==14: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_mail.png')
                if cur==15: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_near.png')
                if cur==16: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_photos.png')
                if cur==17: ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_power.png')
                cur+=1
        
    if event == 'Snap1':        # OPEN OR TAKE A SNAPSHOT FOR ICON 1 AND SET THE IMAGE READY FOR CLONING
        if not values['-icon1B-'] == 'Snapshot':
            old_icon_color = values['-icon1C-']
            window['-icon1B-'].update('Snapshot')
            window['-icon1C-'].update('None.')
            window['Snap1'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap1'].update(button_color=default_button)
            window['-icon1B-'].update('Custom')
            window['-icon1C-'].update(old_icon_color)
            graph = window['-Icon1-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets\IconBuilder\Overlays\Custom\icon_web.png')
            if os.path.exists('assets\IconBuilder\TEMP\Snap'+str(SnapCount)+'.png'):
                os.remove('assets\IconBuilder\TEMP\Snap'+str(SnapCount)+'.png')
            SnapCount+=1
            ImageGrab.grab(bbox=bbox).save('assets\IconBuilder\TEMP\Snap'+str(SnapCount)+'.png')
            window['custom1'].update('assets\IconBuilder\TEMP\Snap'+str(SnapCount)+'.png')
    if event == 'Snap2':        # OPEN OR TAKE A SNAPSHOT FOR ICON 2 ONLY
        if not values['-icon2B-'] == 'Snapshot':
            window['-icon2B-'].update('Snapshot')
            window['Snap2'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap2'].update(button_color=default_button)
            window['-icon2B-'].update('Custom')
            graph = window['-Icon2-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_trophies.png')
    if event == 'Snap3':
        if not values['-icon3B-'] == 'Snapshot':
            window['-icon3B-'].update('Snapshot')
            window['Snap3'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap3'].update(button_color=default_button)
            window['-icon3B-'].update('Custom')
            graph = window['-Icon3-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_friends.png')
    if event == 'Snap4':
        if not values['-icon4B-'] == 'Snapshot':
            window['-icon4B-'].update('Snapshot')
            window['Snap4'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap4'].update(button_color=default_button)
            window['-icon4B-'].update('Custom')
            graph = window['-Icon4-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_messages.png')
    if event == 'Snap5':
        if not values['-icon5B-'] == 'Snapshot':
            window['-icon5B-'].update('Snapshot')
            window['Snap5'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap5'].update(button_color=default_button)
            window['-icon5B-'].update('Custom')        
            graph = window['-Icon5-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_party.png')
    if event == 'Snap6':
        if not values['-icon6B-'] == 'Snapshot':
            window['-icon6B-'].update('Snapshot')
            window['Snap6'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap6'].update(button_color=default_button)
            window['-icon6B-'].update('Custom')
            graph = window['-Icon6-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_ps4link.png')
    if event == 'Snap7':
        if not values['-icon7B-'] == 'Snapshot':
            window['-icon7B-'].update('Snapshot')
            window['Snap7'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap7'].update(button_color=default_button)
            window['-icon7B-'].update('Custom')
            graph = window['-Icon7-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_parental.png')
    if event == 'Snap8':
        if not values['-icon8B-'] == 'Snapshot':
            window['-icon8B-'].update('Snapshot')
            window['Snap8'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap8'].update(button_color=default_button)
            window['-icon8B-'].update('Custom')
            graph = window['-Icon8-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_music.png')
    if event == 'Snap9':
        if not values['-icon9B-'] == 'Snapshot':
            window['-icon9B-'].update('Snapshot')
            window['Snap9'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap9'].update(button_color=default_button)
            window['-icon9B-'].update('Custom')
            graph = window['-Icon9-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_videos.png')
    if event == 'Snap10':
        if not values['-icon10B-'] == 'Snapshot':
            window['-icon10B-'].update('Snapshot')
            window['Snap10'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap10'].update(button_color=default_button)
            window['-icon10B-'].update('Custom')        
            graph = window['-Icon10-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_ps3link.png')
    if event == 'Snap11':
        if not values['-icon11B-'] == 'Snapshot':
            window['-icon11B-'].update('Snapshot')
            window['Snap11'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap11'].update(button_color=default_button)
            window['-icon11B-'].update('Custom')
            graph = window['-Icon11-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_cma.png')
    if event == 'Snap12':
        if not values['-icon12B-'] == 'Snapshot':
            window['-icon12B-'].update('Snapshot')
            window['Snap12'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap12'].update(button_color=default_button)
            window['-icon12B-'].update('Custom')
            graph = window['-Icon12-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_settings.png')
    if event == 'Snap13':
        if not values['-icon13B-'] == 'Snapshot':
            window['-icon13B-'].update('Snapshot')
            window['Snap13'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap13'].update(button_color=default_button)
            window['-icon13B-'].update('Custom')
            graph = window['-Icon13-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_calendar.png')
    if event == 'Snap14':
        if not values['-icon14B-'] == 'Snapshot':
            window['-icon14B-'].update('Snapshot')
            window['Snap14'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap14'].update(button_color=default_button)
            window['-icon14B-'].update('Custom')
            graph = window['-Icon14-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_mail.png')
    if event == 'Snap15':
        if not values['-icon15B-'] == 'Snapshot':
            window['-icon15B-'].update('Snapshot')
            window['Snap15'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap15'].update(button_color=default_button)
            window['-icon15B-'].update('Custom')            
            graph = window['-Icon15-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_near.png')
    if event == 'Snap16':
        if not values['-icon16B-'] == 'Snapshot':
            window['-icon16B-'].update('Snapshot')
            window['Snap16'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap16'].update(button_color=default_button)
            window['-icon16B-'].update('Custom')
            graph = window['-Icon16-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_photos.png')
    if event == 'Snap17':
        if not values['-icon17B-'] == 'Snapshot':
            window['-icon17B-'].update('Snapshot')
            window['Snap17'].update(button_color=('Yellow','#6f6f6f'))
        else:
            window['Snap17'].update(button_color=default_button)
            window['-icon17B-'].update('Custom')
            graph = window['-Icon17-']
            bbox = graph.Widget.winfo_rootx(), graph.Widget.winfo_rooty(), graph.Widget.winfo_rootx() + graph.Widget.winfo_width(), graph.Widget.winfo_rooty() + graph.Widget.winfo_height()
            ImageGrab.grab(bbox=bbox).save('assets/IconBuilder/Overlays/Custom/icon_power.png')

    if event == 'Match all Icon colors\nwith the 1st icon':
        window['-icon2C-'].update(values['-icon1C-'])
        window['-icon3C-'].update(values['-icon1C-'])
        window['-icon4C-'].update(values['-icon1C-'])
        window['-icon5C-'].update(values['-icon1C-'])
        window['-icon6C-'].update(values['-icon1C-'])
        window['-icon7C-'].update(values['-icon1C-'])
        window['-icon8C-'].update(values['-icon1C-'])
        window['-icon9C-'].update(values['-icon1C-'])
        window['-icon10C-'].update(values['-icon1C-'])
        window['-icon11C-'].update(values['-icon1C-'])
        window['-icon12C-'].update(values['-icon1C-'])
        window['-icon13C-'].update(values['-icon1C-'])
        window['-icon14C-'].update(values['-icon1C-'])
        window['-icon15C-'].update(values['-icon1C-'])
        window['-icon16C-'].update(values['-icon1C-'])
        window['-icon17C-'].update(values['-icon1C-'])    
    if event == 'Match all Backgrounds\nwith the 1st icon':
        CloneAll=1
        window['-icon2B-'].update(values['-icon1B-'])
        window['-icon3B-'].update(values['-icon1B-'])
        window['-icon4B-'].update(values['-icon1B-'])
        window['-icon5B-'].update(values['-icon1B-'])
        window['-icon6B-'].update(values['-icon1B-'])
        window['-icon7B-'].update(values['-icon1B-'])
        window['-icon8B-'].update(values['-icon1B-'])
        window['-icon9B-'].update(values['-icon1B-'])
        window['-icon10B-'].update(values['-icon1B-'])
        window['-icon11B-'].update(values['-icon1B-'])
        window['-icon12B-'].update(values['-icon1B-'])
        window['-icon13B-'].update(values['-icon1B-'])
        window['-icon14B-'].update(values['-icon1B-'])
        window['-icon15B-'].update(values['-icon1B-'])
        window['-icon16B-'].update(values['-icon1B-'])
        window['-icon17B-'].update(values['-icon1B-'])
        
        window['custom2'].update(values['custom1'])
        window['custom3'].update(values['custom1'])
        window['custom4'].update(values['custom1'])
        window['custom5'].update(values['custom1'])
        window['custom6'].update(values['custom1'])
        window['custom7'].update(values['custom1'])
        window['custom8'].update(values['custom1'])
        window['custom9'].update(values['custom1'])
        window['custom10'].update(values['custom1'])
        window['custom11'].update(values['custom1'])
        window['custom12'].update(values['custom1'])
        window['custom13'].update(values['custom1'])
        window['custom14'].update(values['custom1'])
        window['custom15'].update(values['custom1'])
        window['custom16'].update(values['custom1'])
        window['custom17'].update(values['custom1'])
    if event == '- RESET ALL ICONS -':
        window['-icon1C-'].update('White')
        window['-icon1B-'].update('None.')
        window['-icon2C-'].update('White')
        window['-icon2B-'].update('None.')
        window['-icon3C-'].update('White')
        window['-icon3B-'].update('None.')
        window['-icon4C-'].update('White')
        window['-icon4B-'].update('None.')
        window['-icon5C-'].update('White')
        window['-icon5B-'].update('None.')
        window['-icon6C-'].update('White')
        window['-icon6B-'].update('None.')
        window['-icon7C-'].update('White')
        window['-icon7B-'].update('None.')
        window['-icon8C-'].update('White')
        window['-icon8B-'].update('None.')
        window['-icon9C-'].update('White')
        window['-icon9B-'].update('None.')
        window['-icon10C-'].update('White')
        window['-icon10B-'].update('None.')
        window['-icon11C-'].update('White')
        window['-icon11B-'].update('None.')
        window['-icon12C-'].update('White')
        window['-icon12B-'].update('None.')
        window['-icon13C-'].update('White')
        window['-icon13B-'].update('None.')
        window['-icon14C-'].update('White')
        window['-icon14B-'].update('None.')
        window['-icon15C-'].update('White')
        window['-icon15B-'].update('None.')
        window['-icon16C-'].update('White')
        window['-icon16B-'].update('None.')
        window['-icon17C-'].update('White')
        window['-icon17B-'].update('None.')
        
        settings["ICON_GENERATOR"]["Icon1Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon2Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon3Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon4Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon5Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon6Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon7Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon8Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon9Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon10Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon11Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon12Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon13Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon14Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon15Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon16Color"] = 'White'
        settings["ICON_GENERATOR"]["Icon17Color"] = 'White'
        
        settings["ICON_GENERATOR"]["Icon1Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon2Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon3Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon4Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon5Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon6Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon7Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon8Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon9Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon10Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon11Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon12Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon13Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon14Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon15Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon16Background"] = 'None.'
        settings["ICON_GENERATOR"]["Icon17Background"] = 'None.'
        
        settings["ICON_GENERATOR"]["Icon1CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon2CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon3CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon4CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon5CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon6CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon7CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon8CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon9CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon10CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon11CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon12CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon13CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon14CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon15CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon16CustomBackground"] = ""
        settings["ICON_GENERATOR"]["Icon17CustomBackground"] = ""

    if not Icon1_old == values['-icon1C-']+values['-icon1B-']:      # BUILD ICON BY MERGING THE OVERLAY AND BACKGROUND
        Icon1_old = values['-icon1C-']+values['-icon1B-']
        window['-Icon1-'].erase()
        icon1col = values['-icon1C-']
        icon1bgc = values['-icon1B-']
        icon1file = 'assets/IconBuilder/Overlays/' + icon1col + '/icon_web.png'
        icon1bgnd = 'assets/IconBuilder/Colors/' + icon1bgc + '.png'
        if values['-icon1B-'] == 'Custom': icon1bgnd = 'assets/IconBuilder/Overlays/Custom/icon_web.png'
        if Path(icon1bgnd).is_file(): window['-Icon1-'].draw_image(filename=icon1bgnd, location=(0,128))
        if Path(icon1file).is_file(): window['-Icon1-'].draw_image(filename=icon1file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=18)
    if not Icon2_old == values['-icon2C-']+values['-icon2B-']:
        Icon2_old = values['-icon2C-']+values['-icon2B-']
        window['-Icon2-'].erase()
        icon2col = values['-icon2C-']
        icon2bgc = values['-icon2B-']
        icon2file = 'assets/IconBuilder/Overlays/' + icon2col + '/icon_trophies.png'
        icon2bgnd = 'assets/IconBuilder/Colors/' + icon2bgc + '.png'
        if values['-icon2B-'] == 'Custom': icon2bgnd = 'assets/IconBuilder/Overlays/Custom/icon_trophies.png'
        if Path(icon2bgnd).is_file(): window['-Icon2-'].draw_image(filename=icon2bgnd, location=(0,128))
        if Path(icon2file).is_file(): window['-Icon2-'].draw_image(filename=icon2file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=19)
    if not Icon3_old == values['-icon3C-']+values['-icon3B-']:
        Icon3_old = values['-icon3C-']+values['-icon3B-']
        window['-Icon3-'].erase()
        icon3col = values['-icon3C-']
        icon3bgc = values['-icon3B-']
        icon3file = 'assets/IconBuilder/Overlays/' + icon3col + '/icon_friends.png'
        icon3bgnd = 'assets/IconBuilder/Colors/' + icon3bgc + '.png'
        if values['-icon3B-'] == 'Custom': icon3bgnd = 'assets/IconBuilder/Overlays/Custom/icon_friends.png'
        if Path(icon3bgnd).is_file(): window['-Icon3-'].draw_image(filename=icon3bgnd, location=(0,128))
        if Path(icon3file).is_file(): window['-Icon3-'].draw_image(filename=icon3file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=20)
    if not Icon4_old == values['-icon4C-']+values['-icon4B-']:
        Icon4_old = values['-icon4C-']+values['-icon4B-']
        window['-Icon4-'].erase()
        icon4col = values['-icon4C-']
        icon4bgc = values['-icon4B-']
        icon4file = 'assets/IconBuilder/Overlays/' + icon4col + '/icon_messages.png'
        icon4bgnd = 'assets/IconBuilder/Colors/' + icon4bgc + '.png'
        if values['-icon4B-'] == 'Custom': icon4bgnd = 'assets/IconBuilder/Overlays/Custom/icon_messages.png'
        if Path(icon4bgnd).is_file(): window['-Icon4-'].draw_image(filename=icon4bgnd, location=(0,128))
        if Path(icon4file).is_file(): window['-Icon4-'].draw_image(filename=icon4file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=21)
    if not Icon5_old == values['-icon5C-']+values['-icon5B-']:
        Icon5_old = values['-icon5C-']+values['-icon5B-']
        window['-Icon5-'].erase()
        icon5col = values['-icon5C-']
        icon5bgc = values['-icon5B-']
        icon5file = 'assets/IconBuilder/Overlays/' + icon5col + '/icon_party.png'
        icon5bgnd = 'assets/IconBuilder/Colors/' + icon5bgc + '.png'
        if values['-icon5B-'] == 'Custom': icon5bgnd = 'assets/IconBuilder/Overlays/Custom/icon_party.png'
        if Path(icon5bgnd).is_file(): window['-Icon5-'].draw_image(filename=icon5bgnd, location=(0,128))
        if Path(icon5file).is_file(): window['-Icon5-'].draw_image(filename=icon5file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=22)
    if not Icon6_old == values['-icon6C-']+values['-icon6B-']:
        Icon6_old = values['-icon6C-']+values['-icon6B-']
        window['-Icon6-'].erase()
        icon6col = values['-icon6C-']
        icon6bgc = values['-icon6B-']
        icon6file = 'assets/IconBuilder/Overlays/' + icon6col + '/icon_ps4link.png'
        icon6bgnd = 'assets/IconBuilder/Colors/' + icon6bgc + '.png'
        if values['-icon6B-'] == 'Custom': icon6bgnd = 'assets/IconBuilder/Overlays/Custom/icon_ps4link.png'
        if Path(icon6bgnd).is_file(): window['-Icon6-'].draw_image(filename=icon6bgnd, location=(0,128))
        if Path(icon6file).is_file(): window['-Icon6-'].draw_image(filename=icon6file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=23)
    if not Icon7_old == values['-icon7C-']+values['-icon7B-']:
        Icon7_old = values['-icon7C-']+values['-icon7B-']
        window['-Icon7-'].erase()
        icon7col = values['-icon7C-']
        icon7bgc = values['-icon7B-']
        icon7file = 'assets/IconBuilder/Overlays/' + icon7col + '/icon_parental.png'
        icon7bgnd = 'assets/IconBuilder/Colors/' + icon7bgc + '.png'
        if values['-icon7B-'] == 'Custom': icon7bgnd = 'assets/IconBuilder/Overlays/Custom/icon_parental.png'
        if Path(icon7bgnd).is_file(): window['-Icon7-'].draw_image(filename=icon7bgnd, location=(0,128))
        if Path(icon7file).is_file(): window['-Icon7-'].draw_image(filename=icon7file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=24)
    if not Icon8_old == values['-icon8C-']+values['-icon8B-']:
        Icon8_old = values['-icon8C-']+values['-icon8B-']
        window['-Icon8-'].erase()
        icon8col = values['-icon8C-']
        icon8bgc = values['-icon8B-']
        icon8file = 'assets/IconBuilder/Overlays/' + icon8col + '/icon_music.png'
        icon8bgnd = 'assets/IconBuilder/Colors/' + icon8bgc + '.png'
        if values['-icon8B-'] == 'Custom': icon8bgnd = 'assets/IconBuilder/Overlays/Custom/icon_music.png'
        if Path(icon8bgnd).is_file(): window['-Icon8-'].draw_image(filename=icon8bgnd, location=(0,128))
        if Path(icon8file).is_file(): window['-Icon8-'].draw_image(filename=icon8file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=25)
    if not Icon9_old == values['-icon9C-']+values['-icon9B-']:
        Icon9_old = values['-icon9C-']+values['-icon9B-']
        window['-Icon9-'].erase()
        icon9col = values['-icon9C-']
        icon9bgc = values['-icon9B-']
        icon9file = 'assets/IconBuilder/Overlays/' + icon9col + '/icon_videos.png'
        icon9bgnd = 'assets/IconBuilder/Colors/' + icon9bgc + '.png'
        if values['-icon9B-'] == 'Custom': icon9bgnd = 'assets/IconBuilder/Overlays/Custom/icon_videos.png'
        if Path(icon9bgnd).is_file(): window['-Icon9-'].draw_image(filename=icon9bgnd, location=(0,128))
        if Path(icon9file).is_file(): window['-Icon9-'].draw_image(filename=icon9file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=26)
    if not Icon10_old == values['-icon10C-']+values['-icon10B-']:
        Icon10_old = values['-icon10C-']+values['-icon10B-']
        window['-Icon10-'].erase()
        icon10col = values['-icon10C-']
        icon10bgc = values['-icon10B-']
        icon10file = 'assets/IconBuilder/Overlays/' + icon10col + '/icon_ps3link.png'
        icon10bgnd = 'assets/IconBuilder/Colors/' + icon10bgc + '.png'
        if values['-icon10B-'] == 'Custom': icon10bgnd = 'assets/IconBuilder/Overlays/Custom/icon_ps3link.png'
        if Path(icon10bgnd).is_file(): window['-Icon10-'].draw_image(filename=icon10bgnd, location=(0,128))
        if Path(icon10file).is_file(): window['-Icon10-'].draw_image(filename=icon10file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=27)
    if not Icon11_old == values['-icon11C-']+values['-icon11B-']:
        Icon11_old = values['-icon11C-']+values['-icon11B-']
        window['-Icon11-'].erase()
        icon11col = values['-icon11C-']
        icon11bgc = values['-icon11B-']
        icon11file = 'assets/IconBuilder/Overlays/' + icon11col + '/icon_cma.png'
        icon11bgnd = 'assets/IconBuilder/Colors/' + icon11bgc + '.png'
        if values['-icon11B-'] == 'Custom': icon11bgnd = 'assets/IconBuilder/Overlays/Custom/icon_cma.png'
        if Path(icon11bgnd).is_file(): window['-Icon11-'].draw_image(filename=icon11bgnd, location=(0,128))
        if Path(icon11file).is_file(): window['-Icon11-'].draw_image(filename=icon11file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=28)
    if not Icon12_old == values['-icon12C-']+values['-icon12B-']:
        Icon12_old = values['-icon12C-']+values['-icon12B-']
        window['-Icon12-'].erase()
        icon12col = values['-icon12C-']
        icon12bgc = values['-icon12B-']
        icon12file = 'assets/IconBuilder/Overlays/' + icon12col + '/icon_settings.png'
        icon12bgnd = 'assets/IconBuilder/Colors/' + icon12bgc + '.png'
        if values['-icon12B-'] == 'Custom': icon12bgnd = 'assets/IconBuilder/Overlays/Custom/icon_settings.png'
        if Path(icon12bgnd).is_file(): window['-Icon12-'].draw_image(filename=icon12bgnd, location=(0,128))
        if Path(icon12file).is_file(): window['-Icon12-'].draw_image(filename=icon12file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=29)
    if not Icon13_old == values['-icon13C-']+values['-icon13B-']:
        Icon13_old = values['-icon13C-']+values['-icon13B-']
        window['-Icon13-'].erase()
        icon13col = values['-icon13C-']
        icon13bgc = values['-icon13B-']
        icon13file = 'assets/IconBuilder/Overlays/' + icon13col + '/icon_calendar.png'
        icon13bgnd = 'assets/IconBuilder/Colors/' + icon13bgc + '.png'
        if values['-icon13B-'] == 'Custom': icon13bgnd = 'assets/IconBuilder/Overlays/Custom/icon_calendar.png'
        if Path(icon13bgnd).is_file(): window['-Icon13-'].draw_image(filename=icon13bgnd, location=(0,128))
        if Path(icon13file).is_file(): window['-Icon13-'].draw_image(filename=icon13file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=30)
    if not Icon14_old == values['-icon14C-']+values['-icon14B-']:
        Icon14_old = values['-icon14C-']+values['-icon14B-']
        window['-Icon14-'].erase()
        icon14col = values['-icon14C-']
        icon14bgc = values['-icon14B-']
        icon14file = 'assets/IconBuilder/Overlays/' + icon14col + '/icon_mail.png'
        icon14bgnd = 'assets/IconBuilder/Colors/' + icon14bgc + '.png'
        if values['-icon14B-'] == 'Custom': icon14bgnd = 'assets/IconBuilder/Overlays/Custom/icon_mail.png'
        if Path(icon14bgnd).is_file(): window['-Icon14-'].draw_image(filename=icon14bgnd, location=(0,128))
        if Path(icon14file).is_file(): window['-Icon14-'].draw_image(filename=icon14file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=31)
    if not Icon15_old == values['-icon15C-']+values['-icon15B-']:
        Icon15_old = values['-icon15C-']+values['-icon15B-']
        window['-Icon15-'].erase()
        icon15col = values['-icon15C-']
        icon15bgc = values['-icon15B-']
        icon15file = 'assets/IconBuilder/Overlays/' + icon15col + '/icon_near.png'
        icon15bgnd = 'assets/IconBuilder/Colors/' + icon15bgc + '.png'
        if values['-icon15B-'] == 'Custom': icon15bgnd = 'assets/IconBuilder/Overlays/Custom/icon_near.png'
        if Path(icon15bgnd).is_file(): window['-Icon15-'].draw_image(filename=icon15bgnd, location=(0,128))
        if Path(icon15file).is_file(): window['-Icon15-'].draw_image(filename=icon15file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=32)
    if not Icon16_old == values['-icon16C-']+values['-icon16B-']:
        Icon16_old = values['-icon16C-']+values['-icon16B-']
        window['-Icon16-'].erase()
        icon16col = values['-icon16C-']
        icon16bgc = values['-icon16B-']
        icon16file = 'assets/IconBuilder/Overlays/' + icon16col + '/icon_photos.png'
        icon16bgnd = 'assets/IconBuilder/Colors/' + icon16bgc + '.png'
        if values['-icon16B-'] == 'Custom': icon16bgnd = 'assets/IconBuilder/Overlays/Custom/icon_photos.png'
        if Path(icon16bgnd).is_file(): window['-Icon16-'].draw_image(filename=icon16bgnd, location=(0,128))
        if Path(icon16file).is_file(): window['-Icon16-'].draw_image(filename=icon16file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=33)
    if not Icon17_old == values['-icon17C-']+values['-icon17B-']:
        Icon17_old = values['-icon17C-']+values['-icon17B-']
        window['-Icon17-'].erase()
        icon17col = values['-icon17C-']
        icon17bgc = values['-icon17B-']
        icon17file = 'assets/IconBuilder/Overlays/' + icon17col + '/icon_power.png'
        icon17bgnd = 'assets/IconBuilder/Colors/' + icon17bgc + '.png'
        if values['-icon17B-'] == 'Custom': icon17bgnd = 'assets/IconBuilder/Overlays/Custom/icon_power.png'
        if Path(icon17bgnd).is_file(): window['-Icon17-'].draw_image(filename=icon17bgnd, location=(0,128))
        if Path(icon17file).is_file(): window['-Icon17-'].draw_image(filename=icon17file, location=(0,128))
        if CloneAll==1: window['-progressbar-'].update(current_count=34)
        if CloneAll==1: CloneAll=0

    def ThemeNAME():            # SAVE AS
        global SetName
        SetName = ('')

        layoutTN = [
            [sg.Text("",s=40)],
            [sg.Text('Enter a name for this icon set')],
            [sg.Input(k='-ThemeNAME-',default_text=ThemeName,s=30)],
            [sg.Text()],
            [sg.Button('OK',s=12,k='OK',bind_return_key=True),sg.Button('Cancel',s=12)],
            [sg.Text()],
            ]

        layoutTNx = [[sg.Column(layoutTN,element_justification='center')]]
        windowTN = sg.Window('Theme Name', layoutTNx, grab_anywhere=True, no_titlebar=True, keep_on_top=True, finalize=True, background_color='#015BBB',margins=(0,0))
        windowTN['-ThemeNAME-'].SetFocus()
        windowTN['-ThemeNAME-'].Widget.icursor('end')
        while True:
            eventN, valuesN = windowTN.read()
            if eventN == sg.WIN_CLOSED or eventN == 'Cancel':
                windowTN.close()
                break
            if eventN == 'OK':
                SetName=valuesN['-ThemeNAME-']
                windowTN.close()
                break

    if event =='- CREATE ICON SET -':   # SAVE THE CURRENT SETTINGS AND GENERATE FINAL IMAGES INTO THE ICONSET\'THEMENAME' FOLDER
        settings["ICON_GENERATOR"]["filecheck"] = 'OK'
        settings["ICON_GENERATOR"]["Icon1Color"] = icon1col
        settings["ICON_GENERATOR"]["Icon2Color"] = icon2col
        settings["ICON_GENERATOR"]["Icon3Color"] = icon3col
        settings["ICON_GENERATOR"]["Icon4Color"] = icon4col
        settings["ICON_GENERATOR"]["Icon5Color"] = icon5col
        settings["ICON_GENERATOR"]["Icon6Color"] = icon6col
        settings["ICON_GENERATOR"]["Icon7Color"] = icon7col
        settings["ICON_GENERATOR"]["Icon8Color"] = icon8col
        settings["ICON_GENERATOR"]["Icon9Color"] = icon9col
        settings["ICON_GENERATOR"]["Icon10Color"] = icon10col
        settings["ICON_GENERATOR"]["Icon11Color"] = icon11col
        settings["ICON_GENERATOR"]["Icon12Color"] = icon12col
        settings["ICON_GENERATOR"]["Icon13Color"] = icon13col
        settings["ICON_GENERATOR"]["Icon14Color"] = icon14col
        settings["ICON_GENERATOR"]["Icon15Color"] = icon15col
        settings["ICON_GENERATOR"]["Icon16Color"] = icon16col
        settings["ICON_GENERATOR"]["Icon17Color"] = icon17col
        
        settings["ICON_GENERATOR"]["Icon1Background"] = icon1bgc
        settings["ICON_GENERATOR"]["Icon2Background"] = icon2bgc
        settings["ICON_GENERATOR"]["Icon3Background"] = icon3bgc
        settings["ICON_GENERATOR"]["Icon4Background"] = icon4bgc
        settings["ICON_GENERATOR"]["Icon5Background"] = icon5bgc
        settings["ICON_GENERATOR"]["Icon6Background"] = icon6bgc
        settings["ICON_GENERATOR"]["Icon7Background"] = icon7bgc
        settings["ICON_GENERATOR"]["Icon8Background"] = icon8bgc
        settings["ICON_GENERATOR"]["Icon9Background"] = icon9bgc
        settings["ICON_GENERATOR"]["Icon10Background"] = icon10bgc
        settings["ICON_GENERATOR"]["Icon11Background"] = icon11bgc
        settings["ICON_GENERATOR"]["Icon12Background"] = icon12bgc
        settings["ICON_GENERATOR"]["Icon13Background"] = icon13bgc
        settings["ICON_GENERATOR"]["Icon14Background"] = icon14bgc
        settings["ICON_GENERATOR"]["Icon15Background"] = icon15bgc
        settings["ICON_GENERATOR"]["Icon16Background"] = icon16bgc
        settings["ICON_GENERATOR"]["Icon17Background"] = icon17bgc
        settings["ICON_GENERATOR"]["Icon1CustomBackground"] = icon1bgnd
        settings["ICON_GENERATOR"]["Icon2CustomBackground"] = icon2bgnd
        settings["ICON_GENERATOR"]["Icon3CustomBackground"] = icon3bgnd
        settings["ICON_GENERATOR"]["Icon4CustomBackground"] = icon4bgnd
        settings["ICON_GENERATOR"]["Icon5CustomBackground"] = icon5bgnd
        settings["ICON_GENERATOR"]["Icon6CustomBackground"] = icon6bgnd
        settings["ICON_GENERATOR"]["Icon7CustomBackground"] = icon7bgnd
        settings["ICON_GENERATOR"]["Icon8CustomBackground"] = icon8bgnd
        settings["ICON_GENERATOR"]["Icon9CustomBackground"] = icon9bgnd
        settings["ICON_GENERATOR"]["Icon10CustomBackground"] = icon10bgnd
        settings["ICON_GENERATOR"]["Icon11CustomBackground"] = icon11bgnd
        settings["ICON_GENERATOR"]["Icon12CustomBackground"] = icon12bgnd
        settings["ICON_GENERATOR"]["Icon13CustomBackground"] = icon13bgnd
        settings["ICON_GENERATOR"]["Icon14CustomBackground"] = icon14bgnd
        settings["ICON_GENERATOR"]["Icon15CustomBackground"] = icon15bgnd
        settings["ICON_GENERATOR"]["Icon16CustomBackground"] = icon16bgnd
        settings["ICON_GENERATOR"]["Icon17CustomBackground"] = icon17bgnd

        ThemeNAME()
        
        if SetName == ('') or SetName == None:
            print ("ERROR.!")    
        else:
            layoutPG = [[sg.Text('Generating images...')],
                [sg.ProgressBar(17,orientation='h', bar_color=('Yellow','Grey'),size=(50, 20),key='-progressbar-')],]
                
            layoutPGx = [[sg.Column(layoutPG)]]
            windowx = sg.Window("Progress Bar", layoutPGx,keep_on_top=True,no_titlebar=True,background_color='#015BBB',margins=(0,0),modal=False)
            eventx, valuesx = windowx.read(10)
            
            windowx['-progressbar-'].update(current_count=0)
            cmdstart = ('md "IconSET\{}"').format(SetName)
            os.system(cmdstart)
            cmd1a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon1bgc)
            cmd1a = cmd1a.replace('assets\IconBuilder\Colors\Custom.png',icon1bgnd)
            cmd1b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_web.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon1col)
            cmd1c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_web.png"').format(SetName)
            os.system(cmd1a)
            os.system(cmd1b)
            os.system(cmd1c)
            windowx['-progressbar-'].update(current_count=1)
            cmd2a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon2bgc)
            cmd2a = cmd2a.replace('assets\IconBuilder\Colors\Custom.png',icon2bgnd)
            cmd2b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_trophies.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon2col)
            cmd2c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_trophies.png"').format(SetName)
            os.system(cmd2a)
            os.system(cmd2b)
            os.system(cmd2c)
            windowx['-progressbar-'].update(current_count=2)
            cmd3a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon3bgc)
            cmd3a = cmd3a.replace('assets\IconBuilder\Colors\Custom.png',icon3bgnd)
            cmd3b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_friends.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon3col)
            cmd3c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_friends.png"').format(SetName)
            os.system(cmd3a)
            os.system(cmd3b)
            os.system(cmd3c)
            windowx['-progressbar-'].update(current_count=3)
            cmd4a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon4bgc)
            cmd4a = cmd4a.replace('assets\IconBuilder\Colors\Custom.png',icon4bgnd)
            cmd4b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_messages.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon4col)
            cmd4c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_messages.png"').format(SetName)
            os.system(cmd4a)
            os.system(cmd4b)
            os.system(cmd4c)
            windowx['-progressbar-'].update(current_count=4)
            cmd5a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon5bgc)
            cmd5a = cmd5a.replace('assets\IconBuilder\Colors\Custom.png',icon5bgnd)
            cmd5b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_party.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon5col)
            cmd5c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_party.png"').format(SetName)
            os.system(cmd5a)
            os.system(cmd5b)
            os.system(cmd5c)
            windowx['-progressbar-'].update(current_count=5)
            cmd6a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon6bgc)
            cmd6a = cmd6a.replace('assets\IconBuilder\Colors\Custom.png',icon6bgnd)
            cmd6b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_ps4link.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon6col)
            cmd6c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_ps4link.png"').format(SetName)
            os.system(cmd6a)
            os.system(cmd6b)
            os.system(cmd6c)
            windowx['-progressbar-'].update(current_count=6)
            cmd7a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon7bgc)
            cmd7a = cmd7a.replace('assets\IconBuilder\Colors\Custom.png',icon7bgnd)
            cmd7b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_parental.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon7col)
            cmd7c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_parental.png"').format(SetName)
            os.system(cmd7a)
            os.system(cmd7b)
            os.system(cmd7c)
            windowx['-progressbar-'].update(current_count=7)
            cmd8a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon8bgc)
            cmd8a = cmd8a.replace('assets\IconBuilder\Colors\Custom.png',icon8bgnd)
            cmd8b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_music.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon8col)
            cmd8c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_music.png"').format(SetName)
            os.system(cmd8a)
            os.system(cmd8b)
            os.system(cmd8c)
            windowx['-progressbar-'].update(current_count=8)
            cmd9a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon9bgc)
            cmd9a = cmd9a.replace('assets\IconBuilder\Colors\Custom.png',icon9bgnd)
            cmd9b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_videos.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon9col)
            cmd9c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_videos.png"').format(SetName)
            os.system(cmd9a)
            os.system(cmd9b)
            os.system(cmd9c)
            windowx['-progressbar-'].update(current_count=9)
            cmd10a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon10bgc)
            cmd10a = cmd10a.replace('assets\IconBuilder\Colors\Custom.png',icon10bgnd)
            cmd10b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_ps3link.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon10col)
            cmd10c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_ps3link.png"').format(SetName)
            os.system(cmd10a)
            os.system(cmd10b)
            os.system(cmd10c)
            windowx['-progressbar-'].update(current_count=10)
            cmd11a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon11bgc)
            cmd11a = cmd11a.replace('assets\IconBuilder\Colors\Custom.png',icon11bgnd)
            cmd11b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_cma.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon11col)
            cmd11c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_cma.png"').format(SetName)
            os.system(cmd11a)
            os.system(cmd11b)
            os.system(cmd11c)
            windowx['-progressbar-'].update(current_count=11)
            cmd12a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon12bgc)
            cmd12a = cmd12a.replace('assets\IconBuilder\Colors\Custom.png',icon12bgnd)
            cmd12b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_settings.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon12col)
            cmd12c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_settings.png"').format(SetName)
            os.system(cmd12a)
            os.system(cmd12b)
            os.system(cmd12c)
            windowx['-progressbar-'].update(current_count=12)
            cmd13a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon13bgc)
            cmd13a = cmd13a.replace('assets\IconBuilder\Colors\Custom.png',icon13bgnd)
            cmd13b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_calendar.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon13col)
            cmd13c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_calendar.png"').format(SetName)
            os.system(cmd13a)
            os.system(cmd13b)
            os.system(cmd13c)
            windowx['-progressbar-'].update(current_count=13)
            cmd14a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon14bgc)
            cmd14a = cmd14a.replace('assets\IconBuilder\Colors\Custom.png',icon14bgnd)
            cmd14b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_mail.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon14col)
            cmd14c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_mail.png"').format(SetName)
            os.system(cmd14a)
            os.system(cmd14b)
            os.system(cmd14c)
            windowx['-progressbar-'].update(current_count=14)
            cmd15a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon15bgc)
            cmd15a = cmd15a.replace('assets\IconBuilder\Colors\Custom.png',icon15bgnd)
            cmd15b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_near.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon15col)
            cmd15c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_near.png"').format(SetName)
            os.system(cmd15a)
            os.system(cmd15b)
            os.system(cmd15c)
            windowx['-progressbar-'].update(current_count=15)
            cmd16a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon16bgc)
            cmd16a = cmd16a.replace('assets\IconBuilder\Colors\Custom.png',icon16bgnd)
            cmd16b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_photos.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon16col)
            cmd16c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_photos.png"').format(SetName)
            os.system(cmd16a)
            os.system(cmd16b)
            os.system(cmd16c)
            windowx['-progressbar-'].update(current_count=16)
            cmd17a = ('call assets\scale.bat -source "assets\IconBuilder\Colors\{}.png" -target "assets\IconBuilder\TEMP\Temp.png" -max-height 128 -max-width 128 -keep-ratio no -force yes').format(icon17bgc)
            cmd17a = cmd17a.replace('assets\IconBuilder\Colors\Custom.png',icon17bgnd)
            cmd17b = ('assets\combine composite "assets\IconBuilder\Overlays\{}\icon_power.png" "assets\IconBuilder\TEMP\Temp.png" "assets\IconBuilder\TEMP\Temp2.png"').format(icon17col)
            cmd17c = ('assets\pngquant.exe -f "assets\IconBuilder\TEMP\Temp2.png" -o "IconSet\{}\icon_power.png"').format(SetName)
            os.system(cmd17a)
            os.system(cmd17b)
            os.system(cmd17c)
            windowx['-progressbar-'].update(current_count=17)
            windowx.close()
            
