N = int(input())
a = []
for i in range(N):
    str_in = input()
    ticket_no = str_in.split(',')[0]
    flight_id = str_in.split(',')[1]
    boarding_no = str_in.split(',')[2].replace('Номер:','')
    seat_no = str_in.split(',')[3]
    if seat_no.find(';') == -1:
        s = ';'
        l = len(seat_no)
        seat_no = s.join([seat_no[:l-1],seat_no[l-1]])
    str_out = ticket_no +','+ flight_id +','+ boarding_no +','+ seat_no
    a.append(str_out)
for i in range(N):
    print(a[i])   