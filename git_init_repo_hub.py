import os

def git_command():
        git_terminal_command = ['echo "# Automate-Git-Init" >> README.md', 'git init',
                            'git add README.md', 'git add .','git commit -m "first commit"',
                            'hub create', 'git push -u origin master']
    
    for comd in git_terminal_command:
        os.system(comd)
    print("SUCCESS")           

# main
git_command()
