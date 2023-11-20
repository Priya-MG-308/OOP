def largest(n):
    m=n[0]
    for i in range(len(n)):
        if(n[i]>m):
            m=n[i]

    return m

l=[12,45,6700,1007,2900]
ans=largest(l)
print("Largest is ",ans)
