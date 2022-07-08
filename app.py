import os
from random import randint

for i in range (365, 365 * 11):
    for j in range (1, randint(1, 5)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as f:
            f.write(d + '\n')
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin master')    