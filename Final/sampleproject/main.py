# main.py
import src.settings as settings
import src.submodule as submodule

settings.init()          # Call only once
submodule.stuff()         # Do stuff with global var
print(settings.myList[0]) # Check the result
