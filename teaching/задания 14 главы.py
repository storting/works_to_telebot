n = int(input("nechetnoe chislo: "))
f = n
l = 0
q = -1
if n % 2 == 0:
    n = n + 1

s = [["."] * n for i in range(n)]
z = n - 2
for g in s:
    q += 1
    s[q][n // 2] = "*"
    for h in g:
        s[n // 2] = ["*"] * n
qq = len(s) - 1
for i in range(n):
    for y in range(n):
        if i == y:
            s[i][y] = '*'
        elif i + y == n - 1:
            s[i][y] = "*"
        
            
    
    
    
    

     
for i in s:
    for y in i:
        print(y, end = " ")
    print()

    



     
