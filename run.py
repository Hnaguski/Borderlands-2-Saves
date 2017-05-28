from subprocess import call
call(["git", "add", "."])
call(["git", "commit", "-a", "-m", "\'new commit\'"])
call(["git", "push", "origin", "master"])