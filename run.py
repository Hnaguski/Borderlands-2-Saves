from subprocess import call
call(["git", "add", "."])
call(["git", "commit", "-a", "-m", "'\Save Updated\'"])
call(["git", "push", "origin", "master"])