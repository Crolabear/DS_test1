import sys
import os

comment = sys.argv[1]
st1= 'git add *'
st2 = 'git commit -m %s' %comment
st3 = 'git push -u origin master'

os.system(st1)
os.system(st2)
os.system(st3)
