This is a very beginner python jarvis file which is a little AI stuff
To run this in you PC,

1. First you have to download python from https://www.python.org
2. Download the jarvis file in a directory
3. Open VSCode ( or any preferable editor where batch file and VBS file can be written )
4. Now you can run the jarvis.py in your editor.

 
****To add it in startup:

1. Open the start.batch file and replace the second line with :
    
             python <path of your directory where you downloaded the Jarvis Folder from github>
   and add \jarvis.py in the end of the path


In my case , the 2nd line was: 
    python C:\Users\Prangon Chakraborty\OneDrive - BUET\Desktop\Jarvis\jarvis.py 
 

2. Now open jarvisFileOrganizer.vbs. Replace the "C:\Users\Prangon Chakraborty\OneDrive - BUET\Desktop\Jarvis\start.bat"
   with your path of directory where you downloaded the Jarvis Folder. Don't Forget to add \start.bat at the end of the
   path and most importantly, add quotation mark before and at the end of the line

  Example: "your directory path till Jarvis Folder\start.bat"

3. Now enable hidden items. For this, Go to This PC. Click the View Tab on the upper left corner of the window.
   and click the Hidden Items as marked

4. Now copy the start.bat file

5. Now traverse through the following path:
   
  C:\Users\Prangon Chakraborty\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup and paste the start.bat file here
 
  Here Replace "Prangon Chakraborty" with your username directory



*** Your batch file is successfully added to the startup. Now whenever you turn on your PC, you will see a notification that
    jarvis has started and jarvis will be ready for service ***
        