import os
import time
import dependant_file_installation as dfins

def git_command(git_path):
    # list of git command for terminal
    git_terminal_command = ['echo "# Automate-Git-Init" >> README.md', 'git init',
                            'git add README.md', 'git add .','git commit -m "first commit"',
                            'git remote add origin ' + git_path,
                            'git push -u origin master']
    
    # iterate every command
    for comd in git_terminal_command:
        os.system(comd)

    time.sleep(2)
    print("\n\nSUCCESS!")

##
## install brew
##
dfins.inst_brew()

##
## install dependency
##
d_app = ['git']
dfins.dependant_application(d_app)

##
## enter Github file path
##
g_path = input("Copy git repo path here and press enter:  ")

##
## main program
##
git_command(g_path)
