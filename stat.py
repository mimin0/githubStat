##collecting statistics from github repo

#!/usr/bit/python
import subprocess


print(subprocess.check_output(["/usr/bin/git diff --numstat"], shell=True))