# Вариант 7
# Протарифицировать абонента с IP-адресом 87.245.198.147
# с коэффициентом k: 2руб/Мб
import os
import math
import matplotlib.pyplot as plt
import datetime

os.system("nfdump -r nfcapd.202002251200 >> input.txt")

def refacor():

    f=open('input.txt','r', encoding='utf-8')
    f.readline()
    data=[]
    while True:
        q=f.readline()
        a=q.split(' ')
        s=[]
        for i in a:
            if i=='':
                pass
            else:
                s.append(i)
        data.append(s)
        if q=='':
            break
    data=data[:-5]
    f.close()
    return data



def tarification(ip):
    data=refacor()
    coord=[]
    trafik=0

    for i in data:
        if i[5][:len(ip)]==ip or i[7][:len(ip)]==ip:
            if i[-2]=='M':
                trafik+=float(i[-3])
                coord.append([float(i[-3])*1024*1024,str(datetime.time(int(i[1][:2]),int(i[1][3:5]),int(i[1][6:8])))])
            else:
                trafik+=(float(i[-2])/1024)/1024
                coord.append([((float(i[-2]))), str(datetime.time(int(i[1][:2]),int(i[1][3:5]),int(i[1][6:8])))])


    trafik = math.ceil(trafik)
    print(coord)
    return [trafik,coord]



def grafik(coord):
    coord=sorted(coord, key=lambda student: student[1])
    x=[]
    y=[]
    for i in coord:
        x.append(i[0])
        y.append(i[1])
    ax = plt.axes()
    ax.set_ylabel("Bytes", fontsize=14)
    ax.set_xlabel("Time", fontsize=14)
    ax.plot(y, x)
    plt.savefig('graph.png')
    plt.show()

def main():
    f=open('output.txt', 'w',encoding='utf-8')
    a=tarification('87.245.198.147')
    f.writelines(str(a[0])+'Mb\n')
    f.writelines(str(a[0]*2)+' руб')
    grafik(a[1])
    f.close()

main()