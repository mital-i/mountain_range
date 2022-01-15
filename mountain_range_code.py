n = int(input())
tri_range = []

for i in range(n): 
    x, y = [int(i) for i in input().split()]
    tri_range.append((x-y, x+y, "s"))
    tri_range.append((x+y, x-y, "e"))
    
tri_range = sorted(tri_range, key= lambda x: x[0])
    
#print(tri_range)

tracker = [0]*(2*n)
tracker[0]=1

peaks = 0
s = 0
i = 0

while i < (2*n):
    if tri_range[i][2] == "e": 
        if tri_range[s][0] == tri_range[i][1]: 
            peaks+=1
            s = tracker.index(0)
            tracker[s]=1
            tracker[i]=1
        else: #it is an ending coordinate and it doesn't match with the first coordinate
            tracker[i]+=1
            tracker[tri_range.index((tri_range[i][1], tri_range[i][0], "s"))]+=1
            #stack.remove((tri_range[i][1], tri_range[i][0], "s"))
    #print(tracker, peaks, s, i)
    if s==i and s>0: 
        s+=1
        i+=2
    else: 
        i+=1
print(peaks)
#print(tracker)
