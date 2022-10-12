id = list(input().split(','))
N = int(input())
a = []
for i in range(N):
    str_in = input()
    ticket_no = str_in.split(',')[0]
    flight_id = str_in.split(',')[1]
    boarding_no = str_in.split(',')[2]
    seat_no = str_in.split(',')[3]
    str_out = ticket_no +','+ flight_id +','+ boarding_no +','+ seat_no
    if id.count(flight_id) != 0:
        str_out = ticket_no +','+ flight_id +','+ boarding_no +','+ seat_no 
        a.append(str_out) 
for i in a:
    print(i)   