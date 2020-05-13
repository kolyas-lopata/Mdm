# Протарифицировать абонента с номером 933156729 с коэффициентом k:
# 4руб/минута исходящие звонки и входящие звонки до 0:30,
# 2руб/минута исходящие звонки и входящие звонки после 0:30,
# смс - 1,5руб/шт



import csv

def parsing(number):
    with open('data.csv', newline='') as csvfile:
        calls_before_00_30=[]
        calls_after_00_30=[]
        datareader = csv.reader(csvfile, delimiter=',')
        for row in datareader:
            print(row)
            if (row[1]==number or row[2]==number) and int(row[0][-5:-3])<30:
                calls_before_00_30.append(row)
            if (row[1]==number or row[2]==number) and int(row[0][-5:-3])>=30:
                calls_after_00_30.append(row)
        print(calls_before_00_30,calls_after_00_30)
        return calls_before_00_30,calls_after_00_30


def tariffication(before,after):
    calls = [0, 0]
    mes = 0.0
    for i in before:
        calls[0] += float(i[3])
        mes += float(i[4])
    for i in after:
        calls[1] += float(i[3])
        mes += float(i[4])
    x=calls[0]*4+calls[1]*2
    y=mes*1.5
    return (x,y)

def main():
    print('Введите номер абонента')
    number=str(input())
    s=parsing(number)
    s=tariffication(s[0],s[1])

    f=open('billing.txt', 'w', encoding='utf-8')
    f.write(str(s[0])+' - Счет за звонки\n')
    f.write(str(s[1])+' - Счет за СМС\n')
    f.write(str(s[0]+s[1])+' - Всего')
    f.close()

main()