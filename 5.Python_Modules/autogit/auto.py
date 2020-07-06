from os import system


def git_panic(change = '*', message = 'This is a Panic Commit', branch = 'master'):
    system('git pull')
    system(f'git add {change}')
    system(f'git commit -m "{message}"')
    system(f'git push -u origin {branch}')
    system('git status')