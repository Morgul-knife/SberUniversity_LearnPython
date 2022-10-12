N = int(input())
a = []
for i in range(N):
    str_in = input()
    ticket_no = str_in.split(',')[0]
    flight_id = str_in.split(',')[1]
    boarding_no = str_in.split(',')[2]
    seat_no = str_in.split(',')[3]
    str_out = ticket_no +','+ flight_id +','+ boarding_no +','+ seat_no
    if i == 0:
        a.append(str_out) 
    else:    
        s = ','
        for j in a:
            if j.find(s.join(str_out.split(',')[:2])) != -1:
                break
        else:
            a.append(str_out)
        # [a.append(str_out) for j in a if j.find(s.join(str_out.split(',')[:2])) == -1]
for i in a:
    print(i)   
