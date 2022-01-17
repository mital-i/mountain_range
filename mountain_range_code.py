import heapq

n = int(input())
tri_range = []

for i in range(n): 
    x, y = [int(i) for i in input().split()]
    tri_range.append((x-y, x+y, "s"))
    tri_range.append((x+y, x-y, "e"))
    
tri_range = sorted(tri_range, key= lambda x: x[0])
    
print(tri_range)

tracker = [0]*(2*n)
tracker[0]=1

peaks = 0
s = 0
i = 0
peaks+=0
unvisited = []
heapq.heapify(unvisited)

for i in range (2*n):
    print(tri_range[s], tri_range[i], peaks)
    if (s==i): 
        continue 
    
    else: 
        if tri_range[i][2]=="s": #if overlapping dont do anything
            if tri_range[i][1] <= tri_range[s][1]: 
                continue
            else:  #if not overlapping, increment peaks
                heapq.heappush(unvisited, i)
                
        #if it is an end that corresponds to the first one, switch standard to the index in unvisited
        #and if unvisited is empty, then standard is simply the next one
        if tri_range[i][2]=="e":
            if tri_range[i][1]==tri_range[s][0]:
                peaks+=1
                if len(unvisited) <= 0 and i < (2*n-1):
                    s = i+1
                else:
                    s = heapq.heappop(unvisited)
print(peaks)
print(unvisited, u_i)
#print(tracker)
