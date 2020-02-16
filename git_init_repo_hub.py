import os
import time
import dependant_file_installation as dfins


def git_command():
    # list of git command for terminal
    git_terminal_command = ['echo "# Automate-Git-Init" >> README.md', 'git init',
                            'git add README.md', 'git add .','git commit -m "first commit"',
                            'hub create', 'git push -u origin master']
    
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
d_app = ['git','hub']
dfins.dependant_application(d_app)

##
## main program
##
git_command()
