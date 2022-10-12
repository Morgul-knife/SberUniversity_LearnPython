N = int(input())
# b = [3,3,1,1,4577,55,1,5,455]
# a = ['10;C','16;F','30;A','51;A','62;A','95;F','88;C','999;C','111;C']
b = []
a = []
for i in range(N):
    str_in = input()
    flight_id = int(str_in.split(',')[1])
    seat_no = str_in.split(',')[3]
    b.append(flight_id)
    a.append(seat_no)    
di = dict(zip(a,b)) # создание словаря из двух списков
# перевернутый словарь
flipped = {} 
for key, value in di.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
# сортировка словаря
flipped = dict(sorted(flipped.items()))
# печать
# print(di)
# print(flipped)
for i in range(len(flipped)):
    print(str(list(flipped.keys())[i]))
    print(','.join(list(flipped.values())[i])) 