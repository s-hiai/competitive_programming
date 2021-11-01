query_list = []
while True:
    n, x = map(int, input().strip().split())
    if n == 0 and x == 0:
        break
    query_list.append((n, x))

for n, x in query_list:
    result_count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    result_count += 1
    print(result_count)
                    


        
