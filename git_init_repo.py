import os

def git_command(git_path):
    git_terminal_command = ['echo "# Automate-Git-Init" >> README.md', 'git init',
                            'git add README.md', 'git add .','git commit -m "first commit"',
                            'git remote add origin %s' % git_path,
                            'git push -u origin master']
    
    for comd in git_terminal_command:
        os.system(comd)
    print("SUCCESS")

# main
g_path = input("Copy git repo path here and press enter:  ")
git_command(g_path)
