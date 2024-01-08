# ImJustAKeyboardSir
Python script so that one does not have to manually dim their MacBook screen when using external displays. Usefull when the user does not want to use their MacBook display, but still wants to use the keyboard and trackpad of the MacBook.  

## When is this useful?

You have at least one external monitor and do not wish to use the MacBooks built in display. Generally to do this you would set the display to mirror your MacBook, and then dim the MaBook display to 0% to turn off the Mac's backlight. Unfortunatly, logging in, or opening the MacBook after it has been closed, causes the display to be set at 50% brightness, and it can be very annoying to constantly dim the display yourself. 

## How does it work?

This script listens for log in events or laptop opening events and uses a private Apple framework to dim the MacBooks screen. This is designed for Apple Silicon Macs, and has only been tested on a single M1 Pro MacBook. I doubt many besides myself will find it useful, but it took me ages to put together so if I can save someone else the trouble I will. Running the python script in terminal is enough for the effect to continue while the terminal is running. I've included a .plist file for if you would like to run the script in the background so you don't need to see the little dot under terminal in the dock. 

## Running in the background

To enable to script to run in the background:

1. Edit the plist file such that the first string in the ProgramArguments array is the location of your python3 installation
 * You can use `which python3` in terminal to find out the location
2. Edit the plist file such that the second string points to the location of the included python script, ImJustAKeyboardSir.py
3. Move the plist file into ~/Library/LaunchAgents
4. You can use `launchctl load ~/Library/LaunchAgents/local.ImJustAKeyboardSir.plist` in terminal to start the process without having to resart your MacBook.
5. The script should now be running in the background. You can test it by locking your MacBook and logging in again while connected to an external display. There will be no effect if there are no external displays connected. 
