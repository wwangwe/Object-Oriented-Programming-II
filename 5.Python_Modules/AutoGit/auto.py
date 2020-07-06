from os import system


def git_panic(change = '*', message = 'This is a Panic Commit'):
    system('git pull')
    system(f'git add {change}')
    system(f'git commit -m "{message}"')
    system('git push')
    system('git status')