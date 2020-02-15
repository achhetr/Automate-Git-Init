import os

def git_command(git_path):
    # git command for terminal
    git_terminal_command = ['echo "# Automate-Git-Init" >> README.md', 'git init',
                            'git add README.md', 'git add .','git commit -m "first commit"',
                            'git remote add origin %s' % git_path,
                            'git push -u origin master']
    
    # iterate every command
    for comd in git_terminal_command:
        os.system(comd)

    print("\n\nSUCCESS")

##
## main program
##
g_path = input("Copy git repo path here and press enter:  ")
git_command(g_path)
