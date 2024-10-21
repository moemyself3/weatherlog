# weatherlog.py
# Weather information is read by ssh response from weather station.
from config import Configuration

import time
import csv
import os
import paramiko

# create ssh client
ssh_client = paramiko.client.SSHClient()

# allow machine to auto add policy for missing host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect ssh client
ssh_client.connect(Configuration.SSH_HOST, username=Configuration.SSH_USER, password=Configuration.SSH_PASS)

# poll time in seconds
poll_time = 300 

while True:
    # read output from client
    _, stdout, _ = ssh_client.exec_command('')
    
    # parse output
    # example output: '2024-10-20T05:11:55 , 16.8 , 7.4 , 755.5\r\n' 
    line = stdout.readline()
    line = line.strip().split(' , ')

    fieldnames = ['time_UTC', 'temp_C', 'humidity', 'pressure_HPa']

    data = {
        fieldnames[0]: line[0],
        fieldnames[1]: line[1],
        fieldnames[2]: line[2],
        fieldnames[3]: line[3],
    }

    logfile = 'weatherlog.csv'

    if os.path.isfile(logfile):
        with open(logfile, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
    else:
        with open(logfile, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() 
            writer.writerow(data)
           
    time.sleep(poll_time)
