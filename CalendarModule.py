import datetime

mm,dd,yyyy = list(map(int,input().split()))
x = datetime.datetime(yyyy,mm,dd).strftime('%A').upper()
print(x)