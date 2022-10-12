from datetime import datetime as dt
# N = 3
# sd = [dt.strptime('16:00',"%H:%M"), dt.strptime('16:00',"%H:%M"), dt.strptime('16:00',"%H:%M")]
# sa = [dt.strptime('19:00',"%H:%M"), dt.strptime('19:50',"%H:%M"), dt.strptime('19:00',"%H:%M")]
# ad = [dt.strptime('16:20',"%H:%M"), dt.strptime('16:20',"%H:%M"), dt.strptime('16:20',"%H:%M")]
# aa = [dt.strptime('19:10',"%H:%M"), dt.strptime('19:10',"%H:%M"), dt.strptime('19:50',"%H:%M")]

# sd = [dt.fromisoformat('2020-07-18T16:00'), dt.fromisoformat('2020-07-18T16:00'), dt.fromisoformat('2020-07-18T16:00')]
# sa = [dt.fromisoformat('2020-07-18T19:00'), dt.fromisoformat('2020-07-18T19:50'), dt.fromisoformat('2020-07-18T19:00')]
# ad = [dt.fromisoformat('2020-07-19T16:20'), dt.fromisoformat('2020-07-18T16:20'), dt.fromisoformat('2020-07-18T16:20')]
# aa = [dt.fromisoformat('2020-07-18T19:10'), dt.fromisoformat('2020-07-18T19:10'), dt.fromisoformat('2020-07-18T19:50')]

N = int(input())
sd = []
sa = []
ad = []
aa = []
for i in range(N):
    str_in = input()
    scheduled_departure = str_in.split(',')[0]
    scheduled_arrival = str_in.split(',')[1]
    actual_departure = str_in.split(',')[2]
    actual_arrival = str_in.split(',')[3]
    sd.append(dt.fromisoformat(scheduled_departure))
    sa.append(dt.fromisoformat(scheduled_arrival))
    ad.append(dt.fromisoformat(actual_departure))
    aa.append(dt.fromisoformat(actual_arrival))
# print(scheduled_departure, scheduled_arrival, actual_departure, actual_arrival)
# print(sd,sa,ad,aa)  
# print(abs(sd[0]-ad[0]).total_seconds() < 1200)
for i in range(N):
    if abs(sd[i]-ad[i]).total_seconds() < 1800 and abs(sa[i]-aa[i]).total_seconds() < 1800:
        print('Yes')
    else: print('No')
