##################################################
## CUSTOM VITA THEME BUILDER - CREATED BY ANTHJ ##
##################################################

import PySimpleGUI as sg
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
sg.theme('PythonPlus')
sg.set_options(font=("Helvetica", 13))

def c(elems):
    return [sg.Stretch(), *elems, sg.Stretch()]

def MainMenu():
    layoutHELP = [
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("Help and Information",justification='c',s=18,font=('Helvetica', 20))]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Theme details',k='Theme details',s=20)]),
        c([sg.Button('Adding images',k='Adding images',s=20)]),
        c([sg.Button('Layout and colors',k='Layout and colors',s=20)]),
        c([sg.Button('Notifications',k='Notifications',s=20)]),
        c([sg.Button('Bubble (iconsets)',k='Bubble (iconsets)',s=20)]),
        c([sg.Button('Background music',k='Background music',s=20)]),
        c([sg.Text("")]),
        c([sg.Button('Generate theme',k='Generate theme',s=20)]),
        c([sg.Button('Install the theme',k='Install the theme',s=20)]),
        c([sg.Button('Export',k='Export',s=20)]),
        c([sg.Text("")]),
        c([sg.Button('Issues',k='Issues',s=20)]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',button_color=('Yellow','DarkGreen'),s=20)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
    window['Theme details'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
        if event == 'Theme details':
            HELP1()
            window['Adding images'].SetFocus()
        if event == 'Adding images':
            HELP2()
            window['Layout and colors'].SetFocus()
        if event == 'Layout and colors':
            HELP3()
            window['Notifications'].SetFocus()
        if event == 'Notifications':
            HELP4()
            window['Bubble (iconsets)'].SetFocus()
        if event == 'Bubble (iconsets)':
            HELP5()
            window['Background music'].SetFocus()
        if event == 'Background music':
            HELP6()
            window['Generate theme'].SetFocus()
        if event == 'Generate theme':
            HELP7()
            window['Install the theme'].SetFocus()
        if event == 'Install the theme':
            HELP8()
            window['Export'].SetFocus()
        if event == 'Export':
            HELP10()
            window['Issues'].SetFocus()
        if event == 'Issues':
            HELP9()
            window['Theme details'].SetFocus()

def HELP1():    # Theme details
    layoutHELP = [
        [sg.Text("Theme details",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("The first screen you will see will ask you to enter a name for your theme")]),
        c([sg.Text("type in a name for your theme and then press enter to select the next box")]),
        c([sg.Text("")]),
        c([sg.Text("The next box is the theme version. Unless you are editing an existing theme")]),
        c([sg.Text("this can be left set to version 01.00 for now as its a new theme")]),
        c([sg.Text("")]),
        c([sg.Text("Next is the Creator. This is obviously you, so feel free to enter your name,")]),
        c([sg.Text("a nickname or however you want to be know. If you intend on uploading your")]),
        c([sg.Text("theme to the themes repository then try to use a unique user/creator name ")]),
        c([sg.Text("NOTE : The app will remember the creator name for next time")]),
        c([sg.Text("")]),
        c([sg.Text("If you have already generated a theme with this tool, you can choose to load")]),
        c([sg.Text("your custom theme to make any changes that you may need. this feature will")]),
        c([sg.Text("not work with downloaded or exported themes as it reads a custom file")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break    
            
def HELP2():    # Adding images
    layoutHELP = [
        [sg.Text("Adding images",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("Select browse on each of the lines to select the images that you")]),
        c([sg.Text("would like to use for the lockscreen and 10 livearea pages, you")]),
        c([sg.Text("can set a wave pattern and font color for each page if needed.")]),
        c([sg.Text("Click the 'Waves' button for a guide to the wave patterns")]),
        c([sg.Text("")]),
        c([sg.Text("This tool will resize and convert images to the Vitas requirements, but")]),
        c([sg.Text("for the best results, try and use horizontal images. Also when searcing")]),
        c([sg.Text("images on google, add the words 'desktop wallpaper' to the search box. ")]),
        c([sg.Text("")]),
        c([sg.Text("You should see a basic preview of your chosen images")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
            
def HELP3():    # layout and colors
    layoutHELP = [
        [sg.Text("Layout and colors",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("You can set a wave pattern and font color for each page if needed")]),
        c([sg.Text("by selecting a number from the menu list and clicking the color box")]),
        c([sg.Text("You can click the 'Waves' button for a guide to the wave patterns")]),
        c([sg.Text("")]),
        c([sg.Text("In the top right you can also select the lockscreen clock possition")]),
        c([sg.Text("and its color, you can also change the status bar/text colors")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break

def HELP4():    # Notifications
    layoutHELP = [
        [sg.Text("Notifications",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("The bottom right can show/hide an example of noticications popup")]),
        c([sg.Text("and icons. if you select the 'change' button this will open another")]),
        c([sg.Text("window where you can now select the color of the noticication bar")]),
        c([sg.Text("and the text color, but also you can change the noticication images")]),
        c([sg.Text("that represent when there is either a NEW or NO notification.")]),
        c([sg.Text("")]),
        c([sg.Text("In this new window you can either browse for an image, use the Vita")]),
        c([sg.Text("default image, or use a Capture mask to 'cutout' an image showing on")]),
        c([sg.Text("your computers screen. this feature acts like a screenshot function.")]),
        c([sg.Text("select 'capture mask', line up the window with a chosen section and")]),
        c([sg.Text("then select 'save snapshot' this image can be cloned to the other")]),
        c([sg.Text("and it can be made into a greyscale image.")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break

def HELP5():	# IconSets
    layoutHELP = [
        [sg.Text("IconSets",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("You can either select to use the default Vita icons, create a NEW icon set")]),
        c([sg.Text("or browse for a set that you have previously created using the IconBUILDER.")]),
        c([sg.Text("")]),
        c([sg.Text("The IconBUILDER can be used to quickly generate an iconset for your custom")]),
        c([sg.Text("theme. just select a background color and overlay image color for each icon")]),
        c([sg.Text("then select 'Create Icon Set' and give it a name to build your system icons")]),
        c([sg.Text("")]),
        c([sg.Text("The 2 buttons in the bottom left corner make it quicker to copy the colors")]),
        c([sg.Text("selected in the first box (Web Browser) to all the remaining system icons")]),
        c([sg.Text("")]),
        c([sg.Text("You can also select to open the capture mask by either pressing the button")]),
        c([sg.Text("labled O for each icon or 'open capture mask for ALL' at the bottom. The best")]),
        c([sg.Text("example for a use for this function is that you could find a textured image")]),
        c([sg.Text("and show it full screen, then use the capture mask feature to take a snapshot")]),
        c([sg.Text("of the texture for ALL icons in just 1 click, a bit like a cookie cutter.")]),
        c([sg.Text("")]),
        c([sg.Text("In the main app, a sample of yout chosen icons should be shown.")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break

def HELP6():	# Music
    layoutHELP = [
        [sg.Text("Background music",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("You can select an MP3 file, WAV file, or an already converted AT9 audio")]),
        c([sg.Text("to use as your background audio. You can Google 'YouTube to MP3' for")]),
        c([sg.Text("more help with how to download the MP3 audio from a Youtube video.")]),
        c([sg.Text("")]),
        c([sg.Text("There are multiple websites that allow you to grab just the MP3 audio")]),
        c([sg.Text("alternitively you can select to just use the default Vita audio.")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break

def HELP7():	# Generate theme
    layoutHELP = [
        [sg.Text("Generate theme",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("When you select to generate the theme you will be shown a window")]),
        c([sg.Text("with an automatically generated thumbnail image which is made up of")]),
        c([sg.Text("the 1st 4 images in your theme and the theme name in a color bar.")]),
        c([sg.Text("You can change the color of the text and bar, or remove the bar,")]),
        c([sg.Text("or remove both the text and bar. You can select another image or")]),
        c([sg.Text("use the capture mask to take a snapshot and create a thumbnail")]),
        c([sg.Text("")]),
        c([sg.Text("Once you are ready, just press -START- and your theme will be build")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
            
def HELP8():	# Install theme
    layoutHELP = [
        [sg.Text("Insalling the theme",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("Hopefully you should have already installed 'Custom Themes Manager' by RedSquirrel")]),
        c([sg.Text("You should have also generated a Theme and copied its folder from 'Created Themes'")]),
        c([sg.Text("to the location 'UX0:customtheme\' on your Vita or Playstation TV.")]),
        c([sg.Text("")]),
        c([sg.Text("Select the 3rd box on the top row, 'Install a Custom Theme from the local folder'")]),
        c([sg.Text("Select your theme and press X to show its preview and the START to install it.")]),
        c([sg.Text("Now select the 1st box 'Apply an installed theme' and select your theme and apply.")]),
        c([sg.Text("")]),
        c([sg.Text("IMPORTANT.!")]),
        c([sg.Text("If you need to remove/uninstall a theme, make sure you apply an alternitive theme")]),
        c([sg.Text("or the system default before uninstalling. You can remove installed themes by using")]),
        c([sg.Text("the 4th box on the top row 'Uninstall a Custom Theme', pressing START will remove")]),
        c([sg.Text("the theme from your device and also delete the files in 'UX0:customtheme\'")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
            
def HELP9():	# Issues
    layoutHELP = [
        [sg.Text("Possible issue",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("If you find that when you reboot your device, the installed themes is")]),
        c([sg.Text("no longer displayed, you can fix this by following this instruction.")]),
        c([sg.Text("")]),
        c([sg.Text("Open VitaShell and goto the location 'tm0:npdrm\'")]),
        c([sg.Text("Press Triangle and select 'New' then 'New file'")]),
        c([sg.Text("type in the file name 'act.dat'")]),
        c([sg.Text("you should now have the file 'tm0:npdrm/act.dat'")]),
        c([sg.Text("Press 'START' and then select 'Reboot'")]),
        c([sg.Text("")]),
        c([sg.Text("Now when you select a theme it should still be applied")]),
        c([sg.Text("when you reboot your device.")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break

def HELP10():	# Export
    layoutHELP = [
        [sg.Text("Exporting",font=('Helvetica', 18))],
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Text("When you generate your theme, the app will also generate a fake thumbnail image")]),
        c([sg.Text("for both the lockscreen and livearea. This is fine if the theme is just for")]),
        c([sg.Text("your own use, But if you are looking to add your created theme to the")]),
        c([sg.Text("PSVita Custom Themes - Free Repository, then you must add genuine screenshot")]),
        c([sg.Text("images to the generated theme. Just follow the steps below to do this.")]),
        c([sg.Text("")]),
        c([sg.Text("Transfer the theme to your system and apply it,")]),
        c([sg.Text("Goto the lockscreen by sleeping and waking the device,")]),
        c([sg.Text("Press 'PS' and 'START' at the same time to take a screenshot,")]),
        c([sg.Text("Unlock your system and goto your favourite livearea page,")]),
        c([sg.Text("Arrange some of the custom icons nicely to help show off the theme,")]),
        c([sg.Text("Press 'PS and 'START' again to take a screenshot of the Livearea,")]),
        c([sg.Text("Open VitaShell and press 'SELECT' to start the USB connection,")]),
        c([sg.Text("On the computer, press the 'Export' button,")]),
        c([sg.Text("The app should find the last 2 snapshots saved and show them here,")]),
        c([sg.Text("If the correct Lockscreen and Livearea page is shown then Export,")]),
        c([sg.Text("you exported (and ready to upload) .zip should be in the 'Exported' folder,")]),
        c([sg.Text("If the images are reversed the just press to swap them.")]),
        c([sg.Text("")]),
        c([sg.Text("If you dont see an 'Export' button, you need to generate the theme first.")]),
        c([sg.Text("If your images are detected wrong, try taking the snapshots again.")]),
        c([sg.Text("If you see an error when taking a snapshot, reboot the Vita and try again.")]),
        c([sg.Text("")]),
        [sg.HorizontalSeparator()],
        c([sg.Text("")]),
        c([sg.Button('Close',k='Close',s=20,bind_return_key=True)]),
        c([sg.Text("")]),
    ]
    
    layoutHELP_frame = [[sg.Column(layoutHELP)]]
	
    window = sg.Window('HELP',layoutHELP_frame,finalize=True,background_color='#009900',margins=(0,0),modal=False,keep_on_top=True,no_titlebar=True,grab_anywhere=True)
    window['Close'].SetFocus()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
            
MainMenu()