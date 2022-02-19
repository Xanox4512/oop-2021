


with open('logs_cpu_temp/ex6.txt') as f:
    lines = f.read()
    lines = lines.split('\n\n')
    for e in lines:
        print('----------')
        print(e)
    print(len(lines))
    # for l in lines:
    #     print(float(l.strip().split(':')[1].strip()))
#