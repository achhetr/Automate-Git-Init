import os
import time

def inst_brew():
    if os.system('which brew') != 0:
        print("Brew does not exist")
        time.sleep(0.8)
        print("Installing now.....")
        time.sleep(1.5)
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

def dependant_application(d_app):
    # list of dependant application for the project
    for dependant in d_app:
        if os.system('which ' + dependant) != 0:
            print(dependant + " does Not Exist")
            time.sleep(0.8)
            print("Installing now.. ")
            time.sleep(1.5)
            os.system("brew install " + dependant)