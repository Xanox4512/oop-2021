"""
Czyta info o aktualnym stanie procesora, i zostawia wyłącznie linie z info o aktualnej prędkości core'ów

Przykład output-u: freq.txt
"""
with open('/proc/cpuinfo') as f:
    lines = f.readlines()
    for l in lines:
        if not 'MHz' in l: continue
        print(l.strip())
