
"""
Czyta typowe dane /proce/cpuinfo i zamienia na liczby ułamkowe.

from cat /proc/cpuinfo | grep MHz | sort



"""

with open('freq.txt') as f:
    lines = f.readlines()
    for l in lines:
        print(float(l.strip().split(':')[1].strip()))
