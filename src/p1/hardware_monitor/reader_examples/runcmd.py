"""
Przykład kodu wykonującego komendy systemowe, dające wgląd w pewne metryki systemu

Przykładowy output: logs_nvme
Typowy Unit to 512B
"""

# needs root access
import os

stream = os.popen('sensors')  # cpu temperature
# stream = os.popen('nvme smart-log /dev/nvme0n1')  #NVMe health
# stream = os.popen('cat /proc/cpuinfo | grep MHz | sort')  # cpu frequencies
lines = stream.readlines()
for l in lines:
    print(l.strip())
