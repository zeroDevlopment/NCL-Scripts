from sys import argv, exit
import pandas as pd

try:
    with open(argv[1], 'r') as f1:
        raw = f1.read()
except IndexError as e:
    print("\n\tIncorrect syntax! Usage: nginxLog.py [LOG FILE]")
    exit(0)

rawLogs = raw.strip().split('\n')

def parseLogs(rawLogs):
    data = []

    for line in rawLogs:
        parts = line.split(" - - ")
        ip = parts[0]
        timePart, requestPart = parts[1].split('"', 1)
        time = timePart.strip()[1:-7]
        requestMsg, statusCodeSize, userAgentPart = requestPart.split('"',2)
        statusCode = statusCodeSize.strip().split(" ")[0]
        userAgent = userAgentPart.split('"')[-2] if userAgentPart else ""

        data.append([ip,time,requestMsg.strip(), statusCode, userAgent])

    df = pd.DataFrame(data, columns=['IP','Time','Message','Status','User Agent'])
    return df

d = parseLogs(rawLogs)
d.to_excel('nginxOutput.xlsx', index=False)
print('Finished')
