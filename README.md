# Blue Print Renaming Automation for Make/Integromat
Make.com (formerly Integromat) is a great web based Low-Code Automation & Integration Tool that I have been utilizing in my current role. However, it has one simple flaw - anytime a Blueprint is exported to be shared with another Team Member, it does not retain its Title. 

This gave me the idea to create an atuomation that opens these files and renames them to the proper Title field.

# Details
This program is built using Python and the Tkinter Library for a simple interface. 

The interface allows you to select a Folder as your Source and a Folder as your Target. Once they have been selected, they are written to a text file to save for next time. 

*The reason that I am copying the Files into a new Folder is because I have a File Scanner that is monitoring my Downloads Folder which will interupt the script.

# How to Install / Run
I originally released an executer created with Pyinstaller but it needs to be debugged. For the time being, you will need to have Python Installed and launch the script from your terminal.

Once you have run the script once and saved your Source/Target Folders, I reccomend using an Event Based system like Task Scheduler (or Automator if you are using Apple) to run *rename_blueprint.py* when a File is added to your Source Folder (Downloads). This will allow you to rename your Blueprints as they are downloaded.

Thank you for reviewing my first Python Project!

