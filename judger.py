from subprocess import Popen,PIPE
import shlex,subprocess
import time,sys,os,easygui,signal
#from signal import SIGALRM
import threading
right=0
ii=0
try:
    filename=sys.argv[1];
    userfile=sys.argv[2];
    language=sys.argv[3];
except:
    print("Usage:name [filename.py] [filepath] [language]")
#print(language)
if (language=="C++"):
    #print(114514)
    os.system("gcc -O2 -g -o "+filename+".exe submit/"+filename)
ansdict={"AC":0,"WA":0,"TLE":0,"CE/RE":0}
logfile=open("data.log","w",encoding="utf-8")
# def TLEKill():
#     #global p
#     times=time.time()
#     while (time.time()-times<1.2):
#         if (OKflag==True):
#             return
#     try:
#         p.terminate()
#         #easygui.msgbox("TLE")
#         return
#     except:
#         return
def submit(i):
    global ansdict,right
    cinfile=open("testdatas/"+filename+"f/"+str(i+1)+".in","r")
    coutfile=open("testdatas/"+filename+"f/"+str(i+1)+".out","r")
        #try:
    #TLEKILL = threading.Thread(target=TLEKill)
        #except:
        #    easygui.msgbox("12345")
    #TLEKILL.start()
    
    rcode=0
    try:
        if (language=="Python"):
            process = subprocess.Popen("python "+userfile, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        elif (language=="C++"):
            process = subprocess.Popen(filename+".exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False)
        # 向子进程发送输入数据
        process.stdin.write(cinfile.read().encode("utf-8"))
        process.stdin.close()  # 关闭stdin，‌表示输入结束
        timea=time.time()
        # 等待子进程完成，‌并设置超时
        process.wait(timeout=1.5)
        if process.poll() is not None:
            proans = process.stdout.read().decode('utf-8')
            print(proans)
        else:
            #print(1)
            # 如果超时，‌终止子进程并返回超时错误
            process.terminate()
            timeb=time.time()-0.7
            logfile.write(str(i+1)+" TLE "+str(int((timeb-timea)*1000))+"ms\n")
    except subprocess.TimeoutExpired:
        #print(1)
        pass
    except subprocess.CalledProcessError as e:
        # 如果程序执行出错，‌返回错误信息
        rcode=1
        pass
    OKflag=True
    timeb=time.time()
    #print(1)
    #signal.alarm(0)
    if (timeb-timea>=1):
        ansdict["TLE"]+=1
        print(i+1,"TLE "+str(int((timeb-timea)*1000))+"ms")
        logfile.write(str(i+1)+" TLE "+str(int((timeb-timea)*1000))+"ms\n")
        i+=1
        return
    if (proans==""):
        print(i+1,"NOP "+str(int((timeb-timea)*1000))+"ms")
        i+=1
        return
    #proans=list(proans)
    #print(proans)
    tempans=[]
    gg=0
    #proans=proans.decode()
    for k in proans:
        if (k!='\r'):
            tempans+=k
            gg+=1
    proans=tempans
    gg=0
        #print(tempans)
        #proans=tempans
        #proans=proans.decode()
        #proans=proans.strip("\r\n")
    cans=coutfile.readlines()
    tempcans=""
        #print(cans)
    for k in cans:
        tempcans+=k
    cans=tempcans
        #cans.strip("\n")
        #proans.strip("\n\r")
        #proans.strip("\n")
        #if (proans[-1]==' '):
        #    proans=proans[0:len(proans)-2]
        #proans.split("\r")
        #print(list(proans))
        #print(list(cans))
    cans=list(cans)
    if (cans[-1]=="\n"):
        cans.pop()
    if (proans[-1]=="\n"):
        proans.pop()
    if (cans[-1]==" "):
        cans.pop()
    if (proans[-1]==" "):
        proans.pop()
    if (str(proans)==str(cans)):
        right+=1
        ansdict["AC"]+=1
        print(i+1,"AC "+str(int((timeb-timea)*1000))+"ms")
        logfile.write(str(i+1)+" AC "+str(int((timeb-timea)*1000))+"ms\n")
    else:
        if (rcode==0):
            ansdict["WA"]+=1
            print(i+1,"WA "+str(int((timeb-timea)*1000))+"ms")
            logfile.write(str(i+1)+" WA "+str(int((timeb-timea)*1000))+"ms\n")
        else:
            ansdict["RE/CE"]+=1
            print(i+1,"RE/CE "+str(int((timeb-timea)*1000))+"ms")
            logfile.write(str(i+1)+" RE/CE "+str(int((timeb-timea)*1000))+"ms\n")
    cinfile.close()
    coutfile.close()
            
    #except:
        #easygui.msgbox("123")
        #break
thr=[]
while True:
    try:
        cinfile=open("testdatas/"+filename+"f/"+str(ii+1)+".in","r")
        coutfile=open("testdatas/"+filename+"f/"+str(ii+1)+".out","r")
        cinfile.close()
        coutfile.close()
    except:
        break
    thr.append(threading.Thread(target=lambda:submit(ii)))
    thr[-1].start()
    ii+=1
time.sleep(1.8)
try:
    print(str((right)/(ii)*100)+"pts")
    logfile.write(str((right)/(ii)*100)+"pts\n")
    if (ansdict["AC"]==ii):
        print("Accepted")
        logfile.write("Accepted")
    elif (ansdict["AC"]>0):
        print("Partial Accepted")
        logfile.write("Partial Accepted")
    else:
        if (max(ansdict["WA"],ansdict["TLE"])==ansdict["WA"]):
            print("Wrong Answer")
            logfile.write("Wrong Answer")
        else:
            print("Time Limit Exceeded")
            logfile.write("Time Limit Exceeded")
    logfile.write("\n"+str((right)/(ii)*100))
    
except:
    print("0.0pts")
    logfile.write("0.0pts\n")
    logfile.write("System Error")
    logfile.write("\n0")
logfile.close()
