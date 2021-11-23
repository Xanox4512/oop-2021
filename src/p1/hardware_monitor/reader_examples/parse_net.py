from dataclasses import dataclass

"""
Czyta dane z
/proc/net/dev

ze statystykami ruchu sieciowego na wszystkich kartach sieciowych. Przykład output: net.txt
"""

@dataclass
class NetworkStats:
    rx_bytes: int
    rx_pkts: int
    tx_bytes: int
    tx_pkts: int

with open('net.txt') as f:
    lines = f.readlines()
    for l in lines[2:]:
        no_multiple_space = ' '.join(l.split())
        print(no_multiple_space)
        numbers = [int(s) for s in no_multiple_space.split()[1:]]
        # print(numbers)
        stats = NetworkStats(numbers[0], numbers[1], numbers[8], numbers[9])
        print(stats)
