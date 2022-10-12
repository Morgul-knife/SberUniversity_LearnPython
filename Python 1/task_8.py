N = int(input())
a = set(map(int,input().split(',')))
for i in range(1,N):
    str_in = set(map(int,input().split(',')))
    a.intersection_update(str_in)     
print(','.join(str(_) for _ in sorted(list(a))))

# l1 = '7,3,2,188'
# l2= '1,2,188,3,4,5'
# l3= '188, 3,2'
# N = 3
# a = set(map(int,l1.split(',')))
# str_in = set(map(int,l2.split(',')))
# a.intersection_update(str_in)
# # print(sorted(list(a)))
# # a = list(a)   
# # print(a) 
# # print(a.sort()) 
# print(' '.join(str(_) for _ in sorted(list(a))))