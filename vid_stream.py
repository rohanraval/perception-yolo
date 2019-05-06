import time

def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.01)
            continue
        yield line

if __name__ == '__main__':
    logfile = open('vid.out')
    loglines = follow(logfile)
    for line in loglines:
        if 'red' in line:
            print('STOP -- \tred light')
        elif 'green' in line:
            print('GO -- \tgreen light')
        elif 'yellow' in line:
            print('SLOW DOWN -- \tyellow light')
        elif 'pedestrian' in line:
            print('SLOW DOWN -- \tpedestrian may be crossing')
        elif 'sign' in line:
            print('SLOW DOWN -- \tread traffic signs')
        else:
            print()

