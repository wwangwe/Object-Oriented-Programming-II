"""
Autogit Documentation

This Package helps you commit changes to your repo from your
python shell.
It is also useful for emergency commits, you can't afford to 
loose your code just because of a fire.

Modules:
    auto:
        functions:
            git_panic(change, message)

            Has three optional parameters
            change - Directory to changes of local repo to commit.
                   - Default(*)
            message - The message for the whole commit.
            branch - The branch of remote repo to commit to.

        The module uses the 'system' function from 'os'.
        It runs a 'git pull' prior to staging to avoid 'merge conflicts'
        After 'push'ing, it shows the 'status' of the repo.

Made with love Tim
"""