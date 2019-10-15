# your contributions here
import time

i = 3
snek1 ="""
                         ____
 _______________________/ O  \___/
<____________________________/   \ 
"""

snek2 ="""
    ____
\__/o   \____________________
/  \_________________________>
"""

for j in range(i):
    if j % 2 == 0:
        print(snek1)
    else:
        print(snek2)
    time.sleep(1)

       
