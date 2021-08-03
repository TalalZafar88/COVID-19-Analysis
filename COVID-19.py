import csv
from datetime import datetime

def todate(a):
    a = a.split('-')
    a = datetime(int(a[0]), int(a[1]), int(a[2])).date()
    return a

def Nmaxelements(list1, N):
    final_list = []
    size=None
    if len(list1) <N:
      size=len(list1)
    else:
      size=N
    for i in range(0, size):
        max1 = list1[0]

        for j in range(len(list1)):
            if list1[j].confirmed > max1.confirmed:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)
    for i in final_list:
     print(i.country_name,i.confirmed)

def lds(A,country):

    LDS = [[] for _ in range(len(A))]
    LDS[0].append(A[0])

    for i in range(1, len(A)):
        for j in range(i):
            if A[j] > A[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()
        LDS[i].append(A[i])

    j = 0
    for i in range(len(A)):
        if len(LDS[j]) < len(LDS[i]):
            j = i
    print('{} has a longest daily death toll decrease period of {}'.format(country,len(LDS[j])))
    print(LDS[j])


def FindMaxLength(A, B):
    n = len(A)
    m = len(B)

    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    for i in range(n -1, -1, -1):
        for j in range(m -1, -1, -1):
            if abs(A[i]-B[j])<=10:
                dp[i][j] = dp[i + 1][j + 1] + 1


    maxm = 0
    xin  = None
    yin  = None
    for i in range(0,n,1):
        for j in range(0,m,1):
               if(maxm<max(maxm, dp[i][j])):
                   maxm = max(maxm, dp[i][j])
                   xin = i
                   yin = j

    l1=[]
    l2=[]
    for i in range(maxm):
        l1.append(xin)
        l2.append(yin)
        xin+= 1
        yin+= 1
    length1=len(l1)
    length2=len(l2)
    final1=[]
    final2=[]
    for i in l1:
        final1.append(A[i])
    for i in l2:
        final2.append(B[i])

    print('The no of days are',maxm)
    print(final1,final2)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j].total < pivot.total:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def printknapSack(W, wt, val, n,names):
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    res = K[n][W]
    print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:

            print(names[i - 1].country,wt[i-1])

            res = res - val[i - 1]
            w = w - wt[i - 1]

class maxconfirm:
  def __init__(self,country,total):
    self.country=country
    self.total=total
    self.value=0

class Country:
  def __init__(self,cost):
    self.cost = cost

class data:
  def __init__(self,day,country,country_name,region,deaths,Cumulative_Deaths,Confirmed,Cumulative_Confirmed):
    self.day=todate(day)
    self.country = country
    self.country_name = country_name
    self.region = region
    self.deaths = deaths
    self.cumulative_deaths = Cumulative_Deaths
    self.confirmed = Confirmed
    self.cumulative_confirmed = Cumulative_Confirmed

with open('CountryWeight.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    a={}
    knapsack = []
    next(reader)
    for row in reader:
        a[row[0]]=Country(int(row[1]))
        a[row[0]]=[]
        knapsack.append(maxconfirm(row[0],int(row[1])))

dates={}
with open('WHO-COVID-19.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        temp=todate(row[0])
        q=data(row[0],row[1],row[2],row[3],int(row[4]),int(row[5]),int(row[6]),int(row[7]))
        if row[2] in a:
            a[row[2]].append(q)
        if temp not in dates:
            dates[temp]=[]
            dates[temp].append(data(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7])))
        else:
            dates[temp].append(data(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7])))


# query1
def query1():
    top20 = input('Enter date in yyyy-mm-dd format\n')
    top20 = todate(top20)

    if top20 in dates:
        Nmaxelements(dates[top20],20)
    else:
        print('Invalid Date')


# query2
def query2():
    dat1 = input('Enter date 1 in yyyy-mm-dd format\n')
    dat1 = todate(dat1)
    dat2 = input('Enter date 2 in yyyy-mm-dd format\n')
    dat2 = todate(dat2)

    n=0
    li=[]
    for keys,values in a.items():
        count=0
        for y in values:
            if(y.day>= dat1 and y.day<=dat2):
                count+= y.confirmed
        if(count>n):
            n=count
            li.clear()
            li.append(maxconfirm(keys,n))
        elif(count==n):
            li.append(maxconfirm(keys,count))

    for i in li:
        print("{} => {}".format(i.country, i.total))


# query3
def query3():
    f=input('Enter Country\n')
    n=0
    li=[]
    for x in a[f]:
       if(x.confirmed>n):
          n = x.confirmed
          li.append(x)

    fd=li[0].day
    ld=li[-1].day
    print("The longest spread period of {} consists of {} days from {} to {}".format(f,(ld-fd).days,fd,ld))
    for i in li:
        print("{}".format(i.confirmed))


# query4
def query4():
    f=input('Enter Country\n')
    li=[]
    for x in a[f]:
          li.append(x.deaths)

    lds(li,f)

# query5
def query5():
    value=[]
    cost=[]
    i=0
    for keys,values in a.items():
        knapsack[i].value=a[keys][-1].confirmed
        i+=1

    quickSort(knapsack,0,len(knapsack)-1)

    for k in knapsack:
        value.append(k.value)
        cost.append(k.total)

    W = 300
    n = len(value)
    printknapSack(W, cost, value, n,knapsack)

# query6
def query6():

    country1 = input('Enter first Country\n')
    country2 = input('Enter second Country\n')
    l1 = []
    l2 = []
    for x in a[country1]:
            l1.append(x.confirmed)
    for x in a[country2]:
            l2.append(x.confirmed)

    FindMaxLength(l1,l2)

while(True):
    print(' 1-Top 20 countries with the most confirmed cases on a given day.\n','2-The country(s) with the highest new cases between two given dates.\n',
          '3-The starting and ending days of the longest spread period for a given country.\n',
          '4-The longest daily death toll decrease period for a given country.\n','5-Finding the highest possible score attainable as well as the countries selected given a budget of 300.\n',
          '6-Compare the response of any two countries against this virus.\n','PRESS 9 TO EXIT\n','PLEASE SELECT OPTION.\n')

    inp=int(input())
    if   (inp == 1):
        query1()
    elif (inp == 2):
        query2()
    elif (inp == 3):
        query3()
    elif (inp == 4):
        query4()
    elif (inp == 5):
        query5()
    elif (inp == 6):
        query6()
    elif (inp == 9):
        exit()
    else:
        print('Invalid Input')

    print('\n\n')