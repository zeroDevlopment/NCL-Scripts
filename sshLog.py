from sys import argv, exit
import pandas as pd

try:
    with open(argv[1], 'r') as f1:
        raw = f1.read()
except IndexError as e:
    print("\n\tIncorrect syntax! Usage: sshLog.py [LOG FILE]")
    exit(0)

rawLogs = raw.strip().split('\n')

def parseLogs(rawLogs):
    data = []

    for line in rawLogs:
        parts = line.split()
        date = f"{parts[0]} {parts[1]}"
        time = parts[2]
        systemName = parts[3]
        logType = parts[4].split('[')[0]
        logMsg = " ".join(parts[5:]).lstrip(": ")

        data.append([date,time,systemName,logType,logMsg])
    
    df = pd.DataFrame(data, columns=['Date','Time','System Name','Log Type','Message'])

    return df

df = parseLogs(rawLogs)

df.to_excel('sshOutput.xlsx', index=False)
print('Finished')