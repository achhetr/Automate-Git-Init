import os

def git_command(git_path):
    os.system('echo "# Automate-Git-Init" >> README.md')
    os.system("git init")
    os.system("git add README.md")
    os.system("git add .")
    os.system('git commit -m "first commit"')
    os.system("git remote add origin %s" % git_path)
    os.system("git push -u origin master")
    print("SUCCESS")

# main
g_path = input("Copy git repo path here and press enter:  ")
git_command(g_path)
